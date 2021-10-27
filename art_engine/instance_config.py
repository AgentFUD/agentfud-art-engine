traits = [
    "Background Color",
    "Color",
    "Body",
    "Ear",
    "Tail",
    "Eye",
    "Mouth",
    "Foot"
]

colors = {
    "Greenish": ["Body", "Ear", "Tail"],
    "Yellowish": ["Body", "Ear", "Tail"]
}

available_colors = ["Yellowish", "Greenish"]

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
