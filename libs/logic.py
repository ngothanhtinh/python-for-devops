import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """Search wikipedia for name"""

    result = wikipedia.search(name)
    return result


def phrase(name):
    """Return a phrase"""

    page = wiki(name)
    blob = TextBlob(page)
    noun_phrase = blob.noun_phrases
    return noun_phrase
