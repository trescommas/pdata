import simplejson
import urllib
import pymongo

def main():
    token = 'API token here'
    url = 'http://api.waqi.info/feed/hongkong/?token='+ token
    response = urllib.urlopen(url)
    result = simplejson.load(response)

    myDict ={}

    main = result['data']['aqi']

    updated_Time = result['data']['time']['s']

    myDict['time'] = updated_Time
    myDict['AQI'] = main

    pollutants = result['data']['iaqi']

    for chem in pollutants:
        value = result['data']['iaqi'][chem]['v']
        myDict[chem] = value

    MONGODB_URI = 'mongodb://url'
    client = pymongo.MongoClient(MONGODB_URI)
    db = client.get_default_database()
    songs = db['theData']
    things = songs.insert(myDict)
    client.close()
    print "Sucessfully updated"

if __name__ == '__main__':
    main()
