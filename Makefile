db_name = widgets.db

.PHONY: clean

sample : db
	cat sample_items.sql | sqlite3 $(db_name)

db : $(db_name)

$(db_name):
	cat schema.sql | sqlite3 $(db_name)

clean:
	rm $(db_name)

