# embedded.py
import tensorflow_hub as hub
import numpy as np
from data import pairs

# Output file name (change if you want different versions)
OUTPUT_FILE = "embeddings.npy"

print("[INFO] Loading Universal Sentence Encoder model...")
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Separate questions and responses
questions = [q for q, a in pairs]
responses = [a for q, a in pairs]

print(f"[INFO] Generating embeddings for {len(questions)} questions...")
question_embeddings = embed(questions)

# Save embeddings and responses together in a structured file
print(f"[INFO] Saving embeddings to '{OUTPUT_FILE}'...")
np.save(OUTPUT_FILE, {
    "embeddings": question_embeddings.numpy(),
    "responses": responses,
    "questions": questions
})

print("[SUCCESS] Embeddings generated and saved!")