from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer
import numpy as np


def preprocess_text(text):
    #To be done using nltk
    return text.lower().split()


def compute_tfidf_keywords(keywords, corpus, top_n=5):
    #Computes the TF-IDF scores for a given set of keywords within a corpus of reviews.

    tfidf_vectorizer = TfidfVectorizer(
        tokenizer=preprocess_text,
        stop_words='english',
        vocabulary=keywords  # Restrict vocabulary to keywords
    )

    pipeline = make_pipeline(
        FunctionTransformer(lambda x: x, validate=False),
        tfidf_vectorizer
    )

    tfidf_matrix = pipeline.fit_transform(corpus)
    feature_names = np.array(tfidf_vectorizer.get_feature_names_out())
    average_tfidf_scores = np.mean(tfidf_matrix, axis=0).A1
    sorted_indices = np.argsort(average_tfidf_scores)[::-1]
    top_keywords = feature_names[sorted_indices][:top_n]

    return top_keywords


def main():
    # Sample reviews (replace with your actual reviews)
    reviews = [
        "This product is great, it exceeded my expectations.",
        "I'm satisfied with the quality of this product.",
        "The product arrived on time and in good condition.",
        "I would highly recommend this product to others."
    ]

    # Sample keywords
    keywords = ["product", "great", "quality", "recommend"]

    top_keywords = compute_tfidf_keywords(keywords, reviews)

    print("Top Keywords:")
    for keyword in top_keywords:
        print(keyword)


if __name__ == "__main__":
    main()
