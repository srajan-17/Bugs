from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='c4406989d7624ad0aa336616ea3e4ada')

model = app.models.get('general-v1.3')
image = ClImage(url='https://samples.clarifai.com/metro-north.jpg')
model.predict([image])
print model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
