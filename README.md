# Sportswatch API
API back-end for sportswatch

### Requirements
* Python 3.8

### Project setup
1. Clone the `develop` branch
2. Setup a virtual environment `venv` in project root with pip installed
  - `$ python -m venv /path/to/root/venv`
3. Run `$ pip install -r requirements.txt`
4. Run `$ python manage.py migrate` to migrate tables to the database. This will create a file `db.sqlite3` which is the database.

To run the API: `$ python manage.py runserver`. Will typically be served on 127.0.0.1:8000
