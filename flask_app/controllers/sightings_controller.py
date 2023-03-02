import os
from flask_app import app
from flask import render_template,redirect,request,session,flash
from werkzeug.utils import secure_filename
from flask_app.models.sighting_model import Sighting

UPLOAD_FOLDER = 'flask_app/static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#  ? what are iphone photo file extensions? JPGs? 
ALLOWED_EXTENSIONS = { 'jpg', 'jpeg', 'png' }

# ? What is this doing? This extracts the filename and the file extension? How?  Finds the frst '.' in filemname
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 



#================= 1 READ ALL - RENDER  =================
@app.route('/')
def index():
    # all_examples = Example.get_all() 
    return render_template('index.html') 

#================= 1 READ ALL - RENDER  =================
@app.route('/sightings')
def sightings():
    all_sightings = Sighting.get_all() 
    return render_template('sightings.html', all_sightings=all_sightings) 

#================= 2 READ ONE - RENDER  =================
@app.route("/learn_more")
def learn_more():
    # data = {
    # 'id':id
    # }
    # this_example = Example.get_one(data)
    return render_template('learn_more.html')

#================= 3 CREATE ONE - ACTION  =================
@app.route('/sightings/create', methods=['post'])
def create_sighting():

    # print(request.form) #littlebitofcodeandtest
    # #? Server side Validation breaks the modal window
    # # if not Sighting.validator(request.form):
    # #     return redirect('/sightings/new')

    # Sighting.create(request.form)


    file = request.files['file']
    print(file)
    # if file.filename == '':
    #     flash('No selected file')
    #     return redirect('/')

    # ? What is beinng asked in this if statement
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
        #send filename and rest of the from to the DB
    Sighting.create({**request.form, 'filename': filename})
    return redirect('/sightings')
