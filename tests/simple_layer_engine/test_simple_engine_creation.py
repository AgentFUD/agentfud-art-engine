from art_engine.engine_factory import ArtEngineFactory
import art_engine.config_files.simple_instance_config as config


def test_simple_engine_creation():
    factory = ArtEngineFactory(config)
    s = factory.getEngine()
    assert s is not None
    assert s.config.engine_type == "simple"
    assert s.config.traits is not None
    assert s.config.traits_excluded_from_metadata is not None


def test_setup():
    factory = ArtEngineFactory(config)
    s = factory.getEngine()
