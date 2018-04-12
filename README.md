# Database project

## Backend

### Dependency
- python3
- django
- djangorestframework
- django-cors-header

## log

### 2018.4.12
 add email service, in the url ./send
 but the views is writting in the database/views.py, so its not healthy

## Installation

### Pipenv

1. install pipenv
2. `pipenv install django djangorestframework django-cors-headers`
3. `pipenv shell`

### Run Django

Run Django server:

```
python3 manage.py runserver
```