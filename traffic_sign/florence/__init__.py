"""
Florence module for traffic sign description using Microsoft's Florence model.

Florence is a vision-language foundation model that can generate detailed
descriptions of images, including traffic signs.
"""

from typing import Optional, Union
from PIL import Image
import torch


class FlorenceDescriptor:
    """
    Traffic sign descriptor using Florence model.
    
    This class provides methods to generate natural language descriptions
    of traffic signs using Microsoft's Florence generative AI model.
    """
    
    def __init__(self, model_name: str = "microsoft/florence-2-base", device: Optional[str] = None):
        """
        Initialize the Florence descriptor.
        
        Args:
            model_name: Name of the Florence model to use
            device: Device to run the model on ('cuda', 'cpu', or None for auto)
        """
        self.model_name = model_name
        self.device = device or ('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = None
        self.processor = None
        
    def load_model(self):
        """Load the Florence model and processor."""
        try:
            from transformers import AutoModelForCausalLM, AutoProcessor
            
            self.processor = AutoProcessor.from_pretrained(
                self.model_name, 
                trust_remote_code=True
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name, 
                trust_remote_code=True
            ).to(self.device)
            
            print(f"Florence model loaded on {self.device}")
            
        except Exception as e:
            print(f"Error loading Florence model: {e}")
            print("Note: Make sure transformers and torch are installed")
            raise
    
    def describe_traffic_sign(
        self, 
        image: Union[str, Image.Image],
        task: str = "<DETAILED_CAPTION>",
        max_new_tokens: int = 1024
    ) -> str:
        """
        Generate a description of a traffic sign.
        
        Args:
            image: Path to image file or PIL Image object
            task: Task prompt for Florence (e.g., '<DETAILED_CAPTION>', '<CAPTION>')
            max_new_tokens: Maximum number of tokens to generate
            
        Returns:
            Description of the traffic sign
        """
        if self.model is None:
            self.load_model()
        
        # Load image if path is provided
        if isinstance(image, str):
            image = Image.open(image).convert('RGB')
        
        # Process image
        inputs = self.processor(
            text=task,
            images=image,
            return_tensors="pt"
        ).to(self.device)
        
        # Generate description
        with torch.no_grad():
            generated_ids = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                num_beams=3
            )
        
        # Decode and return
        generated_text = self.processor.batch_decode(
            generated_ids, 
            skip_special_tokens=True
        )[0]
        
        # Extract the description from the generated text
        # Florence typically returns the task prompt followed by the result
        if task in generated_text:
            description = generated_text.replace(task, "").strip()
        else:
            description = generated_text.strip()
        
        return description
    
    def batch_describe(
        self,
        images: list[Union[str, Image.Image]],
        task: str = "<DETAILED_CAPTION>"
    ) -> list[str]:
        """
        Generate descriptions for multiple traffic signs.
        
        Args:
            images: List of image paths or PIL Image objects
            task: Task prompt for Florence
            
        Returns:
            List of descriptions for each traffic sign
        """
        descriptions = []
        for image in images:
            try:
                description = self.describe_traffic_sign(image, task)
                descriptions.append(description)
            except Exception as e:
                print(f"Error processing image: {e}")
                descriptions.append("")
        
        return descriptions


def describe_sign(image_path: str, model_name: str = "microsoft/florence-2-base") -> str:
    """
    Convenience function to describe a traffic sign.
    
    Args:
        image_path: Path to the traffic sign image
        model_name: Florence model to use
        
    Returns:
        Description of the traffic sign
    """
    descriptor = FlorenceDescriptor(model_name=model_name)
    return descriptor.describe_traffic_sign(image_path)
