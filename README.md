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

<img width="1280" height="720" alt="Image" src="https://github.com/user-attachments/assets/ff3b6904-d9d3-4e12-aea9-29fa1b3a7826" />


<img width="1280" height="720" alt="Image" src="https://github.com/user-attachments/assets/f13a6079-d3e4-463d-95ed-4d6f1827f001" />


### Troubleshooting Guide

| Issue | Fix |
|-------|-----|
| Browser can’t open zenml-server | Replace with localhost in the URL. |
| Pipeline fails to connect to server | Ensure ZenML version in container matches server (`zenml==0.71.0`). |
| Version mismatch warning | Delete `.zen` and reinitialize with `zenml init`. |
| Slow data materialization | Install PyArrow: `pip install pyarrow`. |
| MySQL connection errors | Ensure zenml-db is healthy: `docker ps` → check container logs. |


### Possible Enhancements

- Add model artifact registration (zenml.model_registry)

- Add experiment tracking with MLflow

- Deploy model via ZenML deployment stack

- Extend to use Dask / Ray orchestrators for distributed training

---
---


## Why This Project Matters for Enterprise & MLOps


#### This project is not just about “running an ML model.”

#### It is essentailly a modular, containerized, and trackable ML pipeline — exactly what enterprise teams need to move machine learning from research notebooks to production.

#### Let us break it down by MLOps capabilities and enterprise impact


### <ins>1. Reproducibility via Docker</ins>

- Same code, same environment, anywhere.

#### Why enterprises care:

#### Different engineers, OSes, or cloud environments can produce inconsistent results.

#### Docker ensures your ML pipeline, dependencies, and configurations are identical across:

- Local dev

- CI/CD runners

- Cloud deployments (AWS ECS, GCP, Azure Container Apps)
- 

#### The  project feature:


- The entire ZenML stack and pipeline run from a Docker container.

- Any engineer can reproduce results with:

```python
docker compose up --build
```

---


### <ins>2. Modular ML Pipelines with ZenML</ins>

#### A single source of truth for your ML workflow.

#### Why enterprises care:

##### ML projects often turn into spaghetti code — data cleaning, training, and evaluation all jumbled.

##### ZenML enforces clean separation between pipeline stages:

- load_data → train_model → evaluate_model

- Each step can be independently tested, versioned, and replaced (e.g., swap logistic regression for XGBoost).

##### The  project feature:

- Uses ZenML’s @step and @pipeline decorators to define a DAG-like ML workflow.

- Each step produces trackable artifacts stored in the artifact store.
  

---


### <ins> 3. Experiment Tracking & Auditability</ins>

##### Know what model, data, and parameters produced every result.

##### Why enterprises care:

##### In regulated industries (finance, healthcare, insurance), reproducibility and auditing are required.

##### ZenML tracks:

- Code version

- Parameters

- Datasets

- Model files

- Accuracy metrics

##### The  project feature:

- Every pipeline run is stored and versioned in ZenML’s database.

- MLOps Engineers and other Devs can visually inspect results in the ZenML dashboard at:
  

```python
http://localhost:8080
```


---


### <ins>4. Centralized Metadata via MySQL</ins>

#### One database for all experiment and pipeline metadata.

##### Why enterprises care:

##### Data scientists, ML engineers, and DevOps need shared visibility.

##### A central SQL database makes metadata accessible for:

- Dashboards (Grafana, Superset)

- Auditing tools

- Internal MLOps analytics

##### The  project feature:

- Uses MySQL as ZenML’s metadata store (instead of the default SQLite).

- Enables multi-user access and scalability.
  

---


### <ins>5. Orchestrated ML Lifecycle</ins>

##### From raw data → trained model → evaluated metrics.

##### Why enterprises care:

##### A typical ML lifecycle includes:

- Data ingestion & validation

- Feature engineering

- Model training

- Evaluation

- Model deployment

- Monitoring and retraining

####  The project feature:

- Implements the first three (load, train, evaluate).

- It is structured to easily extend:

- Add a deployment step (e.g., to FastAPI, MLflow, or Seldon)

- Add a data validation step (e.g., Great Expectations)

- Integrate a CI/CD trigger (e.g., GitHub Actions)
  

---


### <ins>6. Scalability and Cloud Readiness</ins>

##### Your team may decide to deploy the same stack on Kubernetes, AWS, or GCP.

##### Why enterprises care:

##### Companies often start local, but scale pipelines in the cloud.

##### ZenML integrates with:

- Kubeflow, Airflow, or Prefect (for orchestration)

- S3, GCS, Azure Blob (for artifact stores)

- MLflow or Weights & Biases (for experiment tracking)


##### The project feature:

- Built using ZenML’s pluggable stack concept.

- You can swap out local components for cloud ones — no code rewrite needed.

<ins>Example</ins>:

```python
zenml stack register aws_stack \
    -o kubeflow_orchestrator \
    -a s3_artifact_store \
    -m mlflow_experiment_tracker
zenml stack set aws_stack
```

---  

### <ins>7. Security and Multi-User Access</ins>

##### Supports user authentication and team collaboration.

##### Why enterprises care:

- Enterprise environments require controlled access.

- ZenML supports user authentication, API tokens, and RBAC (role-based access).

##### The project feature:

- Authenticates users via the ZenML web login flow.
- 
-  Demonstrates replacing zenml-server → localhost for network bridging between host and container.

---

### <ins> 8. Business Impact Summary </ins>

| Business Need | How This Project Solves It |
|---------------|----------------------------|
| Model reproducibility | Docker-based environment ensures consistent builds |
| Pipeline governance | ZenML tracks artifacts, runs, and metrics |
| Multi-user collaboration | MySQL-backed server allows shared metadata |
| Experiment management | Dashboard provides run comparisons |
| Easy deployment | Docker Compose encapsulates all services |
| Scalability | ZenML's stack concept enables cloud migration |
| Security | Server authentication and credential isolation |

---

### <ins> 9. Real-World Enterprise Use Cases</ins>

| Industry | Application Example |
|----------|---------------------|
| 🏦 Finance | Credit risk scoring pipeline using ZenML orchestrator |
| 🏥 Healthcare | Predictive patient diagnosis with auditable ML runs |
| 🚚 Logistics | IoT data analytics using ZenML with Dask backend |
| 🏭 Manufacturing | Predictive maintenance models tracked via ZenML |
| 💳 Retail | Customer churn prediction pipelines |

---

### <ins> 10. MLOps Principles Demonstrated </ins>

| MLOps Pillar | How This Project Demonstrates It |
|--------------|----------------------------------|
| Automation | Pipelines defined declaratively in ZenML |
| Reproducibility | Docker ensures same environment everywhere |
| Versioning | Runs, data, and models tracked via ZenML |
| Scalability | Pluggable architecture enables cloud scaling |
| Monitoring | Metrics logged and visualized in dashboard |
| Collaboration | Central server + database for team access |

--- 
















