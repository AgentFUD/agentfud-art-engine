from art_engine.simple_engine import SimpleEngine
from art_engine.complex_engine import ComplexEngine


class ArtEngineFactory:
    def __init__(self, config) -> None:
        self.config = config

    def getEngine(self):
        if self.config.engine_type == "simple":
            return SimpleEngine(self.config)
        elif self.config.engine_type == "complex":
            return ComplexEngine(self.config)
        else:
            raise Exception("Error, unknown engine type :(")
