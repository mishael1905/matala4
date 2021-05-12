import json
import requests
def dis_test():
    counter=0
    handle= open('C:\dests.txt', 'r',  encoding='utf-8')
    diconery = dict()
    max1=max2=max3=0
    for line in handle:
        url1="https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=%D7%AA%D7%9C%25%D7%90%D7%91%D7%99%D7%91&"
        dest1="destinations="+line
        key1="&key=AIzaSyBpzuvBgx7-6G3rpKnVu6fjkDMiPI35okA" 
        response = requests.get(url1+dest1+key1)
        res= response.content.decode('utf-8')
        thelist = json.dumps(res)
        x=thelist.find("value")
        dist_in_km=int(thelist[x+9:x+17])/1000
        x= thelist.find("text",x,)
        if counter==0:
            duration=thelist[x+11:x+26]
        else:
            duration=thelist[x+11:x+25]
        url2="https://maps.googleapis.com/maps/api/geocode/json?address="
        lng_lat= line
        key2="&key=AIzaSyBpzuvBgx7-6G3rpKnVu6fjkDMiPI35okA"   
        response = requests.get(url2+lng_lat+key2)
        response= response.content.decode('utf-8')
        locstart=response.find('location')
        lat=response[locstart+37:locstart+47]
        lng=response[locstart+72:locstart+85]
        counter=counter+1
        diconery[line]={'distance': dist_in_km,'duration': duration.rstrip(),'latitude': lat,'longitude':lng.rstrip()}  
        if dist_in_km>max1:
            max3=max2
            max2=max1
            max1= dist_in_km
        elif dist_in_km>max2:
            max3=max2
            max2=dist_in_km
        elif dist_in_km>max3:
            max3=dist_in_km            
    for line in diconery:
        print(line, diconery[line])
        
    print('max1:',max1,'max2:',max2,'max3:',max3)