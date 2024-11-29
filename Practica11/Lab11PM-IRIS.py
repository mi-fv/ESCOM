import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score, LeaveOneOut
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración general
np.random.seed(42)

# Cargar dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# Hold-Out (70/30)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Perceptrón Multicapa
mlp = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000, random_state=42)
mlp.fit(X_train, y_train)

# Evaluación con Hold-Out
y_pred = mlp.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Hold-Out Accuracy (MLP):", accuracy)

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred)
print("Matriz de confusión (MLP):\n", cm)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Matriz de Confusión (MLP)")
plt.xlabel("Predicción")
plt.ylabel("Actual")
plt.show()

# 10-Fold Cross-Validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(mlp, X, y, cv=10)
print("10-Fold Cross-Validation Accuracy (MLP):", scores.mean())

# Leave-One-Out


loo = LeaveOneOut()
scores_loo = cross_val_score(mlp, X, y, cv=loo)
print("Leave-One-Out Accuracy (MLP):", scores_loo.mean())
