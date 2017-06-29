#!/usr/bin/python3

import requests
import json
robotURL='http://www.tuling123.com/openapi/api'

def robot(data):
    value=json.dumps(data)

    #requests.adapters.DEFAULT_RETRIES = 5
    result=requests.post(robotURL,value)
    return result.text

if __name__=='__main__':
    api={'key':'b7fa799b04e1485dacadba67091d74ce','info':'你好','userid':'abc12345'}
    print(robot(api))
