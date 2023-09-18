import random

import pandas as pd
from nltk import word_tokenize
import nltk
from nltk.corpus import stopwords

# Downloads of nltk
nltk.download('punkt')
nltk.download('stopwords')

"""File 847 rows and 5 columns 
(news_title, reddit_title, sentiment, text, url)
"""
# Export .csv to a dataframe
NewsDataFrame = pd.read_csv(r'Data/Sentiment_dataset.csv')

# Array that will have all words and their respective sentiment
document = []
allWords = []

# Each title of each news
for phrase in NewsDataFrame['news_title']:
    # Sentiment of the title
    sentiment = NewsDataFrame.loc[NewsDataFrame['news_title'] == phrase, 'sentiment']

    # Each word of the title using
    for word in word_tokenize(phrase):
        allWords.append(word)
        if word not in stopwords.words('english'):
            document.append((word, sentiment.iloc[0]))

# Each description of each news
for desc in NewsDataFrame['text']:
    # Sentiment of the title
    sentiment = NewsDataFrame.loc[NewsDataFrame['text'] == desc, 'sentiment']

    # Each word of the title using
    for word in word_tokenize(desc):
        if word.lower() not in stopwords.words('english'):
            allWords.append(word.lower())
            document.append((word, sentiment.iloc[0]))

random.shuffle(document)
all_words = nltk.FreqDist(allWords)

word_features = list(all_words.keys())[:6000]


def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features


featureSets = [(find_features(word), sent) for (word, sent) in document]

train_features = featureSets[:5000]
test_features = featureSets[5000:]
print(train_features)
classifier = nltk.NaiveBayesClassifier.train(train_features)
print("Accuracy: ", (nltk.classify.accuracy(classifier, test_features)) * 100)
classifier.show_most_informative_features(15)
