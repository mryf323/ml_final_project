from sklearn.model_selection import train_test_split
import pandas as pd
import swifter
from google_drive_downloader import GoogleDriveDownloader as gdd


def load_dataset():
    gdd.download_file_from_google_drive(file_id='15JJ6ZysFM57tlUjXo2nHVhkGwePbVMVV', dest_path='./dataset.csv')
    dataset = pd.read_csv('./dataset.csv')
    dataset['sentiment'] = dataset['sentiment'].replace(['negative', 'positive'], [0, 1])
    return dataset


def preprocess_data(dataset, processor_chain=None, debug=False, debug_data_size=4000):
    X, Y = dataset['comment'], dataset['sentiment']
    if debug:
        X, Y = X[:debug_data_size], Y[:debug_data_size]
    if processor_chain:
        X = X.swifter.apply(processor_chain.process)
    return X, Y


def vectorize_data(X, Y, vectorizer):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)
    return X_train, X_test, Y_train, Y_test
