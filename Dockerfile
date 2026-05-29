FROM clinic-fastapi-base:1.0

WORKDIR /code

COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]