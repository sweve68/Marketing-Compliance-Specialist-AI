import json
data_path = "data/data.jsonl"

def load_dataset(data_path):
	# Load the dataset
	with open(data_path, 'r', encoding='utf-8') as f:
		dataset = [json.loads(line) for line in f]
	return dataset

def stat_dataset(dataset):
	# Initial dataset stats
	print("Num examples:", len(dataset))
	print("First example:")
	for message in dataset[0]["messages"]:
	    print(message)