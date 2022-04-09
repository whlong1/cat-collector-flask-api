# cat-collector-flask-api

![banner](https://i.imgur.com/juxPY8i.png)

# Getting Started

Fork and clone this repo.

Once you are in the project directory, create a new virtual environment.

```bash
conda create -n cat_collector python=3.9
```

Next, activate your virtual environment with the command below. 

```bash
conda activate cat_collector
```

**Once the environment is active**, run the following command in your terminal.

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

Next up in the **`.env`**, add a **`DATABASE_URL`** with the name of our project’s database.

```
DATABASE_URL='postgresql://localhost:5432/cat_collector_api'
```

Make sure your conda environment is active and hop into the `psql` shell. 

```
psql
```

Within the `psql` shell, run the following command. Make sure the name of your database does not already exist. 

```
create database cat_collector_api;
```

Run the following command to exit the shell. 

```
\q
```

Run the following commands in your terminal to update your database.

```bash
python3 -m flask db init
python3 -m flask db migrate
python3 -m flask db upgrade
```

Run the following command to start your application. 

```bash
python3 app.py
```

# Checking Our Database

We can verify that our initial migrations have gone through by jumping into the `psql` interactive shell. Run the following commands in your terminal, and you should see that tables for `users` and `profiles` exist.

```bash
psql cat_collector_api
\dt
```

## React Client App
[Cat Collector React](https://github.com/whlong1/cat-collector-react)