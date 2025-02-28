<img src="images/168805567091_LITrevu banner.png" >

# LITRevu

## Presentation

LITRevu is a blog for books lover.  
You can ask or/and post ticket and review.

## Getting started

- Python version used 3.10.12

### Packages used

- Django
- pillow

### Virtual environment

#### Creation

Create the virtual environment.

Replace :
- \<version> by your version number of python
- <nom_de_l_environnement_virtuel> by the name you like

```
python<version> -m venv <nom_de_l_environnement_virtuel>
```

#### Activation

Activate the virtual environment.

For windows
```
<nom_de_l_environnement_virtuel>/Scripts/activate
```

For Unix/macOs

```
source .<nom_de_l_environnement_virtuel>/bin/activate
```

#### Packages

Install needed packages for the script.
```
pip install -r requirements.txt
```

### Download application

Be sure to be in your vitual environment

Clone this repository
```
git clone https://github.com/spleenYou/OC-P9.git
```

### Start server

Change directory to be in Django project where you can find the file "manage.py"
```
cd OC-P9/
```

And start running Django server
```
python manage.py runserver
```


## Website


In your internet browser, go on this URL to see the login page and a link to create an account
```
http://127.0.0.1:8000
```

Possiblity to create an account or test the website with one of the following login/password :
- SuperUser :
    - Login : spleen85
    - Password : SuperS3cret!!!
- User :
    - Login : toto
    - Password : S3cret!!!
    - Login : lea
    - Password : S3cret!!!
    - Login : matthieu
    - Password : S3cret!!!
    - Login : aurelie
    - Password : S3cret!!!

### Navigation bar

After logged-in, there are buttons for navigating the website.

<img src="images/nav.png"><br>

- LITRevu: go on home page
- Flux: go on home page
- Posts: To manage your own tickets and reviews
- Abonnements: To manage your followed users and see who follow you
- Se déconnecter: To log out

#### LITRevu / Flux

On this page, it's possible to see :
- Tickets and reviews for logged-in user
- Tickets and reviews for users followed by the logged-in user
- Reviews for users following the logged-in user

And it's also to review tickets for users followed by the logged-in user

#### Posts

This page contained tickets and reviews by the logged-in user.  
They can be updated or deleted.

#### Abonnements

This page contained the users you follow, with the option of following other users and the users who follow you.

#### Se déconnecter

To be disconnected