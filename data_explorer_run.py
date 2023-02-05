
import numpy as np
import pandas as pd
from collections import Counter
from scripts.util.dir_path import DATA_CSV ,IMG
import seaborn as sns
import matplotlib.pyplot as plt

path = f'{DATA_CSV}/author_data.csv'
data = pd.read_csv(path)

authors = list(data['Author'].values)
text = list(data['Text'].values)

def get_authors_count():
    return Counter(authors)

def get_author_names(authors_count):
    return list(authors_count.keys())

def get_word_count():
    return np.array([len(sent.split()) for sent in text])

def get_char_count():
    return np.array([len(sent) for sent in text])

def get_average_length(word_count, char_count):
    return  char_count / word_count

def get_stats(var,title):
    print(f'{title}')    
    print('\t Min: ', np.min(var))
    print('\t Max: ', np.max(var))
    print('\t Середнє: ', np.mean(var))
    print('\t Медіана: ', np.median(var))
    print('\t Перцентиль 1%: ', np.percentile(var, 1))
    print('\t Перцентиль 95%: ', np.percentile(var, 95))
    print('\t Перцентиль 99%: ', np.percentile(var, 99))
    print('\t Перцентиль 99.5%: ', np.percentile(var, 99.5))
    print('\t Перцентиль 99.9%:', np.percentile(var, 99.9))
    print()

def distribution(var,title,xlabel,ylabel = 'Кількість речень' , save_path=f'{IMG}',visable=False, xlim_1=0, xlim_2=100):
    sns.distplot(var, kde=True, bins=80, color='blue').set_title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xlim(xlim_1,xlim_2)
    plt.savefig(f'{save_path}/{title}.png')

    if visable == True:
        plt.show()

def get_word_outliers_long(authors, text, word_count):
    word_outliers = np.where(word_count > 150)
    for i in word_outliers[0][:5]:
        print(f'Author: {authors[i]}, Довжина речення: {word_count[i]} слів')
        print(text[i], '\n')
    return word_outliers

def get_max_authors_outliers(authors, author_names, word_outliers):
    max_authors_outliers = {author : 0 for author in author_names}

    for i in word_outliers[0]:
        max_authors_outliers[authors[i]] += 1

    return Counter(max_authors_outliers)

def get_word_outliers_short(text, word_count):
    word_outliers = np.where(word_count < 3)

    for i in word_outliers[0][:10]:
        print(f'Довжина речення: {word_count[i]} слів')
        print(text[i], '\n')


authors_count = get_authors_count()
author_names = get_author_names(authors_count)

word_count = get_word_count()
char_count = get_char_count()
average_length = get_average_length(word_count, char_count)

get_stats(word_count,'Статистика кількості слів:')
distribution(word_count,'Розподіл кількості слів','Довжина речення в словах',xlim_2=100)

get_stats(char_count,'Статистика кількості символів:')
distribution(char_count,'Розподіл кількості символів','Довжина речення в символах',xlim_2=400)

get_stats(average_length,'Статистика середньої довжини:')
distribution(average_length,'Розподіл середньої довжини слова','Середня довжина слова в символах',xlim_2=10)

# Extremely long sentences
outliers_long = get_word_outliers_long(authors, text, word_count)
max_authors_outliers = get_max_authors_outliers(authors, author_names, outliers_long)

# Extremely short
outliers_short = get_word_outliers_short(text, word_count)