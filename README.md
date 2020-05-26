# Simple ecommerce site with Stripe payments integration

This is a simple ecommerce website selling boxes, built with Django. Users can purchase these boxes, supported by a Stripe integration. This project was built to demonstrate usage of a Stripe integration.



## Setup

### Prerequisites

1. Install Python from [the website](https://www.python.org/downloads/) or using your operating system's package manager.

2. Make sure your version of Python is 3.8.3:
```
$ python --version
```
3. Install pip:
```
$ sudo easy_install pip
```
4. It is recommended to use a virtual environment to run Django apps locally. Install virtualenv:
```
$ pip install virtualenv
```
5. Inside the project's root folder, create a virtualenv:
```
$ virtualenv env
```
6. Activate the virtual enviroment:
```
$ source env/bin/activate
```
7. Install the project requirements:
```
$ pip install -r requirements.txt
```
8. Run migrations:
```
$ python manage.py migrate
```

### Stripe Settings

At the bottom of `/simple_shop/settings.py`, set your Stripe API secret and publish key values for `STRIPE_SECRET_KEY` and `STRIPE_PUBLISH_KEY` respectively.

### Creating an admin user

You can view and manage all objects, including payments, via the Django admin dashboard. To do so, run the following command and follow the instructions:
```
$ python manage.py createsuperuser
```
When the server is running, the admin dashboard can be accessed at http://localhost:8000/admin

### Starting the server

From the project root folder, with the virtual environment activated, start the server:
```
$ python manage.py runserver
```


## Using the app

If setup was successful, the app will be running at [http://localhost:8000](http://localhost:8000). You can sign up for a new user account in the app, or log in with the admin user.

### Making purchases

Add some items to your cart, and access the checkout flow. You can then test the payments integration.

### Viewing completed payments

When payments are completed successfully, they are saved in the database. You can view completed payments for all users in the admin dashboard at [http://localhost:8000/admin/shopping_cart/payment/](http://localhost:8000/admin/shopping_cart/payment/).

Alternatively, you can view completed payments for the logged-in user on their [order history page](http://localhost:8000/cart/order-history/).