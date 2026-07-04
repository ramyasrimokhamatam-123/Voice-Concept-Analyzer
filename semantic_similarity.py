from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(student_text, reference_text):
    student_embedding = model.encode(student_text)
    reference_embedding = model.encode(reference_text)

    similarity = cosine_similarity(
        np.array(student_embedding).reshape(1, -1),
        np.array(reference_embedding).reshape(1, -1)
    )[0][0]

    similarity_percentage = round(similarity * 100, 2)

    return similarity_percentage