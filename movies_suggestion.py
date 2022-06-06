import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class movies_suggestion:
    global data
    data = pd.read_csv('movies.csv', low_memory=False)
    def _generate_matrix(data):
        try:
            count = CountVectorizer(stop_words='english')
            count_matrix = count.fit_transform(data['soup'])
            cosine_sim = cosine_similarity(count_matrix, count_matrix)
            data = data.reset_index()
            return cosine_sim
        except Exception as e:
            return e
    try:
        sim = np.load('matrix.npy')
    except:
        sim = _generate_matrix(data)
        np.save('matrix.npy',sim, allow_pickle=False, fix_imports=False)

    def _get_recommendations(title, cosine_sim):
        try:
            indices = pd.Series(
                data.index, index=data['title']).drop_duplicates()
            idx = indices[title]
            sim_score = list(enumerate(cosine_sim[idx]))
            sim_score = sorted(sim_score, key=lambda x: x[1], reverse=True)
            sim_score = sim_score[1:11]
            movie_indices = [i[0] for i in sim_score]
            return data['title'].iloc[movie_indices]
        except KeyError:
            return 'Titolo non valido ', title
        except Exception as e:
            return 'Errore Generico ', e

    def _return_similars(similar):
        try:
            return similar
        except:
            return ''

    def ask_title():
        title = input('Inserisci il titolo del film: ')
        return title

    while True:
        similar = _get_recommendations(ask_title(), sim)
        print(similar)
        ris = input('Vuoi tovarne ancora?(y,n) ')
        if ris == 'n' or ris == 'N':
            break
