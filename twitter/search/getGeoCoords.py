import mechanize
import json

def getGeoCoords(address):
    addressList = address.split()
    formattedAdd = ""
    for i in range(len(addressList)-1):
        formattedAdd = formattedAdd + addressList[i] + '+'

    formattedAdd = formattedAdd + addressList[-1] + "&sensor=false"
    url = "http://maps.googleapis.com/maps/api/geocode/json?address=" + formattedAdd
    
    #calling mechanize to query the google maps api to get geo coords
    br = mechanize.Browser()
    br.set_handle_robots(False)
    geoText = br.open(url).read()
    geoDict = json.loads(geoText)
    results = (geoDict['results'][0])
    return [results['geometry']['location']['lat'],results['geometry']['location']['lng']]

if __name__=="__main__":
    address = "1211 Beacon St, Brookline, MA"
    geoText = (getGeoCoords(address))
    print(geoText)

    '''
    geoDict = json.loads(geoText)
    results = (geoDict['results'][0])
    print results['geometry']['location']
    '''
        
