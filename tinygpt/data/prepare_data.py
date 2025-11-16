from datasets import load_dataset
import tqdm


class PrepareData:
    def __init__(self) -> None: ...

    def load_dataset(self, dataset_name="roneneldan/TinyStories"):
        ds = load_dataset(dataset_name, streaming=True)

        # Training and Validation set
        training_set = ds["train"]
        validation_set = ds["validation"]

        with open("training.txt", "w") as f:
            for chunk in training_set:
                text = chunk["text"]  # type: ignore
                text.lower()
                filtered = text.encode("ascii", "ignore").decode()
                f.write(filtered + "\n")
        with open("validation.txt", "w") as f:
            for chunk in validation_set:
                text = chunk["text"]  # type: ignore
                text.lower()
                filtered = text.encode("ascii", "ignore").decode()
                f.write(filtered + "\n")
