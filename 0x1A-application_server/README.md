# 0x1A. Application server

The purpose of this project is to add an application server piece to our web infrastructure, plug it to our Nginx web server and make it serve our Airbnb clone project.

## Requirements
### General
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- Everything Python-related must be done using ```python3```
- All config files must have comments

### Bash Scripts
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- All your Bash script files must be executable
- Your Bash script must pass ```Shellcheck``` (version ```0.3.3-1~ubuntu14.04.1``` via ```apt-get```) without any error
- The first line of all your Bash scripts should be exactly ```#!/usr/bin/env bash```
- The second line of all your Bash scripts should be a comment explaining what is the script doing

---
File | Task
---|---
0-welcome_gunicorn-upstart_config, 0-welcome_gunicorn-nginx_config | ```Upstart``` script that starts a ```Gunicorn``` instance to serve ```web_flask/0-hello_route.py``` from ```AirBnB_clone_v2```; Setup ```Nginx``` so that the route ```/airbnb-onepage/``` points to Gunicorn instance
1-pass_parameter-upstart_config, 1-pass_parameter-nginx_config | ```Upstart``` script that starts a Gunicorn instance to serve ```web_flask/6-number_odd_or_even.py``` from your ```AirBnB_clone_v2```; Setup ```Nginx``` so that the ```route/airbnb-dynamic/``` points to your ```Gunicorn``` instance
2-api-upstart_config, 2-api-nginx_config | ```Upstart``` script that starts a ```Gunicorn``` instance to serve ```api/v1/app.py``` from your AirBnB_clone_v3; ```Nginx``` setup script so that the route ```/api/``` points to ```Gunicorn``` instance
3-complete_webapp-upstart_config, 3-complete_webapp-nginx_config | ```Upstart``` script that starts a ```Gunicorn``` instance to serve ```web_dynamic/2-hbnb.py``` from your ```AirBnB_clone_v4```; ```Nginx``` setup script so that the route ```/``` points to the ```Gunicorn``` instance, it properly serves the static assets found in ```web_dynamic/static/```, reconfigured ```web_dynamic/static/scripts/2-hbnb.js``` to the correct IP and port

## Author
Francesca Cantor
