###JRD Url Shortner###

Please follow the steps to run the application.

Prerequesties
    elasticsearch
    python3

I am using 
	elasticsearch 6.8.4
	python 3.6

	please check the link for installing elasticsearch
	https://www.elastic.co/guide/en/elasticsearch/reference/6.8/deb.html


Steps to perform 

```
	Create a virtual environment
	
	virtualenv env --python=python3

	source ./env/bin/activate

	cd url/

	pip install -r requirement.txt

```

I am updating Database along with this repository user also adde to the database

```
python manage.py runserver

http://127.0.0.1:8000/
```
Application will be up now.
You can add Url that wil convert to short urls
These are the users which I created.

Admin User

```
username : admin
password : admin123

```

users:
```
username : test
password : test@123

username : tester
password : test@123
```

