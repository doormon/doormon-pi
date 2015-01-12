import ConfigParser

configParser = ConfigParser.RawConfigParser()
configParser.read("doormon.cfg")

api_keys = configParser.get('doormon', 'apikeys').split(',')
endpoint = configParser.get('doormon', 'endpoint')
webcam = configParser.get('doormon', 'webcam')
