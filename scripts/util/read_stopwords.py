import re
import scripts.util.dir_path as dt

def get_stopwords():
    with open(f'{dt.STOPWORDS}', encoding= 'utf-8') as file:
        stop_words_ua = re.sub(r'[.,!?\'\"]', '', file.read()).replace('[','').replace(']','').split(' ')
        return stop_words_ua

get_stopwords()