import mlflow
if __name__ == "__main__":
    with mlflow.start_run():
        mlflow.log_artifact("artifact.png")
