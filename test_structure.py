"""
Basic test to verify package structure without requiring dependencies.
This test checks that all modules are properly structured.
"""

import os
import sys

def test_package_structure():
    """Test that the package structure is correct."""
    print("Testing traffic_sign package structure...")
    print("=" * 60)
    
    # Check main package
    assert os.path.exists('traffic_sign/__init__.py'), "Main package init missing"
    print("✓ Main package exists")
    
    # Check submodules
    submodules = ['florence', 'openclip', 'mapillary']
    for module in submodules:
        module_path = f'traffic_sign/{module}/__init__.py'
        assert os.path.exists(module_path), f"{module} module missing"
        print(f"✓ {module} module exists")
    
    # Check examples
    examples = [
        'example_florence.py',
        'example_openclip.py',
        'example_mapillary.py',
        'complete_workflow.py'
    ]
    for example in examples:
        example_path = f'examples/{example}'
        assert os.path.exists(example_path), f"{example} missing"
        print(f"✓ {example} exists")
    
    # Check configuration files
    config_files = [
        'README.md',
        'requirements.txt',
        'setup.py',
        '.gitignore',
        '.env.template'
    ]
    for config in config_files:
        assert os.path.exists(config), f"{config} missing"
        print(f"✓ {config} exists")
    
    print("=" * 60)
    print("✅ All structure tests passed!")
    print()
    print("Next steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Run examples: python examples/example_florence.py")
    print("3. See README.md for full documentation")
    
    return True

if __name__ == "__main__":
    try:
        # Ensure we're in the repository root
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        test_package_structure()
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
