# nasa-window-to-mars

## What is the application about?

This repository is a light weight REST API application based on Flask framework for accessing Mars POV images from NASA's rovers. Corpus is image data from Mars Rovers (Curiosity, Spirit and Opportunity) through nine on-board cameras.


## What are the dependencies?

In order to access images accessbile through NASA's Open APIs gateway, fetch a developer key from https://api.nasa.gov. Once you have the key, export it as an environmental variable named "NASA_API_KEY" on the system you are installing this application on.

$export NASA_API_KEY=<your_api_key>

This key will be used by the configuration script that will fire secondary API calls to fetch the image.

Install python libraries necessary for the Flask framework to function. These are provided in requirements.txt.

Once everything is set, launch the application and head to localhost.


## How does it feel and look?

![Homepage](https://user-images.githubusercontent.com/53545889/66077245-92c23180-e52d-11e9-8e30-80c10cb40676.png)

![Rover Image](https://user-images.githubusercontent.com/53545889/66077513-1b40d200-e52e-11e9-8d57-7ef834d22689.png)

![Rover Image](https://user-images.githubusercontent.com/53545889/66077550-285dc100-e52e-11e9-887d-95d44a6e02ba.png)

![Rover Image](https://user-images.githubusercontent.com/53545889/66077565-2f84cf00-e52e-11e9-8872-98bc024a0361.png)

![Rover Image](https://user-images.githubusercontent.com/53545889/66077569-33185600-e52e-11e9-925a-4b81b0b43e1f.png)

![Rover Image](https://user-images.githubusercontent.com/53545889/66077580-37447380-e52e-11e9-8d66-c2a046a55a9c.png)

![Rover Image](https://user-images.githubusercontent.com/53545889/66077958-10d30800-e52f-11e9-8c56-a3d2d538c131.png)

![Rover Image](https://user-images.githubusercontent.com/53545889/66077973-1892ac80-e52f-11e9-9d8e-50016c83694b.png)


