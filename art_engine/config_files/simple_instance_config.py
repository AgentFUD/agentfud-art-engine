base_image = "./layers/Base.png"

traits = ["Background Color", "Body", "Foot", "Eye", "Mouth"]

traits_excluded_from_metadata = ["Body", "Foot"]

image_size = (600, 700)

item_name = "Filemon"

description = "Schrödinger's cat who's name is Filemon"

"""
We have 3 DNA generation types:
- 1: sequential; deterministic, all the possible DNA configurations will be generated
- 2: random; random DNA generation
- 3: random DNA generation based on rarity configuration
"""
dna_generation_type = 1

# The image url in metadata json files
image_url = "https://nft.anothernow.io/filemon-test/images"

##########################################################################
### WARNING!!! DO NOT EDIT BELOW THIS LINE, IT MIGHT BREAK THE ENGINE. ###
##########################################################################
engine_type = "simple"
