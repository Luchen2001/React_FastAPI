# How to run

1. change all of the IP address in the scripts

cd ~/React_FastAPI

vim nginx_react_config

cd ~/React_FastAPI/fastapi-react/frontend/src

vim App.js

cd ~/React_FastAPI/fastapi-react/backend

vim fastapi_server.py

2. match the path (*), log into secret key and run 

cd ~/React_FastAPI/fastapi-react/backend

export PATH="/home/ubuntu/.local/bin:$PATH"

. ./secrets.sh

python3 main.py


# Notes

 . ./secrets.sh
 
uvicorn main:app --reload  

uvicorn fastapi_server:app --host 0.0.0.0 --port 8000

https://gitlab.unimelb.edu.au/feit-comp90024/comp90024/-/tree/master/ado
