import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, LeaveOneOut
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

import warnings

# Ignorar todos los warnings
warnings.filterwarnings("ignore")

# Función para cargar datasets locales considerando sus formatos específicos
def load_dataset(dataset_name):
    if dataset_name == "iris":
        # Leer archivo iris.data (CSV sin encabezados, última columna es categórica)
        file_path = "Datasets/iris.data"
        data = pd.read_csv(file_path, header=None)
        X = data.iloc[:, :-1]  # Todas las columnas excepto la última
        y = data.iloc[:, -1]  # Última columna
        # Convertir etiquetas categóricas a numéricas
        y = y.astype('category').cat.codes
    elif dataset_name == "pima-diabetes":
        # Leer archivo Pima Diabetes (CSV con encabezados y valores numéricos)
        file_path = "Datasets/pima-indians-diabetes.csv"
        data = pd.read_csv(file_path, header=None)
        X = data.iloc[:, :-1]  # Todas las columnas excepto la última
        y = data.iloc[:, -1]  # Última columna
    elif dataset_name == "seeds":
        # Leer archivo seeds.txt (separado por tabulaciones, sin encabezados)
        file_path = "Datasets/seeds_dataset.txt"
        data = pd.read_csv(file_path, sep="\t", header=None)
        X = data.iloc[:, :-1]  # Todas las columnas excepto la última
        y = data.iloc[:, -1] - 1  # Última columna (ajuste para iniciar desde 0)
    else:
        raise ValueError("Dataset desconocido")
    return X.to_numpy(), y.to_numpy()

# Clasificador Naive Bayes
def naive_bayes(X_train, X_test, y_train, y_test):
    model = GaussianNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_pred

# Clasificador KNN
def knn(X_train, X_test, y_train, y_test, k=3):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_pred

# Evaluación del desempeño
def evaluate_model(y_test, y_pred):
    acc = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    return acc, conf_matrix

# Validación Hold-Out
def hold_out(X, y, classifier, k=None):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    if classifier == "naive_bayes":
        y_pred = naive_bayes(X_train, X_test, y_train, y_test)
    elif classifier == "knn":
        y_pred = knn(X_train, X_test, y_train, y_test, k=k)
    return evaluate_model(y_test, y_pred)

# Validación cruzada 10-Fold
def k_fold_validation(X, y, classifier, k=None):
    kf = KFold(n_splits=10, shuffle=True, random_state=42)
    accuracies = []
    for train_idx, test_idx in kf.split(X):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        if classifier == "naive_bayes":
            y_pred = naive_bayes(X_train, X_test, y_train, y_test)
        elif classifier == "knn":
            y_pred = knn(X_train, X_test, y_train, y_test, k=k)
        acc, _ = evaluate_model(y_test, y_pred)
        accuracies.append(acc)
    return np.mean(accuracies)

# Leave-One-Out
def leave_one_out_validation(X, y, classifier, k=None):
    loo = LeaveOneOut()
    accuracies = []
    for train_idx, test_idx in loo.split(X):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        if classifier == "naive_bayes":
            y_pred = naive_bayes(X_train, X_test, y_train, y_test)
        elif classifier == "knn":
            y_pred = knn(X_train, X_test, y_train, y_test, k=k)
        acc, _ = evaluate_model(y_test, y_pred)
        accuracies.append(acc)
    return np.mean(accuracies)

# Main
datasets = ["iris", "pima-diabetes", "seeds"]
for dataset_name in datasets:
    print(f"Dataset: {dataset_name}")
    X, y = load_dataset(dataset_name)

    print("Hold-Out Validation (Naive Bayes):", hold_out(X, y, "naive_bayes"))
    print("10-Fold Cross-Validation (Naive Bayes):", k_fold_validation(X, y, "naive_bayes"))
    print("Leave-One-Out (Naive Bayes):", leave_one_out_validation(X, y, "naive_bayes"))

    print("Hold-Out Validation (KNN):", hold_out(X, y, "knn", k=5))
    print("10-Fold Cross-Validation (KNN):", k_fold_validation(X, y, "knn", k=5))
    print("Leave-One-Out (KNN):", leave_one_out_validation(X, y, "knn", k=5))
    print()
