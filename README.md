# nasa-window-to-mars

## What is the application about?

This repository is a light weight REST API application based on Flask framework for accessing Mars POV images from NASA's rovers. Corpus is image data from Mars Rovers (Curiosity, Spirit and Opportunity) through nine on-board cameras.


## What are the dependencies?

1. In order to access images accessbile through NASA's Open APIs gateway, fetch a developer key from https://api.nasa.gov. Once you have the key, export it as an environmental variable named "NASA_API_KEY" on the system you are installing this application on.

$export NASA_API_KEY=<your_api_key>

This key will be used by the configuration script that will fire secondary API calls to fetch the image.

2. Install python libraries necessary for the Flask framework to function. These are provided in requirements.txt and include:

alembic==1.1.0
app==0.0.1
certifi==2019.9.11
chardet==3.0.4
Click==7.0
Flask==1.1.1
Flask-Migrate==2.5.2
Flask-SQLAlchemy==2.4.0
Flask-WTF==0.14.2
idna==2.8
itsdangerous==1.1.0
Jinja2==2.10.1
Mako==1.1.0
MarkupSafe==1.1.1
python-dateutil==2.8.0
python-editor==1.0.4
requests==2.22.0
six==1.12.0
SQLAlchemy==1.3.8
urllib3==1.25.6
Werkzeug==0.15.5
WTForms==2.2.1

Once everything is set, launch the application and head to localhost.


## How does it feel and look?

![Homepage](https://user-images.githubusercontent.com/53545889/66077245-92c23180-e52d-11e9-8e30-80c10cb40676.png)

![Rover Image](https://user-images.githubusercontent.com/53545889/66077513-1b40d200-e52e-11e9-8d57-7ef834d22689.png)

![Rover Image](https://user-images.githubusercontent.com/53545889/66077550-285dc100-e52e-11e9-887d-95d44a6e02ba.png)

![Rover Image](https://user-images.githubusercontent.com/53545889/66077565-2f84cf00-e52e-11e9-8872-98bc024a0361.png)

![Rover Image](https://user-images.githubusercontent.com/53545889/66077569-33185600-e52e-11e9-925a-4b81b0b43e1f.png)

![Rover Image](https://user-images.githubusercontent.com/53545889/66077580-37447380-e52e-11e9-8d66-c2a046a55a9c.png)


