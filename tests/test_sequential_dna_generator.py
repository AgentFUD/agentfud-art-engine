from art_engine.dna_generator import SequentialGenerator
import pytest

traits = ["Eye", "Height", "Wear"]

trait_options = {
    "Eye": ["Blue", "Red", "Brown"],
    "Height": ["Tall", "Short", "Average", "Mountain", "Dwarf"],
    "Wear": ["Glasses", "Trousers", "Headset", "Tie", "Wrist watch", "Earrings"],
}

s = SequentialGenerator()


def test_sequential_basic():
    dnas = s.generate_dnas(
        traits=traits, trait_options=trait_options, collection_size=3, retries=0
    )
    expected = [
        {"Eye": "Blue", "Height": "Tall", "Wear": "Glasses"},
        {"Eye": "Blue", "Height": "Tall", "Wear": "Trousers"},
        {"Eye": "Blue", "Height": "Tall", "Wear": "Headset"},
    ]
    assert dnas == expected


def test_sequential_max():
    dnas = s.generate_dnas(
        traits=traits, trait_options=trait_options, collection_size=90, retries=3
    )
    last_expected = {"Eye": "Brown", "Height": "Dwarf", "Wear": "Earrings"}
    assert len(dnas) == 90
    assert dnas[-1] == last_expected


def test_bigger_than_max_collection_size():
    dnas = s.generate_dnas(
        traits=traits, trait_options=trait_options, collection_size=2000, retries=10
    )
    last_expected = {"Eye": "Brown", "Height": "Dwarf", "Wear": "Earrings"}
    assert len(dnas) == 90
    assert dnas[-1] == last_expected
