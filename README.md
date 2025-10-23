# Enterprise MLOps with ZenML, Docker, and MySQL (End-to-End Machine Learning Pipeline for the Iris Dataset)

## Project Overview

#### This project demonstrates an end-to-end MLOps workflow using:

- Docker for reproducible environments

- ZenML for pipeline orchestration and experiment tracking

-  MySQL as ZenML’s metadata store

- Scikit-learn for model training and evaluation

- Pandas for data handling

---

### Project Structure

```python
zenml_demo_project/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
├── README.md
└── app/
    ├── .zen/                     # ZenML local repo configuration (auto-created)
    ├── src/
    │   └── pipeline.py           # ZenML pipeline definition and entrypoint
    │
    ├── Dockerfile
    ├── requirements.txt
    ├── run_pipeline.sh
 ├── .gitignore
 ├── Makefile



```

The project trains and evaluates a Logistic Regression model on the classic Iris dataset, all orchestrated and tracked via ZenML running in a containerized setup.

**Important notes**
* The ZenML server container image used: `zenmldocker/zenml-server:0.71.0`. See ZenML docs for deploying with Docker. (Docs: https://docs.zenml.io/deploying-zenml/deploy-with-docker). citeturn0search0
* After `docker compose up --build` the `zenml-server` and `mysql` services will be started. You can open the ZenML dashboard at `http://localhost:8080`.
* To execute and track pipelines you must create a ZenML service account / API key and login the ZenML client (instructions below). Docs on connecting a client to a server & using service accounts: https://docs.zenml.io/deploying-zenml/connecting-to-zenml/connect-with-a-service-account. citeturn1search3

## Quick start (recommended)
1. From the project folder run:
   ```bash
   make up
   ```
   This will build the app image and start the `mysql` and `zenml-server` containers.

2. Wait a minute for MySQL & ZenML server to initialize, then open the ZenML dashboard at:
   ```
   http://localhost:8080
   ```

3. Open a shell in the `app` container:
   ```bash
   make shell
   ```

4. Inside the `app` container:
   * Install the Python requirements (already baked into the image, but you can re-run):
     ```
     pip install -r /workspace/app/requirements.txt
     ```
   * Create a service account and API key (this will print the API key):
     ```
     make create-service-account
     ```
     Copy the API key value (you will need it once).
   * Login with the API key (replace the URL & API key / examples below):
     ```
     zenml login http://zenml-server:8000 --api-key <YOUR_API_KEY>
     ```
     Or set environment variables:
     ```
     export ZENML_STORE_URL=http://zenml-server:8000
     export ZENML_STORE_API_KEY=<YOUR_API_KEY>
     ```

5. Run the pipeline:
   ```
   make run
   ```
   The pipeline will run and you will see metadata and run entries in the ZenML dashboard.

## Files
* `docker-compose.yml` - docker compose setup for MySQL, ZenML server, and the app.
* `app/` - application image that contains a small sklearn pipeline and helper scripts.

## Production considerations
* For production use, follow ZenML's production deployment guide and secure your server (TLS, database backups, API key management, etc.). See ZenML docs on "Using ZenML server in production". citeturn0search4

