from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import regex as re
from sklearn.base import BaseEstimator, TransformerMixin

class DataPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.stopwords = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        transformed_X = []
        for text in X:
            # lowercase the text 
            text = text.lower()

            # removing @user handle
            text = re.sub(r'\@\S+','',text)

            # removing any link present
            text = re.sub(r'http:\/\/\S+|https:\/\/\S+|www.[^ ]','',text)

            # removing any alpha numeric character present
            text = re.sub(r'[^\w\s]','',text)

            # replacing multiple white space character with single whitespace
            text = re.sub(r'\s+',' ',text)

            # removing any single letter present
            text = re.sub(r'\b\w\b','',text)

            clean_text = ''

            tokens = word_tokenize(text)

            for token in tokens:
                if token not in self.stopwords:
                    stem_word = self.stemmer.stem(token)
                    lemm_word = self.lemmatizer.lemmatize(stem_word, pos='v')
                    clean_text += (lemm_word+' ')

            transformed_X.append(clean_text.strip())

        return transformed_X



