Project Setup Instructions
Follow the steps below to set up the project:

1. Create a Virtual Environment: First, create a virtual environment for the project:

    python -m venv venv

2. Activate the Virtual Environment:

    source venv/bin/activate

3. Install Required Packages: Install the necessary packages listed in the requirements.txt file:

    pip install -r requirements.txt

4. Update Database Credentials: Replace the database credentials in the .env file with your own. Make sure the following fields are updated:

    DB_NAME
    DB_USER
    DB_PASSWORD
    DB_HOST
    DB_PORT
5. Make Migrations: Create database migrations and apply them:

    python manage.py makemigrations
    python manage.py migrate
6. Run the Development Server: Start the development server:

    python manage.py runserver
