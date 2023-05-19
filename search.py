from collections import defaultdict
from elias_decoding import elias_decoding

def search(inv_index, df, encoding=0):
    query = input(" Enter the query : ")

    # Some preprocessing

    query = query.lower()
    query = query.strip()

    # now real work

    wordlist = query.split()
    search_words = [x for x in wordlist if x in inv_index]  # list of words that are present in index.

    print("\nsearching for words ... : ", search_words, "\n")

    doc_has_word = [(inv_index[word], word) for word in search_words]
    doc_words = defaultdict(list)

    for d, w in doc_has_word:
        for p in d:
            doc_words[p].append(w)

    # create a dictionary identifying matches for each document

    result_set = {}
    # print(doc_words.keys())
    for i in doc_words.keys():
        count = 0
        matches = len(doc_words[i])  # number of matches
        for w in doc_words[i]:
            count += len(inv_index[w])  # count total occurances
        result_set[i] = (matches, count)

    # Now print in sorted order

    # print(result_set)

    print("   Document \t\t Words matched \t\t Total Frequency ")
    print('-' * 40)
    for id in result_set:
        if encoding == 0:
            text = df['text'].loc[df['id'] == id].to_string()
        else:
            text = df['text'].loc[df['id'] == elias_decoding(id, encoding)].to_string()
        print(text, "\t", result_set[id][0], "\t", result_set[id][1])