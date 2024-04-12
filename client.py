from Utilities.g2ApiResponse import getReviewResults
from Utilities.KeyPhraseExtract import keywordGenerator
from Utilities.tf_idf import compute_tfidf_keywords
from Utilities.lemmatise import lemmatize_keywords_in_place
#Call function with parameter: Json output file path
review_list = getReviewResults("Utilities/g2ApiRespone.json")

#This response will call be sent as a parameter to the machine learning model
secondary_answers={}

for key, numbers in review_list[1].items():
    average = round(sum(numbers) / len(numbers), 1)
    secondary_answers[key] = average

print(secondary_answers)

print()
print()

key_corpus = {}
review_corpus={}
comment_answers = review_list[0]

for key in comment_answers:
    print(key)
    key_corpus[key] = []
    review_corpus[key]=[]
    for i in range(20):
        try:
            keywords = keywordGenerator(comment_answers[key][i])
            keywords = [word.lower() for word in keywords]
            review_corpus[key].append(comment_answers[key][i].lower())
            key_corpus[key].extend(keywords)
        except IndexError:
            break

    key_corpus[key] = lemmatize_keywords_in_place(key_corpus[key])
    print(compute_tfidf_keywords(key_corpus[key], review_corpus[key]))
    print()
    print()






