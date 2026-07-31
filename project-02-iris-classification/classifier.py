# classifier.py
# Project 2: Iris Classification using KNN
# Follows Input -> Process -> Output pipeline

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, f1_score


def load_data():
    # Load the built-in Iris dataset
    # X = features (sepal/petal length and width), y = target (flower class)
    data = load_iris()
    return data.data, data.target


def prepare_data(X, y, test_size=0.2, random_state=42):
    # Split into train and test sets
    # random_state makes the split reproducible for testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=True
    )

    # Scale features so all have mean=0, variance=1
    # KNN uses distance, so unscaled features would bias the result
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test


def train_model(X_train, y_train, n_neighbors=5):
    # Create and train a KNN classifier
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    # Predict on test data and check how well the model did
    predictions = model.predict(X_test)

    matrix = confusion_matrix(y_test, predictions)
    f1 = f1_score(y_test, predictions, average="weighted")

    return matrix, f1


def main():
    X, y = load_data()
    X_train, X_test, y_train, y_test = prepare_data(X, y)

    model = train_model(X_train, y_train)
    matrix, f1 = evaluate_model(model, X_test, y_test)

    print("Confusion Matrix:")
    print(matrix)
    print(f"\nF1 Score: {f1:.4f}")


if __name__ == "__main__":
    main()