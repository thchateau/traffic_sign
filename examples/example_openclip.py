"""
Example script demonstrating the OpenCLIP module for traffic sign matching.

This script shows how to use OpenCLIP to compare traffic sign images
with text descriptions to find the best matches.
"""

import sys
import os

# Add parent directory to path to import traffic_sign module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from traffic_sign.openclip import TrafficSignMatcher, create_default_descriptions


def main():
    """Demonstrate OpenCLIP traffic sign matching."""
    
    print("=" * 60)
    print("OpenCLIP Traffic Sign Matching Example")
    print("=" * 60)
    print()
    
    # Initialize the matcher
    print("Initializing OpenCLIP matcher...")
    matcher = TrafficSignMatcher(model_name="ViT-B-32", pretrained="openai")
    
    print("Note: This example requires:")
    print("  1. Traffic sign image files")
    print("  2. PyTorch and open_clip_torch installed")
    print()
    
    # Load descriptions database
    print("Sample traffic sign descriptions database:")
    descriptions = create_default_descriptions()
    for i, desc in enumerate(descriptions[:5], 1):
        print(f"  {i}. {desc}")
    print(f"  ... and {len(descriptions) - 5} more")
    print()
    
    # Example usage
    print("Example usage:")
    print("-" * 60)
    print("from traffic_sign.openclip import TrafficSignMatcher")
    print()
    print("# Initialize matcher")
    print("matcher = TrafficSignMatcher()")
    print()
    print("# Load descriptions database")
    print("descriptions = [")
    print("    'stop sign, red octagonal sign with white text',")
    print("    'yield sign, red and white downward pointing triangle',")
    print("    'speed limit sign showing 50 km/h',")
    print("    # ... more descriptions")
    print("]")
    print("matcher.load_descriptions_database(descriptions)")
    print()
    print("# Find best match for an image")
    print("matches = matcher.find_best_match('my_sign.jpg', top_k=3)")
    print("for description, score in matches:")
    print("    print(f'{description}: {score:.3f}')")
    print()
    print("# Compare two images")
    print("similarity = matcher.compare_images('sign1.jpg', 'sign2.jpg')")
    print("print(f'Similarity: {similarity:.3f}')")
    print("-" * 60)
    print()
    
    print("Sample expected output:")
    print("  1. stop sign, red octagonal sign with white text: 0.923")
    print("  2. no entry sign, red circle with white horizontal bar: 0.785")
    print("  3. yield sign, red and white downward pointing triangle: 0.701")
    print()
    
    print("Use cases:")
    print("  - Match unknown traffic signs with known descriptions")
    print("  - Build a searchable database of traffic sign images")
    print("  - Find duplicate or similar traffic signs")
    print("  - Verify traffic sign recognition results")
    print()


if __name__ == "__main__":
    main()
