class Tokenizer:
    def __init__(self, vocab: list[str]):
        self._vocab = self.itos = vocab
        self.stoi = self.define_mapping_stoi()

    def define_mapping_stoi(self):
        mapping = {ch: i for i, ch in enumerate(self._vocab)}
        return mapping
