
Graphene Subfilters
************************

This little django project shows a way to implement filters on nested objects using [graphene-django](https://github.com/graphql-python/graphene-django)

The following instructions describe the steps to setup/run the application from scratch.

Required Packages
-----------------

In Debian distributions 'apt-get install', in Redhat distributions 'yum install'
    
    * Python 3.7
    * Python 3.6 Dev packages
    * Python Virtual environment
    * python-pip
    * Git    


Clone this repo
---------------

Just type in the command line::

    $ git clone https://github.com/allangz/graphene_subfilters.git


Create virtualenv
-----------------

Create and activate python virtualenv::


    $ python3.7 -m venv <DIR>/test_venv
    $ source <DIR>/test_venv/bin/activate

Install Python Packages
------------------------------

To install necessary packages run::


    $ pip install -r requirements.txt

Configure Database
------------------

The example works with sqlite. Change the settings as you need. After that just run the migrations::

    $ python manage.py migrate

Run application
-----------------
To run the application just type in console::

    $ python manage.py runserver

At this point you should be able to see the [GraphiQL interface](http://127.0.0.1:8000/graphql)

If you can access the view, congrats your app is up and running !!!

Query on subnodes
------------------

The main goal of this example is implementing some filters on the nested objects from the main query using graphene-django,
the implementation for it can be found on the file polls/schema.py.

It is important to mention here, to have this feature do not use `__all__` option on the fields Meta class,
use a custom resolver for the desired fields to filter.

Here is an example of a query, with a filter in the two nested subnodes::


    {
      allQuestions(searchText: "dummy") {
        id
        questionText
        choices(searchChoices: "The") {
          choiceText
          subChoices(searchSubChoices: "another") {
            id
            subChoiceText
          }
        }
      }
    }


Load Test Data
---------------

You can load some data for the example query::

    $ python manage.py loaddata polls polls.json