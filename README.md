Markdown
# Airflow Transaction Processing Pipeline 🚀

## Project Overview
This project is an automated ETL pipeline built for the **Digital Egypt Pioneers Initiative (DEPI)**. It simulates a transaction monitoring system that generates reports, logs processing timestamps, and sends automated email notifications using **Apache Airflow** and **Docker**.

## 🏗️ Architecture
The pipeline is orchestrated using a Directed Acyclic Graph (DAG) consisting of four main tasks:

1. **`pipeline_start_timestamp`**: (PythonOperator) Records the start time of the workflow.
2. **`trans_report`**: (PythonOperator) Aggregates transaction data and generates a local report.
3. **`run_process_transactions_script`**: (BashOperator) Executes a shell command to process the data and verify output.
4. **`Report_email`**: (EmailOperator) Sends the final transaction summary to a designated email address.

## 🛠️ Tech Stack
- **Orchestration:** Apache Airflow 2.x
- **Containerization:** Docker & Docker Compose
- **Language:** Python 3.x
- **Database:** PostgreSQL (Metadata storage)

## 🚀 Getting Started

### Prerequisites
- Docker Desktop installed
- WSL2 (for Windows users)

### Installation & Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/AhmedAlkaik/Airflow-Transaction-Project.git](https://github.com/AhmedAlkaik/Airflow-Transaction-Project.git)
Navigate to the project directory:

Bash
cd Airflow-Transaction-Project
Start the Airflow environment:

Bash
docker-compose -f airflow.yaml up -d
Access the Airflow UI at http://localhost:8089 (Login: admin / admin).

📁 Project Structure
dags/: Contains the main DAG definitions.

plugins/: Custom helper functions for data processing.

shared/: Shared volume for generated report files.

airflow.yaml: Docker Compose configuration for the full stack.

Developed by: Ahmed Hassan Ahmed

Industrial Engineering Student @ E-JUST | DEPI AI & Data Engineering Track