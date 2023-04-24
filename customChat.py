# Import llama_index and indexing the documents stored in the data folder

from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader

documents = SimpleDirectoryReader('data').load_data()

index = GPTSimpleVectorIndex(documents)

index.save_to_disk('index.json')

# Bonus (Not required in the code, but for optimisation)

# Read the index.json later on for doing the indexation only once (#MoneySaving)

index = GPTSimpleVectorIndex.load_from_disk('index.json')
