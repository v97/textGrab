import base64
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import requests

file = "text.png"
API_KEY = "AIzaSyCEpL_gTRvYcDhLthSOg3v_jEltZj95bl0"

with open(file, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()
    payload = {
        "requests": [
            {
                "image": {
                    "content": encoded_image
                },
                "features": [
                    {
                        "type": "TEXT_DETECTION"
                    }
                ]
            }
        ]
    }

r = requests.post('https://vision.googleapis.com/v1/images:annotate?key=' + API_KEY, json=payload)
print(r.json()['responses'][0]['textAnnotations'][0]['description'])

img = mpimg.imread(file)
plt.imshow(img)
plt.show()