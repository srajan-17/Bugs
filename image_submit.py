from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='c4406989d7624ad0aa336616ea3e4ada')

model = app.models.get('Bugz')
image = ClImage(url='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Theraphosa_blondi_MHNT.jpg/220px-Theraphosa_blondi_MHNT.jpg')
model.predict([image])
print model.predict_by_url(url='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Theraphosa_blondi_MHNT.jpg/220px-Theraphosa_blondi_MHNT.jpg')
