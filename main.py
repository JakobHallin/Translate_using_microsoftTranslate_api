import requests, uuid, json
class Translate:
# Add your key and endpoint
    
    def __init__(self, input_text): #setup
        key = "put in the key"
        endpoint = "https://api.cognitive.microsofttranslator.com"

        # location, also known as region.
        # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
        self.location = "swedencentral"
        self.path = '/translate'
        self.constructed_url = endpoint + self.path
        self.params = {
            'api-version': '3.0',
            'from': '',
            'to': ['en']
        }
        self.headers = {
            'Ocp-Apim-Subscription-Key': key,
            # location required if you're using a multi-service or regional (not global) resource.
            'Ocp-Apim-Subscription-Region': self.location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }
        # You can pass more than one object in body.
        self.body = [{
            'text': input_text
        }]
    def requestJson(self):
        request = requests.post(self.constructed_url, params=self.params, headers=self.headers, json=self.body)
        return request.json()
    #test = response[0]
    def translatedText(self):
        response = self.requestJson()
        data = response[0]
        dataT = data['translations']
        dataText = dataT[0]['text']
        print(dataText)
        return dataText
test = Translate('J’aimerais vraiment conduire votre voiture autour du pâté de maisons plusieurs fois!')  
test.translatedText()
# 
# 
#res
#print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, se
