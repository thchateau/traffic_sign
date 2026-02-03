"""
OpenCLIP module for comparing traffic sign images with text descriptions.

OpenCLIP provides powerful vision-language models that can compare images
with textual descriptions to find the best matches.
"""

from typing import Union, Optional
from PIL import Image
import numpy as np
import torch


class TrafficSignMatcher:
    """
    Traffic sign matcher using OpenCLIP for image-text similarity.
    
    This class compares traffic sign images with a database of text descriptions
    to identify the most similar signs.
    """
    
    def __init__(
        self, 
        model_name: str = "ViT-B-32",
        pretrained: str = "openai",
        device: Optional[str] = None
    ):
        """
        Initialize the OpenCLIP matcher.
        
        Args:
            model_name: Name of the CLIP model architecture
            pretrained: Pretrained weights to use
            device: Device to run the model on ('cuda', 'cpu', or None for auto)
        """
        self.model_name = model_name
        self.pretrained = pretrained
        self.device = device or ('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = None
        self.preprocess = None
        self.tokenizer = None
        
        # Database of traffic sign descriptions
        self.descriptions_db = []
        self.description_embeddings = None
    
    def load_model(self):
        """Load the OpenCLIP model."""
        try:
            import open_clip
            
            self.model, _, self.preprocess = open_clip.create_model_and_transforms(
                self.model_name,
                pretrained=self.pretrained,
                device=self.device
            )
            self.tokenizer = open_clip.get_tokenizer(self.model_name)
            
            print(f"OpenCLIP model {self.model_name} loaded on {self.device}")
            
        except Exception as e:
            print(f"Error loading OpenCLIP model: {e}")
            print("Note: Make sure open_clip_torch is installed")
            raise
    
    def load_descriptions_database(self, descriptions: list[str]):
        """
        Load a database of traffic sign descriptions.
        
        Args:
            descriptions: List of text descriptions of traffic signs
        """
        if self.model is None:
            self.load_model()
        
        self.descriptions_db = descriptions
        
        # Encode all descriptions
        with torch.no_grad():
            text_tokens = self.tokenizer(descriptions).to(self.device)
            self.description_embeddings = self.model.encode_text(text_tokens)
            self.description_embeddings = self.description_embeddings / self.description_embeddings.norm(
                dim=-1, keepdim=True
            )
        
        print(f"Loaded {len(descriptions)} descriptions into database")
    
    def encode_image(self, image: Union[str, Image.Image]) -> torch.Tensor:
        """
        Encode an image to an embedding vector.
        
        Args:
            image: Path to image file or PIL Image object
            
        Returns:
            Normalized image embedding
        """
        if self.model is None:
            self.load_model()
        
        # Load image if path is provided
        if isinstance(image, str):
            image = Image.open(image).convert('RGB')
        
        # Preprocess and encode
        image_input = self.preprocess(image).unsqueeze(0).to(self.device)
        
        with torch.no_grad():
            image_embedding = self.model.encode_image(image_input)
            image_embedding = image_embedding / image_embedding.norm(dim=-1, keepdim=True)
        
        return image_embedding
    
    def find_best_match(
        self,
        image: Union[str, Image.Image],
        top_k: int = 1
    ) -> list[tuple[str, float]]:
        """
        Find the best matching description(s) for a traffic sign image.
        
        Args:
            image: Path to image file or PIL Image object
            top_k: Number of top matches to return
            
        Returns:
            List of (description, similarity_score) tuples
        """
        if not self.descriptions_db:
            raise ValueError("Description database is empty. Call load_descriptions_database first.")
        
        # Encode image
        image_embedding = self.encode_image(image)
        
        # Calculate similarities
        similarities = (image_embedding @ self.description_embeddings.T).squeeze(0)
        
        # Get top k matches
        top_indices = similarities.argsort(descending=True)[:top_k]
        
        results = [
            (self.descriptions_db[idx], similarities[idx].item())
            for idx in top_indices
        ]
        
        return results
    
    def compare_images(
        self,
        image1: Union[str, Image.Image],
        image2: Union[str, Image.Image]
    ) -> float:
        """
        Calculate similarity between two traffic sign images.
        
        Args:
            image1: First image (path or PIL Image)
            image2: Second image (path or PIL Image)
            
        Returns:
            Similarity score between 0 and 1
        """
        embedding1 = self.encode_image(image1)
        embedding2 = self.encode_image(image2)
        
        similarity = (embedding1 @ embedding2.T).item()
        
        return similarity


def create_default_descriptions() -> list[str]:
    """
    Create a default database of common traffic sign descriptions.
    
    Returns:
        List of traffic sign descriptions
    """
    descriptions = [
        "stop sign, red octagonal sign with white text",
        "yield sign, red and white downward pointing triangle",
        "speed limit sign showing 50 km/h",
        "speed limit sign showing 30 km/h",
        "speed limit sign showing 90 km/h",
        "no entry sign, red circle with white horizontal bar",
        "one way sign with arrow pointing right",
        "pedestrian crossing sign, blue with white figures",
        "school zone sign with children crossing symbol",
        "no parking sign, red circle with diagonal line",
        "construction ahead warning sign, orange with black symbols",
        "railroad crossing sign with X and RR letters",
        "sharp curve ahead warning sign",
        "traffic light ahead warning sign",
        "merge warning sign with two lanes becoming one",
    ]
    return descriptions


def match_sign(
    image_path: str,
    descriptions: Optional[list[str]] = None,
    top_k: int = 3
) -> list[tuple[str, float]]:
    """
    Convenience function to match a traffic sign with descriptions.
    
    Args:
        image_path: Path to the traffic sign image
        descriptions: List of descriptions to match against (uses default if None)
        top_k: Number of top matches to return
        
    Returns:
        List of (description, score) tuples
    """
    matcher = TrafficSignMatcher()
    
    if descriptions is None:
        descriptions = create_default_descriptions()
    
    matcher.load_descriptions_database(descriptions)
    return matcher.find_best_match(image_path, top_k=top_k)
