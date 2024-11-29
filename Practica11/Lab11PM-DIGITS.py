# Archivo: mlp_digits.py
from sklearn.datasets import load_digits
from sklearn.utils import resample
from sklearn.model_selection import train_test_split, cross_val_score, LeaveOneOut
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset Digits y reducir a 500 muestras
digits = load_digits()
X, y = digits.data, digits.target
X, y = resample(X, y, n_samples=500, random_state=42)  # Reducir a 500 muestras

# Hold-Out (70/30)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Perceptrón Multicapa
mlp = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000, random_state=42)
mlp.fit(X_train, y_train)

# Evaluación Hold-Out
y_pred = mlp.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Hold-Out Accuracy (Digits):", accuracy)

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred)
print("Matriz de Confusión (Digits):\n", cm)  # Imprimir en consola

# Graficar la matriz de confusión
sns.heatmap(cm, annot=True, fmt='d', cmap='Oranges')
plt.title("Matriz de Confusión (Digits)")
plt.xlabel("Predicción")
plt.ylabel("Actual")
plt.show()

# 10-Fold Cross-Validation
scores = cross_val_score(mlp, X, y, cv=10)
print("10-Fold Cross-Validation Accuracy (Digits):", scores.mean())

# Leave-One-Out
loo = LeaveOneOut()
scores_loo = cross_val_score(mlp, X, y, cv=loo)
print("Leave-One-Out Accuracy (Digits):", scores_loo.mean())
