# Crater baiter app
Helps the average up-to-no-good mage keep track of unhelpful portals and their victims


auth is handled using discord oauth


## setup dev
create python virtual env. `python=3.9.15`

```bash
pip install -r requirements.txt

export DISCORD_CLIENT_ID=....
export DISCORD_SECRET_ID=....

python run.py
```


## Run in prod
TODO:
- build container
- kustomize for k8s deployment