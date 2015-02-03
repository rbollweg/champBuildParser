# champBuildParser
a wep app to parse champion builds from a riot match history page
Written in Python 3.4
  
-------------------------------------------------------------------
--Installation (Assuming Python 3.4 is installed and in your PATH)

-from cmdline
pip install flask

pip install flask-sqlalchemy

pip install sqlalchemy-migrate

pip install flask-wtf

This includes a blank database file, to generate your own:

-run db_create.py
-run db_migrate.py



and finally, to run:

-run run.py

should now be running on localhost http://127.0.0.1:5000/

