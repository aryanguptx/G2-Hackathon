import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


def lemmatize_keywords_in_place(keywords):
    """
    Lemmatize a list of keywords in place using NLTK.

    Args:
        keywords (list): List of strings representing keywords to be lemmatized.

    Returns:
        None. The input list keywords is modified in place with lemmatized keywords.
    """
    # Initialize the WordNet Lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Function to map POS tags from nltk.pos_tag to WordNet POS tags
    def get_wordnet_pos(tag):
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN  # default to noun if POS tag not found

    # Perform lemmatization for each keyword
    for i in range(len(keywords)):
        keyword = keywords[i]
        # Get POS tag for the keyword
        pos_tag = nltk.pos_tag([keyword])[0][1]
        # Map the POS tag to WordNet POS tag
        wordnet_pos = get_wordnet_pos(pos_tag)
        # Lemmatize the keyword
        lemma = lemmatizer.lemmatize(keyword, pos=wordnet_pos)
        # Update the keyword in the list with its lemma
        keywords[i] = lemma
    return keywords