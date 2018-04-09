from flask import Flask
from flask import render_template, request
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from werkzeug import secure_filename


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      key = ClarifaiApp(api_key='*')
      model = key.models.get('Bugz')
      image = ClImage(url='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Theraphosa_blondi_MHNT.jpg/220px-Theraphosa_blondi_MHNT.jpg')
      model.predict([image])
      print model.predict_by_url(url='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Theraphosa_blondi_MHNT.jpg/220px-Theraphosa_blondi_MHNT.jpg')
      #return render_template('results.html', summary = results)
      return 'file uploaded successfully'


if __name__ == "__main__":
    app.run()
