FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY .vscode ./
COPY app ./
COPY .flaskenv ./
COPY config.py ./
COPY README.md ./
COPY tox.ini ./
COPY wsgi.py ./

# tell the port number the container should expose
EXPOSE 5000

CMD [ "python", "-m", "flask", "run",  "--host=0.0.0.0"]
