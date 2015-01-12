""" Sends POST requests to the server
"""

import doormon.config as config

import requests

endpoint = config.endpoint

def send_message(state):
    print "Sending %s" % state
    successes = []
    for api_key in config.api_keys:
        success = True
        params = {
                'api_key': api_key,
                'state': state,
                'video_uri': config.webcam
                }
        r = requests.post(endpoint, data=params)

        if r.json.get('success') is not True:
            success = False
        result = r.json.get('result')
        if result is None:
            success = False
        if result.get('success') != 1:
            success = False
        successes.append(success)
    return successes
