import pandas as pd
import simplemma
from scripts.util.dir_path import DATA_CSV
from scripts.util.read_stopwords import get_stopwords

removed_st = []
lem_count = 0

def increment():
    global lem_count
    lem_count = lem_count+1

def clean_authors_works_dataFrame(path = f'{DATA_CSV}/author_data.csv'):
    df = pd.read_csv(path)
    df['Text'] = df['Text'].str.replace('[^\w\s]', '', regex=True).replace('  ', ' ', regex=True)
    df['Text'] = df['Text'].str.strip().str.lower()

    print('Видалення стоп-слів..')
    print(f'Усього  {len(get_stopwords())} стоп-слів')
    df['Text'] = df['Text'].apply(lambda w: stopwords(w))
    removed_st_set = set(removed_st)
    print(f'Стоп слова знайдені в тексті {len(removed_st_set)} слів')
    print(f'Готово! Усього видалино {len(removed_st)} стоп-слів')
    df.to_csv(f'{DATA_CSV}/preprocessed_data.csv', index=False)
    df = pd.read_csv(f'{DATA_CSV}/preprocessed_data.csv')
    print('Лементезація..')
    df['Text'] = df['Text'].apply(lambda t: lemmatization(t))
    print(f'Готово! Лемітизовано {lem_count} слів')
    df.to_csv(f'{DATA_CSV}/preprocessed_data.csv', index=False)
    return df

# Stopwords
def stopwords(data):
    data = str(data).split(' ')
    text = []
    stopwords = get_stopwords()
    for word in data:
        if word in stopwords:
            removed_st.append(word)
        if word not in stopwords:
            text.append(word)
    return ''.join(str(w + ' ') for w in text)


def stopwords_dataFrame(dataFrame):
   dataFrame['Text'] = dataFrame['Text'].apply(lambda s: stopwords(s))
   dataFrame.to_csv(f'{DATA_CSV}/stopwords_clean_data.csv', index=False)
   return dataFrame


# Lemmatization
def lemmatization(data):
    data = str(data).split(' ')
    text = []
    for word in data:
        if word != '':
            w = text.append(simplemma.lemmatize(word, lang='uk'))
        if w != word:
           increment()

    return ''.join(str(w + ' ') for w in text)
        

def lemmatization_dataFrame(dataFrame):
   dataFrame['Text'] = dataFrame['Text'].apply(lambda l: lemmatization(l))
   dataFrame.to_csv(f'{DATA_CSV}/lemmatization_data.csv', index=False)
   return dataFrame
