import yaml
import spacy
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
import joblib

def load_dataset(file_path):
    with open(file_path, 'r') as file:
        dataset = yaml.safe_load(file)
    return dataset

def preprocess_dataset(dataset):
    X = []
    y = []
    for item in dataset:
        intent = item['intent']
        examples = item['examples']
        for example in examples:
            X.append(example)
            y.append(intent)
    return X, y

def print_progress(iteration, total):
    progress = (iteration + 1) / total * 100
    print(f"Training progress: {progress:.2f}%")

# Load dataset
dataset_path = 'dataset.yml'
dataset = load_dataset(dataset_path)

# Preprocess dataset
X, y = preprocess_dataset(dataset)

print("Loaded dataset:")
for item in dataset:
    intent = item['intent']
    examples = item['examples']
    print(f"Intent: {intent}")
    print(f"Examples: {examples}")

# Load pre-trained spaCy model
nlp = spacy.load("en_core_web_md")

# Function to vectorize text using spaCy word embeddings
def vectorize_text(text):
    doc = nlp(text)
    return doc.vector

# Vectorize the text data
X_vectors = np.array([vectorize_text(text) for text in X])

# Define pipeline with LinearSVC classifier
pipeline = Pipeline([
    ('clf', LinearSVC())
])

# Train pipeline
total_samples = len(X)
batch_size = 100  # Adjust batch size as needed
num_batches = total_samples // batch_size

for i in range(num_batches):
    X_batch = X_vectors[i * batch_size: (i + 1) * batch_size]
    y_batch = y[i * batch_size: (i + 1) * batch_size]

    # Fit the model with the current batch
    pipeline.fit(X_batch, y_batch)

    # Print progress
    print_progress(i, num_batches)

# Save trained model
model_path = 'intent_classifier_model.joblib'
joblib.dump(pipeline, model_path)

print("Model trained and saved successfully!")
