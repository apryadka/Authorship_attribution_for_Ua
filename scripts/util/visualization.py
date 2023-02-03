from typing import List
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame


def log(object,df_hand = 10):
    if type(object) == type(pd.DataFrame()):
        print(object.head(df_hand))
    else:
        print(object)

def plot_confusion_matrix(cm, classes: List[str],
                          normalize: bool = False,
                          title: str = 'Confusion matrix',
                          cmap = plt.cm.Greens):
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print('Normalized confusion matrix')
    else:
        print('Unnormalized confusion matrix')

    print(cm)
       
    df_cm = pd.DataFrame(cm, index = classes,
                  columns = classes)
    sns.heatmap(df_cm, annot=True, cmap = cmap)
    plt.ylabel('Right author')
    plt.xlabel('Predicted author')
    plt.title(title)
    plt.show()

def plot_history_of_accurancy(history):
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model\'s accurancy')
    plt.ylabel('accurancy')
    plt.xlabel('epochs')
    plt.legend(['teaching data', 'test data'], loc='upper left')

def plot_history_of_loss(history):
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model\'s error')
    plt.ylabel('error')
    plt.xlabel('epochs')
    plt.legend(['teaching data', 'test data'], loc='upper left')

