# Enterprise MLOps with ZenML, Docker, and MySQL <sub>(End-to-End Machine Learning Pipeline for the Iris Dataset)</sub>



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

--- 

## Step-by-Step Setup and Run Guide

### 1. Clone the Repository
 
```python
git clone https://github.com/manuelbomi/Enterprise-MLOps-with-ZenML-Docker-and-MySQL.git
cd zenml_mlops_docker_mysql

```


### 2. Build and Start the Docker Containers
```python
docker compose up --build
```

#### This spins up:

- A ZenML server on port 8080

- A MySQL database on port 3306

- Your app container with all dependencies installed


### 3. Enter the Application Container

```python
docker compose exec app bash
```

<img width="1280" height="720" alt="Image" src="https://github.com/user-attachments/assets/ddb5d028-209d-4a89-9b5e-eefd2977b8b7" />


<img width="1280" height="720" alt="Image" src="https://github.com/user-attachments/assets/52f521a0-c376-462f-b29c-a21a4a58ce4a" />




### 4. Log in to ZenML Server

```python
zenml login http://zenml-server:8080
```

---


<img width="1280" height="720" alt="Image" src="https://github.com/user-attachments/assets/10d57e78-256c-43f3-a565-57d9e9c6b8f7" />


> [!NOTE]
> If the browser link shows something like:
>
> *http://zenml-server:8080/devices/verify?device_id=...*
>
> replace zenml-server with localhost, like so:
>
> *http://localhost:8080/devices/verify?device_id=...*

#### Once authenticated, you will  see:

```python
Successfully logged in to http://zenml-server:8080.

```

### 5. Check ZenML Status

```python
zenml status
```

#### Expected output:
```python
Connected to a remote ZenML server: http://zenml-server:8080
Server status: available
Active user: default
Active stack: default
```


<img width="1280" height="720" alt="Image" src="https://github.com/user-attachments/assets/522eba9b-9867-4563-8377-7b0c5df44960" />


<img width="1280" height="720" alt="Image" src="https://github.com/user-attachments/assets/c4f6bcab-9141-4640-b6b9-9deb2190f016" />

### 6. (Optional) Register a Local Stack

#### If ZenML complains about missing stacks, re-register one:

```python
zenml stack register local_server_stack \
    -o default \
    -a default
zenml stack set local_server_stack
```

### 7. Run the Pipeline
```python
python src/pipeline.py
```

#### You will see logs similar to:

```python
Connected to ZenML server: http://zenml-server:8080
Active stack: default
Model accuracy: 1.0000
Pipeline run finished successfully!


```


### 8. View Pipeline Runs in the Dashboard

#### Open:

```python
http://localhost:8080
```

#### You will see the iris_training_pipeline run logged, with all steps, artifacts, and metrics.


<img width="1280" height="720" alt="Image" src="https://github.com/user-attachments/assets/f13a6079-d3e4-463d-95ed-4d6f1827f001" />


<img width="1280" height="720" alt="Image" src="https://github.com/user-attachments/assets/ff3b6904-d9d3-4e12-aea9-29fa1b3a7826" />



















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

