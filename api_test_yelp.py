#!/usr/bin/python

import json
import requests

#api-endpoint
api_base = "https://api.yelp.com/v3"

#headers for call

api_token = "G2pgq1NE1tCUhYyR7l248OFWc55g4cgUBQyd2xs98-TkIRtOaBBARm7K4JarvmqryANnTj_kR7MxbsFj6ea9plJbsFyh5Q5A9Jbap1CWa1lLX7NAObQgRdEnGOpOXXYx"

headers = { "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(api_token),
            "Accept": "application/json"}

def intro():
        print("Welcome to the Omega Restaurant Finder")

        
intro()

def search():

        user_city = input('Which City are you in?')
        c_parameters = "?location="+user_city
        c_endpoint = "{0}/businesses/search{1}".format(api_base,c_parameters)

        c_response = requests.get(c_endpoint,c_parameters,headers=headers)

        print(c_endpoint)
        print(c_response.text)


        if c_response.status_code == 200:
                c_json = (json.loads(c_response.content.decode("utf-8")))
                print("Connection made")
                print(c_json)
        elif c_response.status_code == (400 or 401):
                print("Connection not met")
                c_json = (json.loads(c_response.content.decode("utf-8")))
                print(c_json)
        else:
                return none

        camapignInfo = []
        
search()
                
              
def getStats():

        adID = input('Which Advertiser ID?')
        s_endpoint = "{0}v1/statistics".format(api_base)

        s_stats = {
                  "reportType": "CampaignPerformance",
                  "ignoreXDevice": "true",
                  "advertiserIds": adID,
                  "startDate": "2019-07-18T11:29:28.697Z",
                  "endDate": "2019-07-19T11:29:28.697Z",
                  "dimensions": [
                    "CampaignId"
                  ],
                  "metrics": [
                    "clicks"
                  ],
                  "format": "Csv",
                  "currency": "USD",
                  "timezone": "GMT"
                }

        s_response = requests.post(url=s_endpoint,headers=headers,data = s_stats)

        print(s_endpoint)
        print(s_response)


        if s_response.status_code == 200:
                s_json = (json.loads(s_response.content.decode("utf-8")))
                print("Connection made")
        elif s_response.status_code == (400 or 401):
                print(json.loads(s_response.content))
                print(s_stats)
                auth()
                getStats()
        else:
                print("Failed")

        camapignInfo = []
        
