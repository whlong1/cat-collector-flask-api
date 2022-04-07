# flask-react-jwt-auth

# Setup

Clone the template with the command below. Be sure to replace `<name-of-your-app-here>` in the commands below with the name of your app!

```bash
git clone https://github.com/SEI-Remote/flask-react-auth-template <name-of-your-app-here>
cd <name-of-your-app-here>
```

Once you are in the project directory:

```bash
rm -rf .git
```

Re-initialize a git repository:

```bash
git init
```

Use the GitHub CLI to create a new project repository on GitHub:

```bash
gh repo create <name-of-your-app-here>
```

# Getting Started

Next we’ll need to create a new virtual environment. The dependencies involved in this configuration of Flask are a bit different, so we’ll want a fresh start with this environment. 

```bash
conda create -n flask_react
```

Next, activate your virtual environment with the command below. 

```bash
conda activate flask_react
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

In the base directory of your project, you should see a file called `**config.py**`. Update the line below with the name of **your project’s database**.

```python
SQLALCHEMY_DATABASE_URI = "postgresql://localhost:5432/<db_name_here>"
```

After updating `**config.py**`, run the following commands in your terminal. Make sure the name of your database does not already exist. 

```bash
createdb <db_name_here>
flask db init
flask db migrate
flask db upgrade
```

Run the following command to start your application. 

```bash
python3 app.py
```