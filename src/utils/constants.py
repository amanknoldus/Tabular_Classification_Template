from pathlib import Path

path = Path(__file__).resolve().parent.parent
dataset_path = path / "dataset_directory"
dataset_file = dataset_path / "credit_card_data.csv"
