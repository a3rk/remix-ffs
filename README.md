# Funding System 

## Description

Do more with your cryptocurrency by getting the community involved. The goal of the Funding System is to enable community members to complete projects and be paid for the projects by other community members. 

The Funding System was written entirely in Python. It was originally developed by dsc_ (skftn) for the Wownero currency but later updated by various community members to be accepted for cryptonote currencies. 

## Features
* Simplistic user system
* Proposal system
* Accounting system
* Stats per proposal:
    * Coins received
    * Coins paid out
    * Coins available
* Comment system per proposal
* More in development

## Installation (locally)

set environment variables for: 
* BLOCK_EX_SERVER
* COIN_PNG,
* COINCODE, 
* COINTICKER, 
* DB_FFS,
* DISCORD_URL,
* IRC,
* PSQL_USER_FFS,
* PSQL_PASS_FFS, 
* RPC_PORT
* SERVER_DNS,
* SECRET

Better instructions to follow in the future.

### Install dependencies

```
sudo apt install python-virtualenv python3 redis-server postgresql-server-dev-* \
postgresql postgresql-client python-pip virtualenv git
```

1. Create a Postgres user/database for this project that matches the DB_FFS environment var
2. Issue the following commands:
```
	cd ~/git/a3rk/;
	git clone https://github.com/a3rk/remix-ffs.git;
	cd remix-ffs;
	virtualenv -p python3 ~/virtualenv/remix-ffs-env;
	source ~/virtualenv/remix-ffs-env/bin/activate;
	pip install -r requirements.txt;
	python migrate.py db migrate;
	python run_dev.py;
```
3. Register as a new user on the site
4. Flip the admin bit on for the user using psql or pgadmin

### to-do

- [ ] Rate limit posting of proposals per user
- [x] Define coin variable
- [ ] Define one exchange API URL
- [ ] Automated setup
- [ ] User follow proposals
- [x] Flask migrate for db migrations
