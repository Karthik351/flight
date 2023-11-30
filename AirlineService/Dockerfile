FROM python:3.9
RUN mkdir -p /flights
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /flights
COPY flight/flights/flights/requirements.txt /flights/requirements.txt
RUN pip install -r requirements.txt
COPY flight/flights/flights /flights/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]