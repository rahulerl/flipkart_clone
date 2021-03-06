# flipkart_clone


**Prerequisites:**

  1. Python 3

  2. Flask

  3. Virtualenv

   

**Database Setup:**

   Flask has support for several relational database management systems, including SQLite, 

   MySQL, and PostgreSQL. We will be using MySQL.

   **We will install the following:**

       1. **Flask-SQLAlchemy:** This will allow us to use SQLAlchemy, a useful tool for SQL use with  

             Python. SQLAlchemy is an Object Relational Mapper (ORM), which means that it connects

             the objects of an application to tables in a relational database management system. These

             objects can be stored in the database and accessed without the need to write raw SQL.

      2. **MySQL-Python:** This is a Python interface to MySQL. It will help us connect the MySQL 

          database to the app.

          **$ pip install flask-sqlalchemy mysql-python**

**Migration:**

    Migrations allow us to manage changes we make to the models, and propagate these changes in

    the database. For example, if later on we make a change to a field in one of the models, all we will

    need to do is create and apply a migration, and the database will reflect the change.

      **$ pip install flask-migrate**

      **$ flask db init**

      **$ flask db migrate**

      **$ flask db upgrade**

**Run the server:**

    $ export FLASK_CONFIG=development

    $ export FLASK_APP=server.py

    $ flask run
