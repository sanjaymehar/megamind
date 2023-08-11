# Hotel booking api for machine test

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/sanjaymehar/megamind.git
$ cd megamind
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd megamind
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/calculate_price/`.




send a POST request with the required input data in JSON format:
```sh
{
    "booking_type": 1, 
    "number_of_days": 5, 
    "number_of_adults": 2, 
    "number_of_children": 1
}
```
Replace "booking_type" with the ID of the desired booking type from the database.

### Receive a response with the calculated price:
```sh
{
    "calculated_price": 70.00
}
```

## Admin Panel
To set up booking types and formulas, you can access the Django admin panel:
navigate to `http://127.0.0.1:8000/admin/`.
```sh
Username: admin
Password: admin
```
