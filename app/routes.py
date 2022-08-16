from app import app
from flask import render_template
import os

my_images = os.path.join('static','images')
app.config['UPLOAD_FOLDER'] = my_images


@app.route('/')
def index():
    fav_5 = ['kelleyvivianart','theobanoth','samdoesarts','wood.youmind','taraminart']
    return render_template('index.html',fav_5=fav_5, has_title=False)


@app.route('/kelleyvivianart')
def kelley():
    kelley1 = os.path.join(app.config['UPLOAD_FOLDER'],'kelley1.jpg')
    kelley2 = os.path.join(app.config['UPLOAD_FOLDER'],'kelley2.jpg')
    kelley3 = os.path.join(app.config['UPLOAD_FOLDER'],'kelley3.jpg')
    kelley4 = os.path.join(app.config['UPLOAD_FOLDER'],'kelley5.jpg')
    fav_5 = ['kelleyvivianart','theobanoth','samdoesarts','wood.youmind','taraminart']
    return render_template('kelleyvivianart.html', kelley1=kelley1, kelley2=kelley2, kelley3=kelley3, kelley4=kelley4, fav_5=fav_5, has_title=True)


@app.route('/theobanoth')
def theobanoth():
    the1 = os.path.join(app.config['UPLOAD_FOLDER'],'the1.jpg')
    the2 = os.path.join(app.config['UPLOAD_FOLDER'],'the2.jpg')
    the3 = os.path.join(app.config['UPLOAD_FOLDER'],'the3.jpg')
    the4 = os.path.join(app.config['UPLOAD_FOLDER'],'the4.jpg')
    return render_template('theobanoth.html', the1=the1, the2=the2, the3=the3, the4=the4, has_title=True)


@app.route('/samdoesarts')
def sam():
    sam1 = os.path.join(app.config['UPLOAD_FOLDER'],'sam1.jpg')
    sam2 = os.path.join(app.config['UPLOAD_FOLDER'],'sam2.jpg')
    sam3 = os.path.join(app.config['UPLOAD_FOLDER'],'sam3.jpg')
    sam4 = os.path.join(app.config['UPLOAD_FOLDER'],'sam4.jpg')
    return render_template('samdoesarts.html', sam1=sam1, sam2=sam2, sam3=sam3, sam4=sam4, has_title=True)


@app.route('/woodyoumind')
def wood():
    wood1 = os.path.join(app.config['UPLOAD_FOLDER'],'wood1.jpg')
    wood2 = os.path.join(app.config['UPLOAD_FOLDER'],'wood2.jpg')
    wood3 = os.path.join(app.config['UPLOAD_FOLDER'],'wood3.jpg')
    wood4 = os.path.join(app.config['UPLOAD_FOLDER'],'wood4.jpg')
    return render_template('woodyoumind.html', wood1=wood1, wood2=wood2, wood3=wood3, wood4=wood4, has_title=True)


@app.route('/taraminart')
def taraminart():
    tara1 = os.path.join(app.config['UPLOAD_FOLDER'],'tara1.jpg')
    tara2 = os.path.join(app.config['UPLOAD_FOLDER'],'tara2.jpg')
    tara3 = os.path.join(app.config['UPLOAD_FOLDER'],'tara3.jpg')
    tara4 = os.path.join(app.config['UPLOAD_FOLDER'],'tara4.jpg')
    return render_template('taraminart.html', tara1=tara1, tara2=tara2, tara3=tara3, tara4=tara4, has_title=True)

