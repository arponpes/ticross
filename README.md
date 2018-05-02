# Ticross

[![Coverage Status](https://coveralls.io/repos/github/arponpes/Ticross/badge.svg?branch=feat%2Fgithubmigrate)](https://coveralls.io/github/arponpes/Ticross?branch=feat%2Fgithubmigrate ) [![Build Status](https://travis-ci.org/arponpes/Prueba-travis.svg?branch=master)](https://travis-ci.org/arponpes/Prueba-travis)


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
