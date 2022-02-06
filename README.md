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

## Database Structure
| Column Name | Type        | Description                                        |
| ----------- | ----        | -----------                                        |
| widget_id   | int         | Auto increment primary key                         |
| code        | varchar(26) | Unique code for this item (e.g. sku)               |
| name        | varchar(64) | Part name, limited to 64 characters                |
| num_parts   | integer     | Number of parts for this item                      |
| created_at  | int(4)      | Database timestamp for when the record was created |
| updated_at  | int(4) NULL | Null by default, updated via the UPDATE_WIDGET_TRIGGER when the record is modified |

