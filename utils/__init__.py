import matplotlib.pyplot as plt
import pandas as pd


def load_datasets(feats):
    dfs = [pd.read_parquet(f'features/{f}_train.parquet') for f in feats]
    X_train = pd.concat(dfs, axis=1, sort=False)
    dfs = [pd.read_parquet(f'features/{f}_test.parquet') for f in feats]
    X_test = pd.concat(dfs, axis=1, sort=False)
    return X_train, X_test


def load_target(target_name):
    train = pd.read_csv('./data/input/train.csv')
    y_train = train[target_name]
    return y_train


def visualize_features_by_barh(labels, importances):
    plt.figure(figsize=(10, 6))
    plt.barh(y=range(len(importances)), width=importances)
    plt.yticks(ticks=range(len(labels)), labels=labels)
    plt.savefig('./features/importances/importances_barh.png')
