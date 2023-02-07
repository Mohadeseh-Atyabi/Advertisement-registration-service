import requests

api_key = 'acc_6db94b19d8f18fd'
api_secret = 'acadaec68a150bc9bf367e80b1b0e4aa'


def tag(path):
    response = requests.post(
        'https://api.imagga.com/v2/tags',
        auth=(api_key, api_secret),
        files={'image': open(path, 'rb')})
    js = response.json()['result']['tags']
    for i in js:
        # print(i)
        if i['tag']['en'] == 'vehicle' and i['confidence'] > 50:
            return "accepted", js[0]['tag']['en']
    return "rejected", None
