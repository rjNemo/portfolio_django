# Portfolio

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
![Django](https://img.shields.io/pypi/djversions/django-magnificent-messages) [![License](https://img.shields.io/github/license/rjNemo/portfolio_django)](LICENSE.md) ![Release](https://img.shields.io/github/v/release/rjNemo/portfolio_django) ![Tag](https://img.shields.io/github/v/tag/rjNemo/portfolio_django)

![logo](/app/static/images/apple-touch-icon.png)

Personal portfolio

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need the latest `Python 3` version to install `portfolio`.

### Installing

A step by step series of examples that tell you how to get a development env running

Create a virtual envoronment:

```bash
python -m venv .env
source .env/bin/activate
```

## Usage

In the main application folder launch the server using

```bash
python manage.py runserver
```

## Deployment

An example app is deployed on [Heroku](https://www.heroku.com/) at this [address](https://ruidyportfolio.herokuapp.com/)

Follow these steps to deploy. Compile the application:

```bash
TIME=$(date)
git add -A
git commit -am "deploy $TIME"
git push heroku master
heroku run python manage.py makemigrations
heroku run python manage.py migrate
```

## Built With

- [Django](https://www.djangoproject.com/) - The Web framework for perfectionists with deadlines
- [Bootstrap](https://getbootstrap.com/) - The most popular HTML, CSS, and JS library in the world
- [PostgreSQL](https://www.postgresql.org/) - The world's most advanced open source database

## Contributing

Please read [CONTRIBUTING.md](contributing.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](https://semver.org/) for versioning. For the versions available, see the [CHANGELOG.md](CHANGELOG.md) and the [tags on this repository](https://github.com/rjNemo/portfolio/tags).

## Authors

- **Ruidy Nemausat** - _Initial work_ - [rjNemo](https://github.com/rjNemo)

See also the list of [contributors](https://github.com/rjNemo/portfolio/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
