"""
Example script demonstrating the Florence module for traffic sign description.

This script shows how to use Microsoft's Florence model to generate
natural language descriptions of traffic sign images.
"""

import sys
import os

# Add parent directory to path to import traffic_sign module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from traffic_sign.florence import FlorenceDescriptor


def main():
    """Demonstrate Florence traffic sign description."""
    
    print("=" * 60)
    print("Florence Traffic Sign Description Example")
    print("=" * 60)
    print()
    
    # Initialize the descriptor
    print("Initializing Florence descriptor...")
    descriptor = FlorenceDescriptor(model_name="microsoft/florence-2-base")
    
    print("Note: This example requires:")
    print("  1. A traffic sign image file")
    print("  2. PyTorch and transformers installed")
    print("  3. Sufficient memory/GPU for the model")
    print()
    
    # Example usage (would need actual image)
    print("Example usage:")
    print("-" * 60)
    print("from traffic_sign.florence import FlorenceDescriptor")
    print()
    print("# Initialize")
    print("descriptor = FlorenceDescriptor()")
    print()
    print("# Describe a single traffic sign")
    print("description = descriptor.describe_traffic_sign('stop_sign.jpg')")
    print("print(f'Description: {description}')")
    print()
    print("# Batch process multiple signs")
    print("images = ['sign1.jpg', 'sign2.jpg', 'sign3.jpg']")
    print("descriptions = descriptor.batch_describe(images)")
    print("for img, desc in zip(images, descriptions):")
    print("    print(f'{img}: {desc}')")
    print("-" * 60)
    print()
    
    print("Sample expected output:")
    print("  'A red octagonal stop sign with white border and white letters'")
    print("  'A yellow diamond-shaped warning sign showing a pedestrian crossing'")
    print()
    
    print("Tips:")
    print("  - Use '<DETAILED_CAPTION>' for detailed descriptions")
    print("  - Use '<CAPTION>' for shorter descriptions")
    print("  - Use '<MORE_DETAILED_CAPTION>' for very detailed descriptions")
    print()


if __name__ == "__main__":
    main()
