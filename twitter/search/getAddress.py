import mechanize
import json

#takes list containing [lat, lng]
def getAverageCoords(boundCoords):
	lat = 0.0
	lng = 0.0
	for i in range(len(boundCoords)):
		lat = lat + boundCoords[i][0]
		lng = lng + boundCoords[i][1]
	lat = lat / 4.0
	lng = lng / 4.0
	return [lng, lat]


def get(geoCoords):
	reqStr = "http://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(geoCoords[0]) +','+ str(geoCoords[1])+"&sensor=true"
	

	#calling mechanize to query the google maps api to get geo coords
	br = mechanize.Browser()
	br.set_handle_robots(False)
	addText = br.open(reqStr).read()
	addDict = json.loads(addText)
	try:	
		results = (addDict['results'][0])
	except:
		results = None

	return results

def getCity(address):
	return address['address_components'][2]['long_name']

def getFullAddress(address):
	return address['formatted_address']

def main():
	g = [42.3433181,-71.1165203]
	address = get(g)
	print(getCity(address))
	print(getFullAddress(address))



if __name__=="__main__": main()
