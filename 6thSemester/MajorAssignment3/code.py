# 1. Import libraries
import numpy as np
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
from tensorflow.keras.datasets import fashion_mnist # type: ignore
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train = x_train / 255.0
x_test = x_test / 255.0
x_train = x_train.reshape(-1, 28 * 28)
x_test = x_test.reshape(-1, 28 * 28)


x_train_small = x_train[:10000]
y_train_small = y_train[:10000]
x_test_small = x_test[:2000]
y_test_small = y_test[:2000]

# 2. KNN Classification 
print("KNN Accuracy:")
for k in [3, 5, 7]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train_small, y_train_small)
    acc = accuracy_score(y_test_small, knn.predict(x_test_small))
    print(f"K = {k}, Accuracy = {acc:.4f}")

# 3. SVM Classification 
print("\nSVM Accuracy:")
svm_linear = LinearSVC(C=1, max_iter=10000)
svm_linear.fit(x_train_small, y_train_small)
acc_linear = accuracy_score(y_test_small, svm_linear.predict(x_test_small))
print(f"SVM Kernel = linear, C = 1, Accuracy = {acc_linear:.4f}")

svm_linear = LinearSVC(C=10, max_iter=10000)
svm_linear.fit(x_train_small, y_train_small)
acc_linear = accuracy_score(y_test_small, svm_linear.predict(x_test_small))
print(f"SVM Kernel = linear, C = 10, Accuracy = {acc_linear:.4f}")

for C in [1, 10]:
    svm_rbf = SVC(kernel='rbf', C=C)
    svm_rbf.fit(x_train_small, y_train_small)
    acc_rbf = accuracy_score(y_test_small, svm_rbf.predict(x_test_small))
    print(f"SVM Kernel = rbf, C = {C}, Accuracy = {acc_rbf:.4f}")

# 4. t-SNE Visualization 
sample_size = 1000  
pca = PCA(n_components=50)
x_pca = pca.fit_transform(x_train[:sample_size])

tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=500)
x_embedded = tsne.fit_transform(x_pca)

plt.figure(figsize=(8, 6))
scatter = plt.scatter(x_embedded[:, 0], x_embedded[:, 1], c=y_train[:sample_size], cmap='tab10', s=15)
plt.title("t-SNE on PCA-reduced Fashion MNIST")
plt.colorbar(scatter)
plt.show()

# 5. Evaluation and Confusion Matrix
knn_best = KNeighborsClassifier(n_neighbors=5).fit(x_train_small, y_train_small)
svm_best = SVC(kernel='rbf', C=10).fit(x_train_small, y_train_small)
y_knn = knn_best.predict(x_test_small)
y_svm = svm_best.predict(x_test_small)

print("\nKNN Report:\n", classification_report(y_test_small, y_knn))
print("\nSVM Report:\n", classification_report(y_test_small, y_svm))

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.heatmap(confusion_matrix(y_test_small, y_knn), annot=True, fmt='d', cmap="Blues")
plt.title("KNN Confusion Matrix")

plt.subplot(1, 2, 2)
sns.heatmap(confusion_matrix(y_test_small, y_svm), annot=True, fmt='d', cmap="Greens")
plt.title("SVM Confusion Matrix")

plt.show()
 # type: ignore