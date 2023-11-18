# TYBC Server

This project is a Django backend server for the TYBC application.

## Installation

### Prerequisites

```
pip install -r requirements.txt  
```

### Steps

1. Clone the repository:
git clone https://github.com/tarun-hegde/tbyc-server.git  

2. Create a virtual environment and activate it:
```
virtualenv venv
./venv/Scripts/activate
```  

Migrate the database:
```
python manage.py makemigrations    
python manage.py migrate  
```

Start the development server:  
```
python manage.py runserver  
```

The endpoints are as follows:  
http://127.0.0.1:8000/admin : The Django admin interface  
http://127.0.0.1:8000/api/login/ [name='token_obtain_pair'] : Obtain a JWT token for authentication    
http://127.0.0.1:8000/api/verify/ [name='verify-otp'] : Verify an OTP code for authentication  
http://127.0.0.1:8000/api/refresh/ [name='token_refresh'] : Refresh an expired JWT token    
http://127.0.0.1:8000//api/logout/ [name='logout'] : Logout of the current user  
http://127.0.0.1:8000//api/register/ [name='registration'] : Register a new user  
http://127.0.0.1:8000//api/experiment/ [name='demo'] : An example endpoint  
http://127.0.0.1:8000//api/experiment2/ [name='demo2'] : Another example endpoint  

You should now be able to access your Django project.  

Create a superuser to view admin panel if you want to:  
```
python manage.py createsuperuser
```

Setup the EMAIL_HOST_USER and EMAIL_HOST_PASSWORD in the .env files.
