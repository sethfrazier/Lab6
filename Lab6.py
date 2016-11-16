
path = "C:\\work\\Lab6\\"
inFile= open(path+'CityPop.csv')

class City:
    def __init__(self, city='n/a',label='n/a'):
        self.city = city
        self.label= label

    def __repr__(self):
        return self.city
        return self.label
                
#x=City(cityName='Klamath',cityLabel='Klamath Falls')
#print x.name,x.label 

Cities = []

for row in inFile:
    print row
    city=City()
    Cities.append(city)

for city in Cities:
    print city
'''class City():

    __init__(self, . . .):

    # rest of class definition



for row in csv_rows:

    city = City()

    Cities.append(city) '''

