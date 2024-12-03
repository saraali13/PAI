import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("heart.csv")

X = df.drop(columns=["target"])
y = df["target"]

scaler = StandardScaler()
neighbors_range = range(1, 251)
seed_accuracies = {}
for seed in range(1, 11):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed, stratify=y)

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    accuracies = []

    for k in neighbors_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train_scaled, y_train)
        y_prediction = knn.predict(X_test_scaled)
        accuracies.append(accuracy_score(y_test, y_prediction))

    seed_accuracies[seed] = max(accuracies)

print("Accuracies for each random seed:")
for seed, accuracy in seed_accuracies.items():
    print(f"Seed {seed}: {accuracy:.2f}")

highest_seed = max(seed_accuracies, key=seed_accuracies.get)
lowest_seed = min(seed_accuracies, key=seed_accuracies.get)

print(f"\nHighest Accuracy: {seed_accuracies[highest_seed]:.2f} (Seed {highest_seed})")
print(f"Lowest Accuracy: {seed_accuracies[lowest_seed]:.2f} (Seed {lowest_seed})")
