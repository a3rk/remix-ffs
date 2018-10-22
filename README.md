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


### setting up on apache with mod_wsgi
1. git clone into /var/www/remix-ffs
2. copy settings_old.py to settings.py and adjust parameters
3. create a python virtual environment to run the application
4. activate your virtual env. pip install all required packages as above
5. follow instructions here to setup your apache with the appropriate python interpreter: https://pypi.org/project/mod_wsgi/
```pip install mod_wsgi```
mod_wsgi cannot run a virtual environment; it runs its own internal interpreter.  so you must set mod_wsgi to use your new compiled version of mod_wsgi
4. set apache to use your new mod_wsgi
run the command mod_wsgi-express module-config. This will output something like:

```LoadModule wsgi_module /usr/local/lib/python2.7/site-packages/mod_wsgi/server/mod_wsgi-py27.so
WSGIPythonHome /usr/local/lib```
5. put this into  your mods-available section under wsgi.load file
6. sample virtualhost file
```
<IfModule mod_ssl.c>
<VirtualHost *:443>
        ServerName remixffs.hopto.org
        ServerAdmin guzzijones12@gmail.com
        WSGIDaemonProcess remix_ffs.hopto.org threads=2 python-home=/home/ubuntu/venv/ffs_prod display-name=remix-ffs-ssl
        WSGIScriptAlias / /var/www/remix-ffs/flaskapp.wsgi
        <Directory /var/www/remix-ffs/>
            Order allow,deny
            Allow from all
        </Directory>
        Alias /static /var/www/remix-ffs/funding/static
        <Directory /var/www/remix-ffs/funding/static/>
            Order allow,deny
            Allow from all
        </Directory>
        ErrorLog ${APACHE_LOG_DIR}/error.log
        LogLevel warn
        CustomLog ${APACHE_LOG_DIR}/access.log combined

SSLCertificateFile /etc/letsencrypt/live/remixffs.hopto.org/fullchain.pem
SSLCertificateKeyFile /etc/letsencrypt/live/remixffs.hopto.org/privkey.pem
Include /etc/letsencrypt/options-ssl-apache.conf
</VirtualHost>
</IfModule>

```
7. create wsgi file in /var/www/remix-ffs. mine was called flaskapp.wsgi
```
#!/usr/bin/python
# Fired up virtualenv before include application
import os
#activate_env = os.path.expanduser(os.path.join(os.path.dirname(__file__), '/home/ubuntu/venv/ffs_prod/bin/activate_this.py'))
#exec(open(activate_env).read())
import site
import sys 
print(sys.version) 
# Add virtualenv site packages
#site.addsitedir(os.path.join(os.path.dirname(__file__), '/home/ubuntu/venv/ffs_prod/lib/python3.5/site-packages'))
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/remix-ffs/")
logging.debug("version: " +sys.version)

from funding.factory import create_app
import settings
application = create_app()

```

8. setting up ssl
9 ```sudo add-apt-repository ppa:certbot/certbot```
10. ```sudo apt-get update```
11. ```sudo apt-get install python-certbot-apache```
12. ```sudo certbot --apache -d example.com``` - example.com is your virtualhostname
13. ``` sudo certbot --apache -d example.com -d www.example.com``` - example.com is your virtualhosthame
14. setup cronjob under root to renew your ssl cert 
``` 1 1 * * * crontab renew ```


### to-do

- [] rate limit posting of proposals per user
- [x] Define coin variable
- [] Define one exchange API URL
- [] Automated setup
- [] User follow proposals
- [x] flask migrate for db migrations
