import pandas as pd
from inverted_index import inverted_index
from search import search

file_path = "data/NewsfeedPost.json"

if __name__ == '__main__':
    df = pd.read_json(file_path)

    df['id'] = range(1, len(df) + 1)

    inv_index = inverted_index(df)
    # print(total_size(inv_index, verbose=False))
    inv_index_gamma = inverted_index(df, 1)

    # print(inv_index_gamma)
    # print(sys.getsizeof(inv_index_gamma))
    # print(total_size(inv_index_gamma, verbose=False))
    inv_index_delta = inverted_index(df, 2)

    # print(inv_index_delta)
    # print(total_size(inv_index_delta, verbose=False))

    search(inv_index, df)

    search(inv_index_gamma, df, 1)

    search(inv_index_delta, df, 2)
