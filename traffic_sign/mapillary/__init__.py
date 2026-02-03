"""
Mapillary API module for detecting traffic signs in images.

Mapillary provides a powerful API for detecting and recognizing traffic signs
in street-level imagery.
"""

from typing import Optional, Dict, List, Any
import requests
import json


class MapillarySignDetector:
    """
    Traffic sign detector using Mapillary API.
    
    This class provides methods to detect and recognize traffic signs in images
    using Mapillary's computer vision API.
    """
    
    def __init__(self, access_token: Optional[str] = None):
        """
        Initialize the Mapillary detector.
        
        Args:
            access_token: Mapillary API access token (can also be set via environment)
        """
        self.access_token = access_token
        self.base_url = "https://graph.mapillary.com"
        
        if not self.access_token:
            import os
            self.access_token = os.getenv('MAPILLARY_ACCESS_TOKEN')
        
        if not self.access_token:
            print("Warning: No Mapillary access token provided.")
            print("Set MAPILLARY_ACCESS_TOKEN environment variable or pass token to constructor.")
    
    def search_traffic_signs(
        self,
        bbox: tuple[float, float, float, float],
        limit: int = 100
    ) -> List[Dict[str, Any]]:
        """
        Search for traffic signs in a geographic bounding box.
        
        Args:
            bbox: Bounding box as (min_lon, min_lat, max_lon, max_lat)
            limit: Maximum number of results to return
            
        Returns:
            List of traffic sign detections with metadata
        """
        if not self.access_token:
            raise ValueError("Mapillary access token is required")
        
        # Construct query parameters
        params = {
            'access_token': self.access_token,
            'fields': 'id,value,first_seen_at,last_seen_at,geometry',
            'bbox': ','.join(map(str, bbox)),
            'limit': limit
        }
        
        # Query traffic signs from Mapillary
        url = f"{self.base_url}/map_features"
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            features = data.get('data', [])
            
            return features
            
        except requests.exceptions.RequestException as e:
            print(f"Error querying Mapillary API: {e}")
            return []
    
    def get_image_detections(
        self,
        image_id: str
    ) -> Dict[str, Any]:
        """
        Get traffic sign detections for a specific Mapillary image.
        
        Args:
            image_id: Mapillary image ID
            
        Returns:
            Dictionary containing detection information
        """
        if not self.access_token:
            raise ValueError("Mapillary access token is required")
        
        params = {
            'access_token': self.access_token,
            'fields': 'id,detections,thumb_2048_url,captured_at'
        }
        
        url = f"{self.base_url}/{image_id}"
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error getting image detections: {e}")
            return {}
    
    def search_images_with_signs(
        self,
        bbox: tuple[float, float, float, float],
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        limit: int = 50
    ) -> List[Dict[str, Any]]:
        """
        Search for images containing traffic signs in a geographic area.
        
        Args:
            bbox: Bounding box as (min_lon, min_lat, max_lon, max_lat)
            start_time: Start time filter (ISO 8601 format)
            end_time: End time filter (ISO 8601 format)
            limit: Maximum number of results
            
        Returns:
            List of images with traffic sign detections
        """
        if not self.access_token:
            raise ValueError("Mapillary access token is required")
        
        params = {
            'access_token': self.access_token,
            'fields': 'id,thumb_2048_url,detections,captured_at,geometry',
            'bbox': ','.join(map(str, bbox)),
            'limit': limit
        }
        
        if start_time:
            params['start_time'] = start_time
        if end_time:
            params['end_time'] = end_time
        
        url = f"{self.base_url}/images"
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            images = data.get('data', [])
            
            # Filter for images with traffic sign detections
            images_with_signs = []
            for img in images:
                detections = img.get('detections', [])
                if any('traffic_sign' in str(d.get('value', '')).lower() for d in detections):
                    images_with_signs.append(img)
            
            return images_with_signs
            
        except requests.exceptions.RequestException as e:
            print(f"Error searching images: {e}")
            return []
    
    def get_sign_value_info(self, value: str) -> Dict[str, str]:
        """
        Get information about a traffic sign value code.
        
        Args:
            value: Traffic sign value code from Mapillary
            
        Returns:
            Dictionary with sign information
        """
        # This is a simplified mapping - Mapillary has extensive sign taxonomies
        sign_info = {
            'regulatory--stop': 'Stop sign',
            'regulatory--yield': 'Yield sign',
            'regulatory--no-entry': 'No entry sign',
            'warning--curve-left': 'Left curve warning',
            'warning--curve-right': 'Right curve warning',
            'warning--pedestrian-crossing': 'Pedestrian crossing warning',
            'information--parking': 'Parking information sign',
        }
        
        return {
            'value': value,
            'description': sign_info.get(value, 'Unknown traffic sign'),
            'category': value.split('--')[0] if '--' in value else 'unknown'
        }


def detect_signs_in_area(
    bbox: tuple[float, float, float, float],
    access_token: Optional[str] = None,
    limit: int = 100
) -> List[Dict[str, Any]]:
    """
    Convenience function to detect traffic signs in a geographic area.
    
    Args:
        bbox: Bounding box as (min_lon, min_lat, max_lon, max_lat)
        access_token: Mapillary API access token
        limit: Maximum number of results
        
    Returns:
        List of traffic sign detections
    """
    detector = MapillarySignDetector(access_token=access_token)
    return detector.search_traffic_signs(bbox, limit=limit)


def get_image_signs(
    image_id: str,
    access_token: Optional[str] = None
) -> Dict[str, Any]:
    """
    Convenience function to get traffic signs in a Mapillary image.
    
    Args:
        image_id: Mapillary image ID
        access_token: Mapillary API access token
        
    Returns:
        Dictionary with image and detection information
    """
    detector = MapillarySignDetector(access_token=access_token)
    return detector.get_image_detections(image_id)
