FROM python:3.7-slim
EXPOSE 8080
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

RUN pip install fastapi
RUN pip install uvicorn
COPY ./../main.py /main.py
COPY "deployments/start.sh" "/usr/local/bin/start.sh"
ADD /deployments/start.sh /usr/local/bin/start.sh

ENTRYPOINT ["sh","/usr/local/bin/start.sh"]

