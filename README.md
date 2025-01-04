**DEACERO**

Run the following command to apply the pending migrations:
alembic upgrade head

This command will apply all the pending migrations to bring the database schema up to date. After successfully applying the migrations, you can then create a new revision using:

alembic revision --autogenerate