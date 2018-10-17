from django.shortcuts import render

# Create your views here.
from Crypto.Cipher import AES
import base64
from django.http import JsonResponse

import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle

# @api_view(['GET'])
def get_encrypted_data(request):
    data = bytes('ala'.encode('utf-8'))
    key_text = ''.join([str(i)[1] if len(str(i)) == 2 else str(i) for i in range(16) ])[:16]
    key = bytes(key_text.encode())
    print(key)

    cipher = AES.new(key, AES.MODE_CBC, key)
    ct_bytes = cipher.encrypt(pad(data, 16))
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv':key_text, 'ciphertext':ct})
    print(result)

    return JsonResponse({"data" : str(base64.b64decode(ct)), 
        "key" : str(base64.b64decode(key_text)),
        "iv" : str(base64.b64decode(key_text))
        },
    safe=False)
    # return JsonResponse({"data" : 'test'})

if __name__ == "__main__":
    get_encrypted_data(None)
