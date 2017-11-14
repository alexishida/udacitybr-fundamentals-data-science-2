import json
import requests


def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. The grader will supply the URL as an argument to
    # the function; you do not need to construct the address or call this
    # function in your grader submission.
    #
    # Once you've done this, return the name of the number 1 top artist in
    # Spain.

    data = requests.get(url).text
    data = json.loads(data)
    return data


api_key = 'api key'
api_url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&format=json&api_key='+api_key
api_dados = api_get_request(api_url)
print api_dados['topartists']['artist'][0]['name']