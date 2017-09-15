from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
import geocoder , json
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def nearestDHL(request):
    '''
    #######   Select the service you require
    ## OPTION 1. Need to send a parcel and don't have a DHL account?
    ## OPTION 2. Are you a DHL account holder with a parcel to send?
    ## OPTION 3. Did we miss you? Find stores that offer parcel collection
    ## OPTION 4. Do you have a parcel to return via DHL?
    ######  Pass the option of the servise as string containing an the number option like '1'
    ######  Pass the postal code as the second parameter in url
    '''
    print ('entered')
    # lat = request.GET.get("lat")
    # lon = request.GET.get("lon")
    zipcode = request.GET.get("zipcode")
    optionSelected = request.GET.get("optionSelected")
    # x = json.loads(request.body)
    # lat = x['lat']
    # lon = x['lon']
    # optionSelected = x['optionSelected']

    # (print) 'get parameters stored'
    # ## add the x y coordinates of the input 
    # g = geocoder.google([lat,lon] , method ='reverse')
    # # (print) g.json
    # (print) g.json
    # zip = str(g.json['postal'])
    print (zipcode)
    # optionSelected = "1"
    url = "http://parcel.dhl.co.uk/dhl-service-point/find-your-nearest/?gomap=1&option=" + str(optionSelected) + "&postcode=" + str(zipcode)

    r = requests.get(url)
    # browser = webdriver.Firefox()
    # browser.get(url)
    # r = browser.page_source

    soup = bs(r.text,"html.parser")

    try:
        ## address of the nearest DHL
        address = soup.findAll("div", { "class" : "info-address-content" })[0]
        a =  str(address.text)


        ## contactDetails of the nearest DHL
        contactDetails = soup.findAll("div", { "class" : "info-phone-content" })[0]
        b = str(contactDetails.text)

        ## distance of the nearest DHL
        distance = soup.findAll("div", { "class" : "info-distance-content" })[0]
        c =  str(distance.text)

        box = {'contactDetails':b,'address':a,'distance':c} 
        
        jsonResponse=json.dumps(box,indent=4)
        # return HttpResponse(box)
        return HttpResponse(jsonResponse,content_type="application/json")

    except: 
        return HttpResponse('No DHL near you')




def track(request):
    # url = "http://139.59.40.238:88/trackShipment?TrackingNo=5520188122"
    # r = requests.get(url)
    # context_dict = {}
    # context_dict['r'] = r
    return render(request,'app/track.html')





