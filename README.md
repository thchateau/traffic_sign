# Traffic Sign Recognition

A comprehensive Python package for traffic sign recognition using three complementary approaches:

1. **Florence** (Microsoft) - Generative AI for detailed traffic sign descriptions
2. **OpenCLIP** - Image-text similarity for matching signs with description databases
3. **Mapillary API** - Geographic traffic sign detection in street-level imagery

## Features

- 🤖 **AI-Powered Descriptions**: Generate natural language descriptions of traffic signs using Microsoft's Florence model
- 🔍 **Smart Matching**: Compare traffic sign images with description databases using OpenCLIP
- 🗺️ **Geographic Detection**: Detect and map traffic signs using Mapillary's extensive street-level imagery database
- 🛠️ **Easy Integration**: Simple, modular API for each component
- 📚 **Comprehensive Examples**: Detailed usage examples for each module and combined workflows

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Basic Installation

```bash
git clone https://github.com/thchateau/traffic_sign.git
cd traffic_sign
pip install -r requirements.txt
```

### Dependencies

The package requires the following main dependencies:

- **PyTorch** - Deep learning framework
- **transformers** - For Florence model
- **open_clip_torch** - For OpenCLIP model
- **requests** - For Mapillary API calls
- **Pillow** - Image processing

See `requirements.txt` for the complete list.

## Quick Start

### 1. Florence - Traffic Sign Description

Generate natural language descriptions of traffic signs using Microsoft's Florence model:

```python
from traffic_sign.florence import FlorenceDescriptor

# Initialize the descriptor
descriptor = FlorenceDescriptor()

# Describe a traffic sign
description = descriptor.describe_traffic_sign('stop_sign.jpg')
print(description)
# Output: "A red octagonal stop sign with white border and white STOP text"
```

### 2. OpenCLIP - Image Matching

Match traffic sign images with a database of text descriptions:

```python
from traffic_sign.openclip import TrafficSignMatcher, create_default_descriptions

# Initialize matcher
matcher = TrafficSignMatcher()

# Load descriptions database
descriptions = create_default_descriptions()
matcher.load_descriptions_database(descriptions)

# Find best matches
matches = matcher.find_best_match('unknown_sign.jpg', top_k=3)
for description, score in matches:
    print(f"{description}: {score:.3f}")
```

### 3. Mapillary - Geographic Detection

Detect traffic signs in street-level imagery using Mapillary API:

```python
from traffic_sign.mapillary import MapillarySignDetector
import os

# Initialize with API token
detector = MapillarySignDetector(
    access_token=os.getenv('MAPILLARY_ACCESS_TOKEN')
)

# Search for signs in a geographic area (Paris example)
bbox = (2.3, 48.85, 2.35, 48.87)  # (min_lon, min_lat, max_lon, max_lat)
signs = detector.search_traffic_signs(bbox, limit=50)

print(f"Found {len(signs)} traffic signs")
for sign in signs[:5]:
    print(f"Type: {sign.get('value')}")
    print(f"Location: {sign.get('geometry')}")
```

## Module Documentation

### Florence Module

The Florence module uses Microsoft's Florence vision-language model for generating detailed descriptions of traffic signs.

**Key Classes:**
- `FlorenceDescriptor` - Main class for traffic sign description

**Key Methods:**
- `describe_traffic_sign(image)` - Generate description for a single sign
- `batch_describe(images)` - Process multiple signs at once

**Example:**
```python
from traffic_sign.florence import FlorenceDescriptor

descriptor = FlorenceDescriptor(model_name="microsoft/florence-2-base")
description = descriptor.describe_traffic_sign('sign.jpg')
```

See `examples/example_florence.py` for detailed usage.

### OpenCLIP Module

The OpenCLIP module provides image-text similarity matching for traffic sign recognition.

**Key Classes:**
- `TrafficSignMatcher` - Main class for image-text matching

**Key Methods:**
- `load_descriptions_database(descriptions)` - Load text descriptions
- `find_best_match(image, top_k)` - Find best matching descriptions
- `compare_images(image1, image2)` - Calculate image similarity

**Example:**
```python
from traffic_sign.openclip import TrafficSignMatcher

matcher = TrafficSignMatcher()
matcher.load_descriptions_database([
    'stop sign, red octagonal sign',
    'yield sign, red and white triangle',
])
matches = matcher.find_best_match('sign.jpg', top_k=3)
```

See `examples/example_openclip.py` for detailed usage.

### Mapillary Module

The Mapillary module provides access to Mapillary's traffic sign detection API.

**Key Classes:**
- `MapillarySignDetector` - Main class for API interaction

**Key Methods:**
- `search_traffic_signs(bbox, limit)` - Search for signs in an area
- `get_image_detections(image_id)` - Get detections for a specific image
- `search_images_with_signs(bbox, limit)` - Find images containing signs

**Setup:**
1. Create account at [https://www.mapillary.com/](https://www.mapillary.com/)
2. Get API token from [https://www.mapillary.com/dashboard/developers](https://www.mapillary.com/dashboard/developers)
3. Set `MAPILLARY_ACCESS_TOKEN` environment variable

**Example:**
```python
from traffic_sign.mapillary import MapillarySignDetector

detector = MapillarySignDetector(access_token='your_token')
bbox = (2.3, 48.85, 2.35, 48.87)
signs = detector.search_traffic_signs(bbox, limit=50)
```

See `examples/example_mapillary.py` for detailed usage.

## Complete Workflow

Combine all three approaches for comprehensive traffic sign analysis:

```python
from traffic_sign.florence import FlorenceDescriptor
from traffic_sign.openclip import TrafficSignMatcher
from traffic_sign.mapillary import MapillarySignDetector

# 1. Find signs using Mapillary
detector = MapillarySignDetector(access_token='your_token')
signs = detector.search_traffic_signs((2.3, 48.85, 2.35, 48.87), limit=20)

# 2. Generate descriptions with Florence
descriptor = FlorenceDescriptor()
descriptions = []
for sign in signs:
    # Download image and generate description
    desc = descriptor.describe_traffic_sign(image_path)
    descriptions.append(desc)

# 3. Match with known signs using OpenCLIP
matcher = TrafficSignMatcher()
matcher.load_descriptions_database(descriptions)
matches = matcher.find_best_match('unknown_sign.jpg', top_k=3)
```

See `examples/complete_workflow.py` for a detailed workflow example.

## Examples

All examples are located in the `examples/` directory:

- `example_florence.py` - Florence model usage
- `example_openclip.py` - OpenCLIP matching usage
- `example_mapillary.py` - Mapillary API usage
- `complete_workflow.py` - Combined workflow demonstration

Run examples:
```bash
python examples/example_florence.py
python examples/example_openclip.py
python examples/example_mapillary.py
python examples/complete_workflow.py
```

## Use Cases

### 1. Traffic Sign Inventory
- Map all traffic signs in a city using Mapillary
- Generate descriptions with Florence
- Build a comprehensive, searchable database

### 2. Sign Recognition System
- Process unknown signs with Florence for initial description
- Match with known signs using OpenCLIP
- Validate results with Mapillary's geographic data

### 3. Quality Assurance
- Compare AI-generated descriptions with database entries
- Verify sign classification accuracy
- Identify misclassified or damaged signs

### 4. Research and Analysis
- Study traffic sign distribution patterns
- Analyze regional variations in signage
- Create training datasets for ML models

## Project Structure

```
traffic_sign/
├── traffic_sign/           # Main package
│   ├── __init__.py        # Package initialization
│   ├── florence/          # Florence module
│   │   └── __init__.py
│   ├── openclip/          # OpenCLIP module
│   │   └── __init__.py
│   └── mapillary/         # Mapillary module
│       └── __init__.py
├── examples/              # Usage examples
│   ├── example_florence.py
│   ├── example_openclip.py
│   ├── example_mapillary.py
│   └── complete_workflow.py
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── LICENSE               # Project license
└── README.md             # This file
```

## Requirements

- Python 3.8+
- CUDA-capable GPU (recommended for Florence and OpenCLIP)
- Internet connection (for Mapillary API)
- Mapillary API token (for Mapillary module)

## Contributing

This is a student project for traffic sign recognition. Contributions, suggestions, and feedback are welcome!

## License

See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Microsoft Florence** - For the vision-language model
- **OpenAI CLIP** and **OpenCLIP** - For image-text matching capabilities
- **Mapillary** - For street-level imagery and traffic sign data

## Authors

Student project by a group of three students working on traffic sign recognition.

## Support

For questions or issues, please open an issue on the GitHub repository.
