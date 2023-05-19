import pandas as pd
import nltk
from collections import defaultdict
from nltk.corpus import stopwords
from elias_encoding import elias_encoding


def inverted_index(df, encoding=0):
    inv_index = defaultdict(list)
    stop_arr = stopwords.words('russian')
    for doc, words in zip(
            df['id'],
            df.text.str.findall(r"\w+").map(set)
    ):
        i = 0
        for word in words:
            i += 1
            if word.lower() not in stop_arr:
                if encoding == 0:
                    inv_index[word.lower()].append(doc)
                else:
                    inv_index[word.lower()].append(elias_encoding(doc, encoding))

    return inv_index
