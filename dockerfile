FROM python:3.12.2-slim as base
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 5001
CMD ["flask", "--app" , "app.run:app", "run", "--debug" , "--host=0.0.0.0" , "--port=5001"]
