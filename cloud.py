import requests
import six
import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
    cloud_name = "enviropi",
    api_key = "183424931379914",
    api_secret = "3GFjxQJ1ExuMU8-acIQD9yUu2MY"
)

test = cloudinary.uploader.upload("test_send_pic.jpg", public_id="letsgo")

print(test["secure_url"])


##filetoSend = {'file': 'test_send_pic.jpg', 'upload_preset': 'dhe9tf4s'}
##testing = requests.post('https://api.cloudindary.com/v1_1/enviropi/image/upload', data=filetoSend)
##print(testing)
