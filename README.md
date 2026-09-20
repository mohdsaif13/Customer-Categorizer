# Customer Personality Categorization

### End-to-End Machine Learning Pipeline | Python | Scikit-learn | MongoDB | AWS S3 | Docker | Azure | GitHub Actions

> A practical machine-learning project for customer segmentation and cluster prediction, built with a modular training and prediction pipeline and cloud-oriented deployment components.

## 📌 Overview

This project takes customer profile and purchase data, prepares it for modeling, groups customers into behavioral segments, and uses a classification model to predict the resulting segment for new customer records.

The repository is organized as an end-to-end ML workflow rather than a single notebook: **data ingestion → validation → transformation → clustering → model training → evaluation → model storage → prediction**.

## 🧰 Technology Stack

| Area | Technologies |
|---|---|
| Language | Python |
| Data | Pandas, NumPy |
| Machine Learning | Scikit-learn, K-Means, Logistic Regression, GridSearchCV |
| Data Validation | Schema validation, Evidently data-drift profiling |
| Data Processing | Feature engineering, imputation, scaling, SMOTETomek |
| Database | MongoDB / MongoDB Atlas |
| Object Storage | AWS S3 |
| API / App | Flask, FastAPI, Jinja2 |
| Containerization | Docker |
| Cloud Deployment | Azure Web App Service |
| CI/CD | GitHub Actions |
| Configuration | YAML-based configuration |
| Engineering | Logging, custom exceptions, modular components |

## 🔄 Pipeline

### 1. Data Ingestion

Customer data is read from MongoDB and exported into the feature-store layer. The training pipeline then creates train/test datasets.

### 2. Data Validation

The validation layer checks the expected schema and compares train/test data for drift using Evidently profiling.

### 3. Data Transformation

Customer attributes are transformed into modeling features such as age, children, family size, spending and purchase-related variables. Missing values are handled and numerical features are prepared for modeling.

### 4. Customer Clustering

K-Means is used to create customer groups from the transformed behavioral features.

### 5. Model Training

Logistic Regression is trained to map customer features to the generated cluster labels. `GridSearchCV` is used for hyperparameter search.

### 6. Model Evaluation

The trained model is evaluated against the configured metric and accepted only when it meets the pipeline's comparison logic.

### 7. Model Pushing

Accepted model artifacts can be stored in AWS S3 through the repository's cloud-storage layer.

### 8. Prediction

The prediction pipeline converts incoming customer attributes into the configured schema, loads the trained estimator from the model store, and returns the predicted customer segment.

## 🗂️ Project Structure

```text
Customer-Categorizer/
├── config/                     # Schema and model configuration
├── docs/                       # Setup and architecture documentation
├── flowchart/                  # Pipeline diagrams
├── notebooks/                  # EDA / experimentation notebooks
├── src/
│   ├── cloud_storage/          # AWS S3 integration
│   ├── components/             # Ingestion, validation, transformation, ML
│   ├── configuration/          # AWS / MongoDB connections
│   ├── constant/               # Pipeline and application constants
│   ├── data_access/            # MongoDB data access
│   ├── entity/                 # Configuration and artifact objects
│   ├── exception/              # Custom exception handling
│   ├── logger/                 # Logging
│   ├── ml/                     # Estimators and metrics
│   ├── pipeline/               # Train and prediction pipelines
│   └── utils/                  # Shared utilities
├── static/                     # Application CSS
├── templates/                  # Application templates
├── app.py
├── Dockerfile
├── requirements.txt
└── setup.py
```

## ⚙️ Local Setup

### 1. Clone

```bash
git clone https://github.com/mohdsaif13/Customer-Categorizer.git
cd Customer-Categorizer
```

### 2. Create an environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure services

The pipeline expects the required database/cloud settings to be supplied through environment variables/configuration used by the application.

Typical services used by the repository include:

- MongoDB / MongoDB Atlas
- AWS S3
- Azure Web App Service

Do not commit credentials or secret keys.

## 🐳 Docker

Build the image:

```bash
docker build -t customer-categorizer .
```

Run it:

```bash
docker run -p 5000:5000 customer-categorizer
```

The exact application route depends on the configured Flask app entry point and environment.

## ☁️ CI/CD

The repository includes a GitHub Actions workflow that builds a Docker image, pushes it to Azure Container Registry, and deploys the image to Azure Web App Service using GitHub repository secrets.

## 📊 Modeling Notes

The repository's configuration currently defines:

- **K-Means** for customer clustering
- **Logistic Regression** for cluster prediction
- **GridSearchCV** for hyperparameter search

The feature pipeline also includes preprocessing, imputation, scaling and class-balancing utilities.

## 🔐 Engineering Practices

- YAML-based configuration keeps model and schema settings separate from application code.
- Custom logging and exception classes are used across pipeline components.
- Training and prediction are separated into independent pipelines.
- Model artifacts are represented explicitly and can be pushed to cloud storage.
- Docker and GitHub Actions make the deployment path reproducible.

## ⚠️ Notes

This repository is a portfolio/learning implementation of a production-style ML pipeline. Cloud services and credentials are environment-dependent, so the complete deployment path may require your own MongoDB, AWS and Azure configuration.

## 👤 Author

**Md Saif Ali**

Data Science | Machine Learning | AI/ML

[GitHub](https://github.com/mohdsaif13) · [LinkedIn](https://www.linkedin.com/in/md-saif-ali-a3250825b/)

---

### ⭐ Project focus

**Customer data → validation → feature engineering → clustering → classification → evaluation → cloud model storage → prediction**