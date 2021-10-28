import sys, os


project_template = {
    "scripts": "scripts",
    "cache": "cache",
    "built_images": "build/images",
    "built_metadata": "build/metadata",
    "simple_layer": "layers/simple",
    "complex_layer": "layers/colors",
}

RARITY_JSON_NAME = "rarity-config.json"

max_items = 10

image_size = (600, 700)

item_name = "Filemon"

description = "Schrödinger's cat who's name is Filemon"

engine_name = "Agent FUD Art Engine v0.1"

"""
We have 3 DNA generation types:
- 1: totally random DNA generation
- 2: random DNA generation based on rarity configuration
- 3 deterministic, all the possible DNA configurations will be generated
"""
dna_generation_type = 1

"""
When you run it multiple times if clear_project is True
then all the previously generated images and metadata files will be removed.
Otherwise files will be overwritten. 
"""
clear_project = True


try:
    sys.path.append(os.getcwd())
    from instance_config import *
except ImportError:
    pass
