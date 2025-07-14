
import tensorflow_hub as hub
import numpy as np
from data import pairs

# Load USE model (only loads once)
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Prepare embedded questions
questions = [q for q, a in pairs]
responses = [a for q, a in pairs]
question_embeddings = embed(questions)

def get_response(user_input):
    input_embedding = embed([user_input])
    similarities = np.inner(input_embedding, question_embeddings)[0]
    best_match = np.argmax(similarities)
    return responses[best_match]