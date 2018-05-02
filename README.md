# Ticross
[![Build Status](https://travis-ci.org/arponpes/ticross.svg?branch=master)](https://travis-ci.org/arponpes/ticross) [![Coverage Status](https://coveralls.io/repos/github/arponpes/ticross/badge.svg?branch=master)](https://coveralls.io/github/arponpes/ticross?branch=master)

### Configure development environment

Requirements

+ python
+ pipenv

``` bash
pipenv install --dev

createdb timecontroller

python manage.py migrate
python manage.py makemigrations

python manage.py createsuperuser

```
## Available commands

| Name          | Command           | 
| ------------- |:-------------:| 
| projectExcel  | Print the projects in excel |

### Documentación


* [django](https://docs.djangoproject.com/en/2.0/)
