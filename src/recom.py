from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as distance
import pandas as pd
import numpy as np
import seaborn as sns


def recommender(username, data):
    count_vectorizer = CountVectorizer()
    sparse_matrix = count_vectorizer.fit_transform(data.values())
    print(list(count_vectorizer.vocabulary_.keys()))
    m = sparse_matrix.todense()
    print(m.shape)
    print(m[0])
    doc_term_matrix = sparse_matrix.todense()
    df = pd.DataFrame(doc_term_matrix,
                      columns=count_vectorizer.get_feature_names(),
                      index=data.keys())
    similarity_matrix = distance(df, df)
    print(similarity_matrix)

    sim_df = pd.DataFrame(
        similarity_matrix, columns=data.keys(), index=data.keys())
    sns.heatmap(sim_df, annot=True)
    # Remove diagonal max values and set those to 0
    np.fill_diagonal(sim_df.values, 0)
    print(sim_df)

    x = sim_df.idxmax().loc[username]
    print(x)

    return x
