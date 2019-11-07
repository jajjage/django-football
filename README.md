# django-football

This is a django website for storing match statistics (i.e., attendance/goals) for a football team.
It has both templates and an API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
You can run the project locally and use Virtualenv, which is the [recommended installation approach](https://docs.djangoproject.com/en/stable/topics/install/#install-the-django-code) for Django itself.

#### Dependencies
* Python 3.6 or higher
* [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
* [VirtualenvWrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) (optional)

### Installation

With [PIP](https://github.com/pypa/pip) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
installed, run:

    mkvirtualenv football --python=python3

Now we're ready to set up the project itself:

    git clone https://github.com/Thijss/django-football.git
    cd django-football
    pip install -r requirements/development.txt

Next, we'll set up our local environment variables. We use django-environ to help with this. 
It reads environment variables located in a file name `.env` in the top level directory of the project. Copy the example
and fill out all necessary fields:

    $ cp .env.example .env
    $ nano .env

To set up your database and load initial data, run the following commands:

    ./manage.py migrate
    ./manage.py runserver


## Running the tests

You can run the tests with:

    ./manage.py test

## Authors

* **Thijs Baaijen** - *Initial work* - [Thijss](https://github.com/Thijss)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
