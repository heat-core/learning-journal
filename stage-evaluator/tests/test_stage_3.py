import unittest
from challenges.stage_3_rag_systems import VectorSearchEngine, CitationGroundingValidator

class TestStage3RAG(unittest.TestCase):
    def test_vector_search_ranking(self):
        engine = VectorSearchEngine()
        q_vec = [1.0, 0.0, 0.0]
        docs = [
            {"id": "doc1", "text": "About Python", "embedding": [0.9, 0.1, 0.0]},
            {"id": "doc2", "text": "About Cooking", "embedding": [0.0, 1.0, 0.0]},
            {"id": "doc3", "text": "About Machine Learning", "embedding": [0.8, 0.3, 0.0]},
        ]
        top = engine.rank(q_vec, docs, top_k=2)
        self.assertEqual(len(top), 2)
        self.assertEqual(top[0]["id"], "doc1")
        self.assertEqual(top[1]["id"], "doc3")

    def test_citation_grounding(self):
        context = ["FastAPI is a modern web framework for Python.", "PostgreSQL handles relational queries."]
        grounded_answer = "FastAPI is a Python web framework."
        hallucinated_answer = "Django utilizes MongoDB exclusively."
        self.assertTrue(CitationGroundingValidator.validate_grounding(grounded_answer, context))
        self.assertFalse(CitationGroundingValidator.validate_grounding(hallucinated_answer, context))

if __name__ == "__main__":
    unittest.main()
