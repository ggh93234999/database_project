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

### 2018.4.13
 add sign in, in the url ./signin
 this need to use POST method, and need contain 'username', 'password', 'email'
 and I close the 'CSRF ' in the setting.py middleware
 and I add djangorestframework-jwt for auth, but it's not work right away

## Installation

### Pipenv

1. install pipenv
2. `pipenv install django djangorestframework django-cors-headers djangorestframework-jwt`
3. `pipenv shell`

### Run Django

Run Django server:

```
python3 manage.py runserver
```
