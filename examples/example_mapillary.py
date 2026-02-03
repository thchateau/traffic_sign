"""
Example script demonstrating the Mapillary API module for traffic sign detection.

This script shows how to use the Mapillary API to detect and recognize
traffic signs in street-level imagery.
"""

import sys
import os

# Add parent directory to path to import traffic_sign module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from traffic_sign.mapillary import MapillarySignDetector


def main():
    """Demonstrate Mapillary traffic sign detection."""
    
    print("=" * 60)
    print("Mapillary Traffic Sign Detection Example")
    print("=" * 60)
    print()
    
    print("Note: This example requires:")
    print("  1. A Mapillary API access token")
    print("  2. Set MAPILLARY_ACCESS_TOKEN environment variable")
    print("  3. Or pass token to MapillarySignDetector constructor")
    print()
    print("To get a Mapillary API token:")
    print("  1. Create account at https://www.mapillary.com/")
    print("  2. Go to https://www.mapillary.com/dashboard/developers")
    print("  3. Register an application and get your access token")
    print()
    
    # Example usage
    print("Example usage:")
    print("-" * 60)
    print("import os")
    print("from traffic_sign.mapillary import MapillarySignDetector")
    print()
    print("# Initialize with token")
    print("token = os.getenv('MAPILLARY_ACCESS_TOKEN')")
    print("detector = MapillarySignDetector(access_token=token)")
    print()
    print("# Search for traffic signs in a geographic area")
    print("# Bounding box: (min_lon, min_lat, max_lon, max_lat)")
    print("# Example: Paris center")
    print("bbox = (2.3, 48.85, 2.35, 48.87)")
    print("signs = detector.search_traffic_signs(bbox, limit=50)")
    print()
    print("print(f'Found {len(signs)} traffic signs')")
    print("for sign in signs[:3]:")
    print("    print(f\"Sign: {sign.get('value', 'unknown')}\")")
    print("    print(f\"Location: {sign.get('geometry', {})}\")")
    print("    print()")
    print()
    print("# Get detections for a specific image")
    print("image_id = '123456789'")
    print("detections = detector.get_image_detections(image_id)")
    print("print(f\"Image captured at: {detections.get('captured_at')}\")")
    print("print(f\"Detections: {len(detections.get('detections', []))}\")")
    print()
    print("# Search for images with traffic signs")
    print("images = detector.search_images_with_signs(bbox, limit=20)")
    print("for img in images[:3]:")
    print("    print(f\"Image ID: {img.get('id')}\")")
    print("    print(f\"URL: {img.get('thumb_2048_url')}\")")
    print("    print(f\"Signs detected: {len(img.get('detections', []))}\")")
    print("-" * 60)
    print()
    
    print("Sample expected output:")
    print("  Found 47 traffic signs")
    print("  Sign: regulatory--stop")
    print("  Location: {'type': 'Point', 'coordinates': [2.3234, 48.8567]}")
    print()
    print("  Sign: warning--pedestrian-crossing")
    print("  Location: {'type': 'Point', 'coordinates': [2.3289, 48.8601]}")
    print()
    
    print("Common traffic sign value codes:")
    print("  - regulatory--stop: Stop sign")
    print("  - regulatory--yield: Yield sign")
    print("  - regulatory--no-entry: No entry sign")
    print("  - warning--curve-left: Left curve warning")
    print("  - warning--pedestrian-crossing: Pedestrian crossing")
    print("  - information--parking: Parking information")
    print()
    
    print("Use cases:")
    print("  - Map traffic signs in a specific area")
    print("  - Analyze traffic sign distribution")
    print("  - Validate traffic sign databases")
    print("  - Build datasets for computer vision models")
    print()


if __name__ == "__main__":
    main()
