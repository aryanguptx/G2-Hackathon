from transformers import (
    TokenClassificationPipeline,
    AutoModelForTokenClassification,
    AutoTokenizer,
)
from transformers.pipelines import AggregationStrategy
import numpy as np


# Define keyphrase extraction pipeline
class KeyphraseExtractionPipeline(TokenClassificationPipeline):
    def __init__(self, model, *args, **kwargs):
        super().__init__(
            model=AutoModelForTokenClassification.from_pretrained(model),
            tokenizer=AutoTokenizer.from_pretrained(model),
            *args,
            **kwargs
        )

    def postprocess(self, all_outputs):
        results = super().postprocess(
            all_outputs=all_outputs,
            aggregation_strategy=AggregationStrategy.SIMPLE,
        )
        return np.unique([result.get("word").strip() for result in results])


def getKeywords(text):
    # Load pipeline
    model_name = "ml6team/keyphrase-extraction-kbir-kpcrowd"

    #Create a model instance
    extractor = KeyphraseExtractionPipeline(model=model_name)

    keyphrases = extractor(text)

    return (keyphrases)


if __name__ == "__main__":
    i = 5
    review = """G2 has helped our customers publicly validate us to prospects and has helped us build 
        pipeline and be considered for opportunities where we likely would not have been found otherwise. Also it has 
        aided as a great validation point for customers in meetings and demo's as to our market profile and position.  It 
        has helped us need less reference calls and enabled our customers to have a more open and valid place to voice 
        their opinion on us."""
    keysToIterate = ""

    #Running a test case to check how many iterations of extraction lead to 0 gradient

    while i > 0:
        keysToIterate = getKeywords(review)
        print(keysToIterate, len(keysToIterate))
        review = ' '.join(keysToIterate)
        i = i - 1
