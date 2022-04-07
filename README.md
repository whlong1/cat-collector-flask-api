# cat-collector-flask-api

![banner](https://i.imgur.com/juxPY8i.png)

## Getting Started

Fork and clone this repository.

Create a new virtual environment. The dependencies involved in this configuration of Flask are a bit different, so we’ll want a fresh start with this environment. 

```bash
conda create -n cat_collector python=3.9
```

Next, activate your virtual environment with the command below. 

```bash
conda activate cat_collector
```

Once the environment is active, run the following command in your terminal.

```bash
pip3 install -r requirements.txt 
```

In your terminal, run the following command to create a **`.env`** in the base directory of your project.

```bash
touch .env
```

Add an **`APP_SECRET`** variable to your **`.env`** file.

```
APP_SECRET=supersecretkey
```

In the base directory of your project, you should see a file called `**config.py**`. Update the line below with the name of our project’s database.

```python
SQLALCHEMY_DATABASE_URI = "postgresql://localhost:5432/cat_collector_api"
```

After updating `**config.py**`, run the following commands in your terminal. Make sure the name of your database does not already exist. 

```bash
createdb cat_collector_api
flask db init
flask db migrate
flask db upgrade
```

Run the following command to start your application. 

```bash
python3 app.py
```

## Checking Our Database

We can verify that our initial migrations have gone through by jumping into the `psql` interactive shell. Run the following commands in your terminal, and you should see that tables for `users`, `profiles`, `cats`, and `toys` exist.

```bash
psql cat_collector_api
\dt
```

## React Client App
[Cat Collector React](https://github.com/whlong1/cat-collector-react)