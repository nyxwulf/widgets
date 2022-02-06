# widgets
Widgets API

Simple python rest api
Requires sqlite3, python 3.8, and make.

## Running the api
1. Run the server with sample data
```sh
make run
```
2. Build the database
```sh
make clean
make db
```

or if sample data is desired
```sh
make clean
make sample
```

## Python virtual environment
The server is built and tested on python 3.8.12.  To ensure version compatibility this document will walk through the steps to create an anaconda environment with the same version of python, and then activate the python virtual environment for this project.

1. Follow the instructions on the [Anaconda](https://www.anaconda.com/products/individual "Anaconda Website") site for getting anaconda installed.
2. Create a python 3.8 environment, then activate
  ```sh
  conda create -y --name py38 python=3.8.12
  conda activate py38
  ```

  Deactivate when finished
  ```sh
  conda deactivate
  ```
3. Create project virual environment

  First create the environment from the root of the project, activate and install the requirements
  ```sh
  python -m venv venv
  . venv/bin/activate
  pip install -r requirements.txt
  ```





## Database Structure
| Column Name | Type        | Description                                        |
| ----------- | ----        | -----------                                        |
| widget_id   | int         | Auto increment primary key                         |
| code        | varchar(26) | Unique code for this item (e.g. sku)               |
| name        | varchar(64) | Part name, limited to 64 characters                |
| num_parts   | integer     | Number of parts for this item                      |
| created_at  | int(4)      | Database timestamp for when the record was created |
| updated_at  | int(4) NULL | Null by default, updated via the UPDATE_WIDGET_TRIGGER when the record is modified |

