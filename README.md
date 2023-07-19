# A demo for Python and SQL


## Alembic setup

- add the connection string to the alembic.ini file
- edit the env.py file to add the models to the target_metadata variable

```
alembic init alembic
alembic revision --autogenerate -m "create tables"
alembic upgrade head
```
