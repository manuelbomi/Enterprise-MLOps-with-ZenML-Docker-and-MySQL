import logging
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from zenml import pipeline, step
from zenml.client import Client


# -----------------------------
#  Step 1 — Load and split data
# -----------------------------
@step
def training_data_loader() -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Loads and splits the Iris dataset."""
    logging.info(" Loading Iris dataset...")
    iris = load_iris(as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    logging.info(" Data successfully loaded and split.")
    return X_train, X_test, y_train, y_test


# -----------------------------
#  Step 2 — Train model
# -----------------------------
@step
def model_trainer(X_train: pd.DataFrame, y_train: pd.Series) -> LogisticRegression:
    """Trains a Logistic Regression model."""
    logging.info(" Training Logistic Regression model...")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    logging.info(" Model training complete.")
    return model


# -----------------------------
#  Step 3 — Evaluate model
# -----------------------------
@step
def model_evaluator(model: LogisticRegression, X_test: pd.DataFrame, y_test: pd.Series) -> float:
    """Evaluates the trained model."""
    logging.info(" Evaluating model performance...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    logging.info(f" Model accuracy: {accuracy:.4f}")
    return accuracy


# -----------------------------
#  ZenML Pipeline definition
# -----------------------------
@pipeline
def iris_training_pipeline():
    """ZenML pipeline for training and evaluating an Iris classifier."""
    X_train, X_test, y_train, y_test = training_data_loader()
    model = model_trainer(X_train=X_train, y_train=y_train)
    model_evaluator(model=model, X_test=X_test, y_test=y_test)


# -----------------------------
#  Run pipeline entrypoint
# -----------------------------
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    client = Client()
    logging.info(f" Connected to ZenML server: {client.zen_store.url}")
    logging.info(f"Active stack: {client.active_stack.name}")

    # Run pipeline on the server
    run_response = iris_training_pipeline()

    logging.info(" Iris training pipeline completed successfully!")
    logging.info(f" Pipeline Run ID: {run_response.id}")
    logging.info(f" Check the dashboard at: http://localhost:8080/runs/{run_response.id}")
