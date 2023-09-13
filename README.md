👋 Hello!

# Airflow Project 🚀

This project demonstrates how to use Apache Airflow to orchestrate workflows within a Docker environment. It provides a Dockerized setup using docker-compose for easy deployment and management of the Airflow services. This project downloads New York yellow taxi data and loads it into database. You can then run various queries against this analytics database.

## Requirements

Before getting started with the project, make sure you have the following components installed:

- [Docker](https://www.docker.com/get-started)
- [docker-compose](https://docs.docker.com/compose/install/)

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/fridaytmn/airflow_project.git
   cd airflow_project
   ```

    Create a `.env` file and write data there
    `
    PG_USER=***
    PG_PASS=***
    PG_DB=***
    PG_PORT=***
    `

    Run
    ```
    echo -e "AIRFLOW_UID=$(id -u)" >> .env
    ```

2. Build the Docker image:
   ```
   docker-compose build
   ```

3. Start the Docker containers:
   ```
   docker-compose up -d
   ```

   This command will start the Airflow services defined in the `docker-compose.yml` file in detached mode.

4. Access the Airflow UI:
   Open a web browser and go to [http://localhost:8080](http://localhost:8080) to access the Airflow UI.

## Customization

You can customize the Airflow configuration and workflows according to your requirements. Below are the key files and directories that you may want to modify:

- `docker-compose.yml`: Defines the Docker services for Airflow and other dependencies.
- `dags/`: Contains the Airflow DAGs (workflows) that you can create or modify.

Feel free to explore the project structure and modify it as per your needs.