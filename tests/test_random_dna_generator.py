from art_engine.dna_generator import RandomGenerator

traits = ["Eye", "Height", "Wear"]

trait_options = {
    "Eye": ["Blue", "Red", "Brown"],
    "Height": ["Tall", "Short", "Average", "Mountain", "Dwarf"],
    "Wear": ["Glasses", "Trousers", "Headset", "Tie", "Wrist watch", "Earrings"],
}

s = RandomGenerator()


def test_random_basic():
    dnas = s.generate_dnas(
        traits=traits, trait_options=trait_options, collection_size=3, retries=1
    )
    assert len(dnas) == 3
    assert list(dnas[0].keys()) == traits
