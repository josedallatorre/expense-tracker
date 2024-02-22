FROM python:3.9-slim-bullseye
COPY db.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD python ./db.py
# Or enter the name of your unique directory and parameter set.