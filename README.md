# Funding System 

## Description

Do more with your cryptocurrency by getting the community involved. The goal of the Funding System is to enable community members to complete projects and be paid for the projects by other community members. 

The Funding System was written entirely in Python. It was originally developed by dsc_ (skftn) for the Wownero currency but later updated by various community members to be accepted for cryptonote currencies. 

## Features
- Simplistic user system
- Proposal system
- Accounting system
- Stats per proposal
-- Coins received
-- Coins paid out
-- Coins available
- Comment system per proposal
- More in development

## Installation (locally)

set environment variables for: 
BLOCK_EX_SERVER
COIN_PNG,
COINCODE, 
COINTICKER, 
DB_FFS,
DISCORD_URL,
IRC,
PSQL_USER_FFS,
PSQL_PASS_FFS, 
RPC_PORT
SERVER_DNS,
SECRET

Better instructions to follow in the future.

### Install dependancies

```sudo apt install python-virtualenv python3 redis-server postgresql-server-dev-* postgresql postgresql-client python-pip virtualenv git```

1. Create a Postgres user/database for this project
2.
```
git clone 
cd aeon-funding-system
virtualenv -p /usr/bin/python3 <venv>
source <venv>/bin/activate
pip install -r requirements.txt
python migrate.py db migrate
python run_dev.py
```
3. move settings_org.py to settings.py and set all variables
3. register as a new user on the site
4. flip the admin bit on for the user using psql or pgadmin

### to-do

- [] rate limit posting of proposals per user
- [x] Define coin variable
- [] Define one exchange API URL
- [] Automated setup
- [] User follow proposals
- [x] flask migrate for db migrations
