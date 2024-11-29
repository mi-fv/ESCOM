# Archivo: rbf_digits.py
from sklearn.datasets import load_digits
from sklearn.utils import resample
from sklearn.kernel_approximation import RBFSampler
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split, cross_val_score, LeaveOneOut
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset Digits y reducir a 500 muestras
digits = load_digits()
X, y = digits.data, digits.target
X, y = resample(X, y, n_samples=500, random_state=42)  # Reducir a 500 muestras

# Hold-Out (70/30)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Red Neuronal RBF
rbf_feature = RBFSampler(gamma=1, random_state=42)
X_train_rbf = rbf_feature.fit_transform(X_train)
X_test_rbf = rbf_feature.transform(X_test)

clf_rbf = SGDClassifier(random_state=42)
clf_rbf.fit(X_train_rbf, y_train)

# Evaluación Hold-Out
y_pred = clf_rbf.predict(X_test_rbf)
accuracy = accuracy_score(y_test, y_pred)
print("Hold-Out Accuracy (Digits RBF):", accuracy)

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred)
print("Matriz de Confusión (Digits RBF):\n", cm)

# Graficar la matriz de confusión
sns.heatmap(cm, annot=True, fmt='d', cmap='Oranges')
plt.title("Matriz de Confusión (Digits RBF)")
plt.xlabel("Predicción")
plt.ylabel("Actual")
plt.show()

# 10-Fold Cross-Validation
X_rbf = rbf_feature.fit_transform(X)
scores = cross_val_score(clf_rbf, X_rbf, y, cv=10)
print("10-Fold Cross-Validation Accuracy (Digits RBF):", scores.mean())

# Leave-One-Out
loo = LeaveOneOut()
scores_loo = cross_val_score(clf_rbf, X_rbf, y, cv=loo)
print("Leave-One-Out Accuracy (Digits RBF):", scores_loo.mean())
