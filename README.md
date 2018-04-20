# Database project

## Backend

### Dependency
- python3
- django
- djangorestframework
- django-cors-header

## log

### 2018.4.12
1. add email service, in the url ./send
 but the views is writting in the database/views.py, so its not healthy

### 2018.4.13
1. add sign in, in the url ./signin
2. this need to use POST method, and need contain 'username', 'password', 'email'
3. I close the 'CSRF ' in the setting.py middleware
4. I add djangorestframework-jwt for auth, but it's not work right away

### 2018.4.20
1. jwt is OK, now need to get the token at /api-token-auth/ first, and then add the header "Authorization": '"JWT "+token'
2. now i only lock the Users and Departments.

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
