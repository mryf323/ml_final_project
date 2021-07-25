import sklearn.metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score


def analysis(labels, predictions):
    print("Report: Classification\n", classification_report(labels, predictions, target_names=["positive", "negative"]))
    print("Matrix: Confusion\n", confusion_matrix(labels, predictions))
    print("Accuracy:\n", accuracy_score(labels, predictions))
    return f1_score(labels, predictions)

def evaluate_models_with_data(models, X_train, X_test, Y_train, Y_test):
    for name, model in models.items():
        print(f'------Evaluating {name}------')
        model.fit(X_train, Y_train)
        pred = model.predict(X_test)
        analysis(Y_test, pred)
