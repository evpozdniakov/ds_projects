import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import chi2

# local modules
from helpers import figax
from helpers import logger
import constants

@logger
def visualize_correlation(X):
    if constants.DEBUG:
        fig, ax = figax(figsize=(15, 15), name='corr')
        sns.heatmap(ax=ax, data=X.corr(), annot=True)
        ax.set_title('Features correlation')
        plt.show()

@logger
def visualize_num_cols_importance(X, y, ax):
    num_cols = [col for col in constants.NUM_COLUMNS if col in list(X.columns)]

    f_classif_results = f_classif(X[num_cols], y)

    data = pd.DataFrame(data=f_classif_results[0], index=num_cols, columns=['value'])
    data.sort_values(by=['value'], inplace=True, ascending=False)

    sns.barplot(ax=ax, data=data, x='value', y=data.index)
    ax.set_title('Importance of numeric features')

@logger
def visualize_cat_cols_importance(X, y, ax):
    cat_cols = [col for col in constants.CAT_COLUMNS if col in list(X.columns)]

    chi2_results = chi2(X[cat_cols], y.astype('int'))

    data = pd.DataFrame(data=chi2_results[0], index=cat_cols, columns=['value'])
    data.sort_values(by=['value'], ascending=False, inplace=True)

    sns.barplot(ax=ax, data=data, x='value', y=data.index)
    ax.set_title('Importance of categorical features')

@logger
def select_features(data):
    X = data.select_dtypes(include=[np.number])

    # visualize_correlation(X)

    # if constants.TARGET_COLUMN_NAME in X.columns:
    #     X.drop(columns=[constants.TARGET_COLUMN_NAME], inplace=True)

    #     y = data[constants.TARGET_COLUMN_NAME]

    #     if constants.DEBUG:
    #         fig, ax = figax(figsize=(15, 15), rowcol=(2, 1), name='importance')

    #         visualize_cat_cols_importance(X, y, ax[0])
    #         visualize_num_cols_importance(X, y, ax[1])

    #         plt.show()


    columns_to_remove = [col for col in list(data.columns) if col not in list(X.columns)]
    data.drop(columns=columns_to_remove, inplace=True)

    columns_to_remove = [col for col in constants.EXCLUDE_FROM_TRAINING if col in list(data.columns)]
    data.drop(columns=columns_to_remove, inplace=True)

@logger
def draw_features_hist(data):
    # X = data.select_dtypes(include=[np.number])
    data[constants.FEATURES_TO_NORM].hist()
    plt.show()
