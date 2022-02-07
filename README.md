# widgets
Widgets API

Simple python rest api
Requires sqlite3, python 3.8, and make.

## Prerequisites
1. Setup python 3.8 environment, for example, using Anaconda:
```sh
conda create -y --name py38 python=3.8.12
conda activate py38
```
when finished:
```sh
conda deactivate
```
2. Create project virtual environment
```sh
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

All other instructions assume an activated virtual environment with installed requirements.

## Running the api
1. Run the server with sample data
```sh
make clean
make sample
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

## Documentation
With the server running navigate to: [Swagger Documentation](http://127.0.0.1:8000/docs)
or [ReDoc Documentation](http://127.0.0.1:8000/redoc)

## Running the tests
```sh
pytest
```

## Database Structure
| Column Name | Type         | Description                                                                        |
| ----------- | ----         | -----------                                                                        |
| widget_id   | int          | Auto increment primary key                                                         |
| name        | varchar(64)  | Part name, limited to 64 characters                                                |
| description | varchar(256) | Part Description, limited to 256 characters                                        |
| num_parts   | integer      | Number of parts for this item                                                      |
| created_at  | int(4)       | Database timestamp for when the record was created                                 |
| updated_at  | int(4) NULL  | Null by default, updated via the UPDATE_WIDGET_TRIGGER when the record is modified |

