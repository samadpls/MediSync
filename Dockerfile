FROM python:3.10

WORKDIR /MediSync

COPY requirements.txt /MediSync/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /MediSync/
ENV DJANGO_SETTINGS_MODULE=MediSync.settings

EXPOSE 8000

# Run database migrations
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]