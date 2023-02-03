import os
import numpy as np
import random
import pandas as pd
from nltk import tokenize, download
import scripts.util.dir_path as dt
from typing import List
from scripts.util.work_with_files import read_data_docx,read_file,save_data_txt

#download('punkt')

def split_text(filepath: str, min_char: int = 5) -> List[str]:
    text = str()
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read().replace('\n', '.')
    sentences = tokenize.sent_tokenize(text)    
    sentences = [sentence.replace('\n','') for sentence in sentences if len(sentence) >= min_char]
    return list(sentences)


def create_authors_works_files(path = dt.DATA):
    os.makedirs(f'{dt.DATA_TXT}', exist_ok=True)
    dir_list = os.listdir(path)
    for dir in dir_list:
        author = read_data_docx(f'{path}/{dir}')
        save_data_txt(author, f'{dt.DATA_TXT}/{dir}.txt')
    print(f'Data saved to files')


def create_dist(path):
    authors = [] * 2
    dirs = os.listdir(dt.DATA)
    for dir in dirs:
        authors.append(read_file(f'{path}/{dir}.txt'))
    dist = {i: authors[i] for i in range(len(authors))}
    return dist


def create_authors_works_dataFrame(max_row_len = 2000):
    dist = create_dist(dt.DATA_TXT)

    authors_names = os.listdir(dt.DATA)
    for key in dist.keys():
        print(authors_names[key], ':', len(dist[key]), ' речень')

    np.random.seed(1)
    #max_row_len = 100

    dist_data = []
    for data in dist.keys():
        dist_data.append(dist[data])

    dist_combined_data = []
    for data in dist_data:   
        data = np.random.choice(data, max_row_len,replace=False)
        dist_combined_data +=list(data) 

    combined = []
    for combined_data in  dist_combined_data :
        combined.append(combined_data.strip().replace('\n',''))

    labels = []
    dirs = os.listdir(dt.DATA)

    for dir in dirs:
        for _ in range(max_row_len):
            labels.append(dir.replace('\n',''))

    print('Довжина позначеного списку:', len(labels))
    print('Довжина комбінованого та внутрішньо перетасованого списку:', len(combined))

    np.random.seed(1)
    zipped = list(zip(combined, labels))
    random.shuffle(zipped)
    combined, labels = zip(*zipped)

    data_frame = pd.DataFrame()
    data_frame['Text'] = combined
    data_frame['Author'] = labels

    print(len(combined) == len(labels))
    os.makedirs(f'{dt.DATA_CSV}/', exist_ok=True)
    data_frame.to_csv(f'{dt.DATA_CSV}/author_data.csv', index=False)
    return data_frame
