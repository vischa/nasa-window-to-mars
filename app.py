from flask import Flask, render_template, flash, redirect, url_for, request, session
from config import Config
from mars_form import DataForm
import requests
import json

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/api/v1/nasa_mars_photos', methods = ['GET','POST'])
def login():
        form=DataForm()
        if form.validate_on_submit():
                session['rover']=form.rover.data
                session['sol']=form.sol.data
                session['camera']=form.camera.data
                return redirect(url_for('photo_out', picture=form.rover.data))
        return render_template('mars_form.html',form=form)

@app.route('/api/v1/rover_photo')
def photo_out():
        DEMO_KEY = Config.NASA_API_KEY
        ROVER = session['rover']
        MARTIAN_SOL = session['sol']
        CAMERA = session['camera']
        r = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/{}/photos?sol={}&camera={}&api_key={}".format(ROVER,MARTIAN_SOL,CAMERA,DEMO_KEY))
        photo_dict = r.json()
        for photo in photo_dict['photos']:
                current_image = photo['img_src']
                break
        return render_template('photo_out.html', picture = current_image, image_meta_data = request.args.get('picture'))

if __name__ == '__main__':
        app.debug = True
        app.run(host='0.0.0.0')
