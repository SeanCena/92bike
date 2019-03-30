from urllib import request
from urllib import parse
import json


def HttpGet(url, values, outputFormat='json'):
    contents = request.urlopen(url + outputFormat + '?' + parse.urlencode(values)).read().decode('utf-8')
    return json.loads(contents)


# https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood&key=AIzaSyCQNdg3K1bKweoQ_2GAJrbHJ80eGD1gs7c
# API_KEY = 'AIzaSyCQNdg3K1bKweoQ_2GAJrbHJ80eGD1gs7c'
#
# origin = 'Disneyland'
# destination = 'Universal+Studios+Hollywood'
#
# outputFormat = 'json'
# mode = 'bicycling'
# region = 'us'
#
# base_url = 'https://maps.googleapis.com/maps/api/directions/'
# values = {'key': API_KEY,
#          'origin': origin,
#          'destination': destination,
#          'mode': mode,
#          'region': region }
#
# contents = HttpGet(base_url, values, outputFormat)
