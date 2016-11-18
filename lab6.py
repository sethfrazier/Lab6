import math

class City:
    
    def __init__(self,city,label,latitude,longitude,yr1970,yr1975,\
                 yr1980,yr1985,yr1990,yr1995,yr2000,yr2005,yr2010):
        #self.idnum=idnum
        self.city=city
        self.label=label
        self.latitude=latitude
        self.longitude=longitude
        self.yr1970=yr1970
        self.yr1975=yr1975
        self.yr1980=yr1980
        self.yr1985=yr1985
        self.yr1990=yr1990
        self.yr1995=yr1995
        self.yr2000=yr2000
        self.yr2005=yr2005
        self.yr2010=yr2010
        
    def printAttrib(self):
        print self.city+","+self.label+","+self.latitude+","+self.longitude+","\
              +yr1970+","+yr1975+","+yr1980+","+yr1985+","+yr1990+","+yr1995+","\
              +yr2000+","+yr2005+","+yr2010

    def printDistance(self,othercity):
        try:
            # point one-self lat and lon
            # check to see if lat and long is a number and convert to float.
            # convert Lat and long for pt1 decimal degrees to radians
            lat1 = float(self.latitude)
            lon1=float(self.longitude)
            lat1 = math.radians(lat1)
            lon1 = math.radians(lon1)

            # Point two- othercity input lat and lon 
            # check to see if lat and long is a number and convert to float.
            # convert Lat and long for pt1 decimal degrees to radians
            lat2=float(othercity.latitude)
            lon2=float(othercity.longitude)
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
            format='Distance between %s and %s is %.2f km'
            values=(self.label, othercity.label,arcLength)
            print format % values
        except: print "there is an error in one of the points latitude \
                        or longitude, please check latitude and longitude \
                        of point"
    def printPopChange(self,year1,year2):
        year1=float(year1)
        year2=float(year2)
        print 'population change for',city.label,'is', year2-year1
        
#try:
path = "C:\\work\\Lab6\\"
inFile= open(path+'CityPop.csv')

        
Cities = []
header = (inFile.readline())
#header = header.split(',')
for row in inFile:
    print row
    row=row.strip('/n')
    print row
    rowsplit=row.split(',')
    city=rowsplit[3]
    label=rowsplit[4]
    latitude=rowsplit[1]
    longitude=rowsplit[2]
    yr1970=rowsplit[5]
    yr1975=rowsplit[6]
    yr1980=rowsplit[7]
    yr1985=rowsplit[8]
    yr1990=rowsplit[9]
    yr1995=rowsplit[10]
    yr2000=rowsplit[11]
    yr2005=rowsplit[12]
    yr2010=rowsplit[13]

##    #print city
    #city=City(header,rowsplit)
    city=City(city,label,latitude,longitude,yr1970,yr1975,yr1980,yr1985,\
              yr1990,yr1995,yr2000,yr2005,yr2010)
    Cities.append(city)    

inFile.close()
try:
    for city in Cities:
        city.printAttrib()

    Cities[50].printDistance(Cities[4])
except: print "one of the cities is not found please try again"

try:
    for city in Cities:
        city.printPopChange(city.yr1980,city.yr1985)
except: print 'On of the years is not found, please try again'

city
#except:
#    print 'File not Found'


