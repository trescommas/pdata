import simplejson
import urllib
import pymongo

def main():
    token = 'dde134b116d76f3eac813a3164c312ab76d51815'
    url = 'http://api.waqi.info/feed/hongkong/?token=' + token
    response = urllib.urlopen(url)
    result = simplejson.load(response)

    myDict ={}

    main = result['data']['aqi']
    time = ''
    updated_Time = result['data']['time']['s']
    if (time != updated_Time):
        time = updated_Time


        myDict['Time Updated'] = time
        myDict['AQI'] = main

        pollutants = result['data']['iaqi']

        for chem in pollutants:
            value = result['data']['iaqi'][chem]['v']
            myDict[chem] = value

        MONGODB_URI = 'mongodb://abhs:abhs@ds117829.mlab.com:17829/airpoll'
        client = pymongo.MongoClient(MONGODB_URI)
        db = client.get_default_database()
        songs = db['theData']
        things = songs.insert(myDict)
        client.close()
        print "Sucessfully updated"
    else:
        print "Time is same"

if __name__ == '__main__':
    main()
