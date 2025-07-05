# Python/Django Portfolio Tutorial

## Joe O'Regan

Tutorial from LinkedIn Learning [here](https://www.linkedin.com/learning/building-a-personal-portfolio-with-django/)

- Django
- PostgreSQL
- Bootstrap (jQuery, Popper)

#### Screenshots

![Django Portfolio Site](https://raw.githubusercontent.com/joeaoregan/portfolio-django-py/master/images/screenshot_site.jpg "Django Portfolio Site")

###### Django Portfolio Site

#### References

[Building a Personal Portfolio with Django](https://www.linkedin.com/learning/building-a-personal-portfolio-with-django/)

#### Downloads

[python 3](https://www.python.org/downloads/)  
[django](https://www.djangoproject.com/download/)  
[postgresql](https://www.postgresql.org/download/)  
[pgAdmin 4](https://www.pgadmin.org/download/)
[Bootstrap 4.1 Album example](https://getbootstrap.com/docs/4.1/examples/album/)
[Bootstrap 4.1 Compiled CSS and JS](https://getbootstrap.com/docs/4.1/getting-started/download/)
[jQuery](https://jquery.com/download/)
[Popper](https://unpkg.com/popper.js@1.16.1/dist/umd/popper.min.js)

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

```console
\password <username>
```

##### Boostrap

Album Example

[Bootstrap 4.1 Album Example](https://getbootstrap.com/docs/4.1/examples/album/)

[Bootstrap 4.1 Quickstart](https://getbootstrap.com/docs/4.1/getting-started/introduction/)

#### Static files

```console
python3 manage.py collectstatic
```
