# Payment Request Management Application

This application is designed for managing and processing payment requests. It provides functionality for creating and tracking payment requests.

## Running the Application

To run the application, follow these steps:

1. Navigate to the project directory:
    ```bash
    cd ozp
    ```
2. Run the application with the following command:
    ```bash
    python -m app.app
    ```

## Setting Up the Database

To set up the database, follow these steps:

1. Navigate to the `database` directory:
    ```bash
    cd database
    ```
2. Run the `create_db.py` script to create the database:
    ```bash
    python create_db.py
    ```
3. Populate the database with initial data by running the `population_db.py` script:
    ```bash
    python population_db.py
    ```