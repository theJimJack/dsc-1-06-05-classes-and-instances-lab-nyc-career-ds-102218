#Big Takeaways
    #Global variables = variables that could be standard across all classes/instances (i.e. how to greet customers)
    #Class variables = variables that are consistent across all instances (i.e. standard ice cream flavors)
    #Instance variables = variables that are specific to an instance (i.e. address, franchise owner's name)
    #INIT stuff
        #wrapping data in functions
    #class variable; we want each instance of this class to have this .location attribute

greeting = "Hello"
class IceCreamShop():
    something_here = 'something' #class variable
    # print (greeting)
    kindness = "you_are_nice" #this is a class variable, can be accessed by "IceCreamShop.kindness" (ie on the class)
    # print(kindness) #prints kindness string on startup
    # def __init__(self, name):
    #     self._name = name
    #     self.kindness = "you_are_nice"

    def start_goodbye(self):
        self.goodbye= 'ciao' #assigns .goodbye value

    def say_goodbye(self):
        print(self.goodbye) #prints goodbye as well. (duplicative of .goodbye)

    def say_something(self):
        print(greeting)

    def say_kindness(self):
        print(kindness) #NB -- kindness is a class variable that is referenced when the instance references this method


tcby = IceCreamShop()
# tcby.name()
tcby.kindness
# vars(tcby)



class AmpleHills():
    def __init__(self, location):
        #reject
        #coerce
        #{'address':"", "zip": integer}
        #shows how __init__ can be used for data validation
        self.validate_location(location)
        self._location = location

    def validate_location(self,location): #referenced whenever the location is changed
        if not isinstance(location, dict):
            raise('must be a dictionary')

    @property #decorator -- pass the method below to the property method  and assign result to the name of the function
    def location(self); #get_location
        return 'zip code is equal to {zipcode}'.format(zipcode = self._location['zip'])

    # location = property(get_location) #made redundant by @property object

    @location.setter
    def location(self, location): #set_location; location references property variable 'location' and sets setter function
        self.validate_location(location)
        self._location = location

    #location = location.setter(set_location) #tags the set_location function as the setter; made redundant by @location.setter

Example:
manhattan = AmpleHills({'zip':10001})
manhattan.location
    #returns --> 'zip code is equal to 10001'
manhattan.location = {'zip':10002}
manhattan.location
    #returns --> 'zip code is equal to 10002'
