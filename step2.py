from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='f805f0ec701747a2ae4db700dd78f217')

app = ClarifaiApp()
model = app.public_models.general_model
response = model.predict_by_filename("lastframe.jpg")
concepts = response['outputs'][0]['data']['concepts']

eyes="two"
for concept in concepts:
    if( u'eyeglasses' == concept['name']):
        print "GOT IT"
        eyes="four"
print eyes+" eyes"
