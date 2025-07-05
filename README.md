# Python/Django Portfolio Tutorial

## Joe O'Regan

Tutorial from LinkedIn Learning [here](https://www.linkedin.com/learning/building-a-personal-portfolio-with-django/)

- Django
- PostgreSQL
- Bootstrap

#### References

[Building a Personal Portfolio with Django](https://www.linkedin.com/learning/building-a-personal-portfolio-with-django/)

#### Downloads

[python 3](https://www.python.org/downloads/)  
[django](https://www.djangoproject.com/download/)  
[postgresql](https://www.postgresql.org/download/)  
[pgAdmin 4](https://www.pgadmin.org/download/)
[Bootstrap: Album example](https://getbootstrap.com/docs/5.3/examples/album/)

#### Create Project:

```console
django-admin startproject <project_name>
```

```console
django-admin startapp jobs
```

#### Start App:

```console
python3 manage.py runserver
```

#### Dependencies:

```console
pip3 install pillow
```

```console
pip3 install psycopg2
```

```console
pip3 install psycopg2-binary
```

```console
python3 manage.py makemigrations
```

```console
python3 manage.py migrate
```

```console
python3 manage.py createsuperuser
```

#### PostgreSQL

Using pgAdmin 4

```
\password <username>
```
