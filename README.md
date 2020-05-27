# Simple ecommerce site with Stripe payments integration

This is a simple ecommerce website selling boxes, built with Django. Users can purchase these boxes, powered by Stripe. This project was built to demonstrate usage of a Stripe integration.


## Setup

### Prerequisites

1. Install the lasest version of Python from [the website](https://www.python.org/downloads/) or using your operating system's package manager.

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

### Stripe settings

At the bottom of `/simple_shop/settings.py`, set your Stripe API secret and publish key values for `STRIPE_SECRET_KEY` and `STRIPE_PUBLISH_KEY` respectively.


### Webhook receiver settings

This app uses the `payment_intent.succeeded` event to asynchronously complete the purchase. You will need to set up your local web server to receive webhook events from Stripe. To do so, use (ngrok)[https://ngrok.com/]. Download and install ngrok from the website. Follow the instructions (here)[https://dashboard.ngrok.com/get-started/setup] to set it up.

After setup, do the following:
1. Start `ngrok` on port 8000
```
./ngrok http 8000
```
2. Once it is running, you will notice two Forwarding hosts in its console. It will look something like this:
```
Forwarding                    http://4885e61e.ngrok.io -> http://localhost:8000
```
3. In the (test webhooks page)[https://dashboard.stripe.com/test/webhooks] on the Stripe Dashboard, add a new endpoint. The endpoint should use the ngrok host followed by the path `/cart/payment-complete/`. For the example above, the endpoint should be `http://4885e61e.ngrok.io/cart/payment-complete/`. Make sure to include the trailing slash.
4. At the bottom of `/simple_shop/settings.py`, add a new entry in `ALLOWED_HOSTS` for your ngrok host. For example:
```
ALLOWED_HOSTS = [
    '4885e61e.ngrok.io',
    'localhost'
]
```

### Starting the server

From the project root folder, with the virtual environment activated, start the server:
```
$ python manage.py runserver
```


## Using the app

If setup was successful, the app will be running at [http://localhost:8000](http://localhost:8000). You can sign up for a new user account in the app, or log in with the admin user (see section below).


### Using the admin dashboard

You can view and manage all objects, including payments, via the Django admin dashboard at [http://localhost:8000/admin](http://localhost:8000/admin). Since this is a demo app, an admin user has already been created for you. The credentials are:
```
username: admin
password: password
```

### Making purchases

Add some items to your cart and go to the checkout flow. You can then test the payments integration.


### Viewing completed payments

When payments are completed successfully, they are saved in the database. You can view completed payments for all users in the admin dashboard at [http://localhost:8000/admin/shopping_cart/payment/](http://localhost:8000/admin/shopping_cart/payment/).

Alternatively, you can view completed payments for the logged-in user on their order history page at [http://localhost:8000/cart/order-history/](http://localhost:8000/cart/order-history/).
