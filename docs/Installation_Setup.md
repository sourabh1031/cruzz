## Server Installation setup:

Authored by: [Monal Shadi](https://github.com/Monal5031)

Initial setup:

1. Install python3.6
    ```bash
       sudo apt-get install python3.6
    ```

2. Fork and then clone repo
    ```bash
       git clone <forked-repo-link>.git
    ```

3. Install virtual environment
    ```bash
       sudo apt-get install virtualenv
    ```

4. Create python3.6 virtualenv
    ```bash
       virtualenv -p python3.6 venv
    ```

5. Activate virtual environment
   ```bash
      source venv/bin/activate
   ```

6. Install requirements
    ```bash
       pip install -r requirements.txt 
    ```
    
Note: before installing requirements make sure your pip is upto date

If not then upgrade it by the following command and make sure to do this inside virtual environment

    ```bash
       pip install --upgrade pip
    ```

Project Databse Setup:

1. Install psql (PostgreSQL) (v9.5.12^ or later)

2. Login to postgres
    ```bash
       sudo su - postgres
    ```
    It will ask for your root password.

3. Login to psql
    ```bash
       psql
    ```
    It will ask for your psql password.

4. Create database
    ```bash
       create database cruzz;
    ```

5. Create DB user
    ```bash
       create user cruzz with password 'cruzz12345';
    ```

6. Grant permissions to user
    ```bash
       grant all on database cruzz to cruzz;
    ```


Migrate database and runserver

:Note: Migration files are already included in the repo so no need to create migrations.

1. First activate virtualenv
    ```bash
       source venv/bin/activate
    ```

2. Migrate database
    ```bash
       python manage.py migrate
    ```

3. Runserver
    ```bash
       python manage.py runserver
    ```


To test things out, go through the URL endpoints in [API_Testing_docs](API_Docs.md) at API_Docs.

You can use `Postman` or similar services for testing endpoints.
