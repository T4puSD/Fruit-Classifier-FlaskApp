from flask import Flask, render_template, url_for, request, flash, redirect
from werkzeug.utils import secure_filename
import os
from scripts import ValidationWithRandomImage

UPLOAD_FOLDER = './static/uploads'
SECRET_KEY = 'some ranodm key'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY

def allowed_file(filename):
    return filename.split('.')[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/upload_img', methods =['POST'])
def upload_img():
    if request.method == 'POST':
        img = request.files['picture_upload']
        if img.filename =='':
            flash("No files selected")
            return redirect('/')
        if img and allowed_file(img.filename):
            filename = secure_filename(img.filename)
            print(filename)
            pathtosave = os.path.join(app.config['UPLOAD_FOLDER'])
            try:
                os.mkdir(pathtosave)
            except:
                print("Exception")
            
            img.save(os.path.join(pathtosave,filename))
            # return "file succefully received"
            return redirect('/predict')
@app.route('/predict', methods=['GET'])
def predict():
    #get the image
    img = None
    for dirname, path, filename in os.walk('./static/uploads'):
        img = os.path.join(dirname,filename[0])
        break
    # img = os.listdir('./static/uploads')[0]
    print(img)
    result = ValidationWithRandomImage.main(img)
    print(result)
    # os.system('cd scripts && python ValidationWithRandomImage.py ../static/uploads/{}'.format(img))
    imgname = img.split('/')[-1]
    print(imgname)
    if(result[0][1] < 0.6):
        return render_template('unsuccessfull.html',filename=imgname)
    return render_template('showimg.html', filename = imgname, fruite_name = result[0][0])

@app.route('/delete/<filename>')
def delete(filename):
    os.remove(os.path.join('.','static','uploads',filename))
    # return "fruite is: "+filename
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
