import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

wine = datasets.load_wine()
X = wine.data[:, [9, 12]]
# X = wine.data

sc = StandardScaler()
X_std = sc.fit_transform(X)

model2 = KMeans(n_clusters=2, random_state=103)
model3 = KMeans(n_clusters=3, random_state=103)
model4 = KMeans(n_clusters=4, random_state=103)

model2.fit(X_std)
model3.fit(X_std)
model4.fit(X_std)

plt.figure(figsize=(8, 12))

plt.subplot(3, 1, 1)
plt.scatter(X_std[:, 0], X_std[:, 1], c=model2.labels_)
plt.scatter(model2.cluster_centers_[:, 0], model2.cluster_centers_[:, 1], s=250, marker="*", c="red")
plt.title("K-means(n_clusters=2)")

plt.subplot(3, 1, 2)
plt.scatter(X_std[:, 0], X_std[:, 1], c=model3.labels_)
plt.scatter(model3.cluster_centers_[:, 0], model3.cluster_centers_[:, 1], s=250, marker="*", c="red")
plt.title("K-means(n_clusters=3)")

plt.subplot(3, 1, 3)
plt.scatter(X_std[:, 0], X_std[:, 1], c=model4.labels_)
plt.scatter(model4.cluster_centers_[:, 0], model4.cluster_centers_[:, 1], s=250, marker="*", c="red")
plt.title("K-means(n_clusters=4)")

plt.show()
