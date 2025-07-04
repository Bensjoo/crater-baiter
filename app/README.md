# Crater baiter app
Helps the average up-to-no-good mage keep track of unhelpful portals and their victims


auth is handled using discord oauth


## setup dev
create python virtual env. `python=3.9.15`

```bash
pip install -r requirements.txt

# Required env variables
DISCORD_CLIENT_ID=VALUE
DISCORD_SECRET_KEY=VALUE
SECRET_KEY=VALUE
APP_CONFIG=VALUE
HOST=VALUE
SQLALCHEMY_DATABASE_URI=VALUE

python run.py
```

# TODO:
- add new crater victim form
- start page => list of latest victims
- CRUD victims
- simple auth in debug mode