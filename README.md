# 0x02. AirBnB clone - MySQL
** Group project Python OOP Back-end SQL MySQL ORM SQLAlchemy **

## Description

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

## Resources
- [cmd module] (https://docs.python.org/3/library/cmd.html)
- [unittest module] (https://docs.python.org/3/library/unittest.html#module-unittest)
- [args, kwargs] (https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [SQLAlchemy tutorial] (https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [How To Create a New User and Grant Permissions in MySQL] (https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [Python3 and environment variables] (https://docs.python.org/3/library/os.html?highlight=env#os.getenv)
- [SQLAlchemy] (https://docs.sqlalchemy.org/en/13/)
- [MySQL 8.0 SQL Statement Syntax] (https://docs.sqlalchemy.org/en/13/)


## Learning Objectives
### What is Unit testing and how to implement it in a large project
### What is *args and how to use it
### What is **kwargs and how to use it
### How to handle named arguments in a function
### How to create a MySQL database
### How to create a MySQL user and grant it privileges
### What ORM means
### How to map a Python Class to a MySQL table
### How to use environment variables
### How to handle 2 different storage engines with the same codebase


<img src="hbnb_step2.png" alt="">


## The Command Interpreter

The command interpreter provides a simple REPL (Read-Evaluate-Print-Loop) for interacting with the models in this project only. It can be used to test the functionality of the supported storage engines as well. You can find some examples of its usage [here](#examples).

### How To Use

1. First clone this repository.

2. Once the repository is cloned locate the "[console.py](console.py)" file and run it as follows:
   ```powershell
   ➜  AirBnB_clone_v2 git:(master) ✗ ./console.py
   ```

4. When this command is run the following prompt should appear:
   ```
   (hbnb)
   ```

5. This prompt designates that you are in the "HBnB" console. There are a variety of commands available within the console program.

### Supported Commands

These are commands that can be executed by the command interpreter. They have the format `command [argument]...` but you could also use the format `Model.command([argument]...)`, with the exception of the first 3 commands below.

| Format | Description |
|:-|:-|
| `help [command]` | Prints helpful information about a command (`command`). If `command` is not provided, it prints the help menu. |
| `quit` | Closes the command interpreter. |
| `EOF` | Closes the command interpreter. |
| `create Model [prop_key=prop_value]...` | Creates a new instance of the `Model` class with the given properties. `prop_value` can be a double-quoted string with double-quotes escaped and spaces replaced with underscores. `prop_value` can also be a float or integer. |
| `count Model` | Prints the number of instances of the `Model` class. |
| `show Model id` | Prints the string representation of an instance of the `Model` class with the given `id`. |
| `destroy Model id` | Deletes an instance of the `Model` class with the given `id`. |
| `all [Model]` | Prints a list containing the string representation of all instances of the `Model` class. `Model` is optional and if it isn't provided, all the availble objects are printed. |
| `update Model id attr_name attr_value` | Updates an instance of the `Model` class with the given `id` by assigning the attribute value `attr_value` to its attribute named `attr_name`. Attributes having the names `__class__`, `id`, `created_at`, and `updated_at` are silently ignored. |
| `update Model id dict_repr` | Updates an instance of `Model` having the given `id` by storing the key, value pairs in the given `dict_repr` dictionary as its attributes. The keys `__class__`, `id`, `created_at`, and `updated_at` are silently ignored. |
<br>

### Supported Models

These are the models that are currently available.

| Class | Description |
|:-|:-|
| BaseModel | A(n abstract) class that represents the base class for all models (all models are instances of this class). |
| User | Represents a user account. |
| State | Represents the geographical state in which a _User_ lives or a _City_ belongs to. |
| City | Represents an urban area in a _State_. |
| Amenity | Represents a useful feature of a _Place_. |
| Place | Represents a building containing rooms that can be rented by a _User_. |
| Review | Represents a review of a _Place_. |

### Environment Variables

+ `HBNB_ENV`: The running environment. It can be `dev` or `test`.
+ `HBNB_MYSQL_USER`: The MySQL server username.
+ `HBNB_MYSQL_PWD`: The MySQL server password.
+ `HBNB_MYSQL_HOST`: The MySQL server hostname.
+ `HBNB_MYSQL_DB`: The MySQL server database name.
+ `HBNB_TYPE_STORAGE`: The type of storage used. It can be `file` (using `FileStorage`) or `db` (using `DBStorage`).
