import math
path = "C:\\work\\Lab6\\"
inFile= open(path+'CityPop.csv')



class City:
    def __init__(self,header,line):
        for x in xrange(len(header)):
            setattr(self,header[x],line[x])
##        self.header = header
##        print self.header
            #print x
        #print line[1:]
## def __init__(self, cityName='n/a',label='n/a',yr2010=0):
##        self.city = cityName
##        self.label= label
##        self.yr2010=yr2010
##
    def printAttrib(self):
        print self.city+","+self.label+","+self.latitude+","+self.longitude

    def printDistance(self,othercity):
            lat1 = float(self.latitude)
            #check to see if long is a int and conver to float.
            lon1=float(self.longitude)
            
            # convert Lat and long for pt1 decimal degrees to radians
            lat1 = math.radians(lat1)
            lon1 = math.radians(lon1)

            # Point two
            # check to make sure it is a number
            lat2=float(othercity.latitude)
            # check long to make sure it is a number that can be converted to float
            lon2=float(othercity.longitude)

            # convert lat long for pt 2 to radians
            lat2 = math.radians(lat2)
            lon2 = math.radians(lon2)

            # s = sine and c = cos declare variables now to make calc easier to read.
            # take cos and sin of variables to make calculations
            s1=math.sin(lat1)
            s2=math.sin(lat2)
            c1=math.cos(lat1)
            c2=math.cos(lat2)
            cos=math.cos((lon1-lon2))

            # compute the angle between the points
            d =math.acos(s1*s2+c1*c2*cos)

            #compute the arc length and round the output to two decimal places.
            arcLength=(round((d*6.3e6)/1000,2))
            print arcLength 
###x=City(cityName='Klamath',cityLabel='Klamath Falls')
###print x.name,x.label 
##
Cities = []
header = (inFile.readline()).strip('\n')
header = header.split(',')
for row in inFile:
    #print row
    rowsplit=row.split(',')
    
##    city,label,yr2010=rowsplit[3],rowsplit[4],rowsplit[-1]
##    #print city
    city=City(header,rowsplit)
    Cities.append(city)

#print Cities

for city in Cities:
    city.printAttrib()

    city1="London"
    city2 = "London"
    if city=="London" in city:
        city1="London"
        city2="London"
        print 'yes'
    
    else: print 'no'
    #city.printDistance(city2)
    #print float(city.latitude)
Cities[0].printDistance(Cities[0])



