FROM python:3.9-slim-bullseye
COPY . .
COPY requirements.txt .
# Install core dependencies.
RUN apt-get update && apt-get install -y libpq-dev build-essential
RUN pip install -r requirements.txt
CMD python ./main.py
# Or enter the name of your unique directory and parameter set.