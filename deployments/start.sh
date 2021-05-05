#!/usr/bin/env sh
uvicorn main:app --port 8080 --host 0.0.0.0 --reload
#docker build -t project/nginx -f deployments/Dockerfile ./ 
#docker run -p 8080:8080 -it project/nginx 
