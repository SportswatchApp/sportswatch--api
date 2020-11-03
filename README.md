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

### Sample data
Run `$ python manage.py makesampledata` before running the server, to set initial sample data


### Create new usecase
Command `python manage.py usecase use-case-type use-case-name [--request]`

The command creates a new use case. 

* `use-case-type` should be camel case ex. `Login`, `Create`, `Edit`, etc.
* `use-case-name` should be lowercase with underscores ex. `login_member`, `create_new_user`, `edit_club`, etc
* The `--request` is optional and should be added if the usecase requires data in a request


### Documentation
Endpoints: https://documenter.getpostman.com/view/11478271/TVYM5GDd#055e00ab-f034-4096-80ef-7b5d3cc2ad34
