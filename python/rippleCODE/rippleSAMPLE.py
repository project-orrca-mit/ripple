import datetime

class rippleSAMPLE:
  
 def __init__(self, loc, date, ACC_RAD, collector, polLIST =[], mode =False):
    """DEFINITION: rippleSAMPLE.__init__() creates a rippleSAMPLE() object storing the data of a sample taken. The object stores the location, date, name data, accuracy, collector of the data sample.
    
       Keyword arguments:
       loc -- a python TUPLE defining the location the same was taken of the form (LATITUDE, LONGITUDE)
       date -- an official date the sample was collected on for documentation purposes. Form "MM/DD/YYYY"
       polLIST -- a list of tuples, (POLLUTANT, CONCENTRATION IN PPM) where pollutant is a string, and concentration is a float. DEFAULTS TO EMPTY
       ACC_RAD -- a float containing the accuracy radius of the data. Determine an accurate RADIUS IN METERS for which the sample is applicable. 
       collector -- a STRING defining the organization who collected this data sample.
       mode -- a boolean value either True or False determining if this is an actual pollutant sample or simply a test sample. DEFAULTS TO FALSE.
       
       DISCLAIMER: In the interest of keeping samples robust, while we have implemented some functionality for getting and setting parameters, we've also implemented a VERIFY function, that will verify the data structure. You are also NOT ALLOWED to remove data, change the collector, or the sample type AFTER the object has been collected. For this please create a new sample. 
    """
    self.loc = loc
    #checking the date
    try:
        self.date = datetime.datetime.strptime(date, '%m/%d/%Y')
    except ValueError:
        print("ERROR: Invalid date entered, please enter in form MM/DD/YYYY")
    self.polLIST = polLIST
    self.ACC_RAD = ACC_RAD
    self.collector = collector
    if mode:
      self.mode = 'data sample'
    else:
      self.mode = 'test sample'
      
 def setLoc(self, loc):
    """DEFINITION: sets the location of the sample
  
       Keyword arguments:
       loc -- a python TUPLE defining the location the same was taken of the form (LATITUDE, LONGITUDE)
    """
    self.loc = loc
    
 def getLoc(self):
    """DEFINITION: returns the location of the object
    
       Keyword returns:
       returns -- the location of the sample
    """
    return self.loc
 
 def setDate(self, date):
    """DEFINITION: sets the date the sample was collected on
  
       Keyword arguments:
       date -- an official date the sample was collected on for documentation purposes. Form "MM/DD/YYYY"
    """
    self.date = date
    
 def getDate(self):
    """DEFINITION: returns the date of the data sample
    
       Keyword returns:
       returns -- the date of sample collection
    """
    return self.date
  
 def addData(self, data):
    """DEFINITION: adds the data tuple (POLLUTANT, CONCENTRATION IN PPM) to the datalist.
       
       Keyword arguments:
       data -- (POLLUTANT, CONCENTRATION IN PPM) where pollutant is a string, and concentration is a float.
    """
    self.polLIST.append(data)
    
 def getDATA(self):
    """DEFINITION: returns the data in the sample
    
       Keyword returns:
       returns -- the data in sample collection
    """
    return self.polLIST
 
 def setAcc(self, acc):
    """DEFINITION: sets the accuracy radius of the sample
  
       Keyword arguments:
       acc -- a float representing the distance in meters around the sample it should be stored in the database as.
    """
    self.ACC_RAD= acc

 def getDATA(self):
    """DEFINITION: returns the accuracy radius of a sample
    
       Keyword returns:
       returns -- the accuracy radius of a sample in meters.
    """
    return self.ACC_RAD
  
 def getCollector(self):
    """DEFINITION: returns the collector of a sample
    
       Keyword returns:
       returns -- string, the collector of a sample.
    """
    return self.collector
  
 def getMode(self):
    """DEFINITION: returns the type of a sample
    
       Keyword returns:
       returns -- the type of a sample either test or actual.
    """
    return self.mode
  
 def __str__(self):
    """DEFINITION: returns a valid string representing the sample. 
    
       Keyword returns:
       returns -- a vaild string to print the sample as text.
    """
    smpl = "Sample Data:\n\nCollector: " + self.collector + "\nLat/Lon: " + self.loc + "\nSamples: " + self.polLIST
    return smpl
  
 def verify(self):
    """DEFINTINION: verifies the contents of the data sample NOT FOR ACCURACY but for syntax, it ensures all the items are the correct type.
    
       Keyword returns:
       returns -- a boolean True or False if the data is valid...
    """
    passed = False
    tests_passed = 0
    tests = 7
    
    #checking for the location object
    if not(isinstance(self.loc[0], float)):
        print("ERROR: Warning, your LATITUDE is not a valid number!")
    else:
        tests_passed += 1
    if not(isinstance(self.loc[1], float)):
        print("ERROR: Warning, your LONGITUDE is not a valid number!")
    else:
        tests_passed += 1
    if not(isinstance(self.loc, tuple)):
        print("ERROR: Warning, your location is not a valid tuple, LATITUDE, LONGITUDE")
    else:
        tests_passed += 1
    if (-180 <= self.loc[0] <= 180):
        print("ERROR: Warning, your LATITUDE is NOT a valid LATITUDE inside the -180 to 180 range")
    else:
        tests_passed += 1
    if (-180 <= self.loc[1] <= 180):
        print("ERROR: Warning, your LONGITUDE is NOT a valid LONGITUDE inside the -180 to 180 range")
    else:
        tests_passed += 1
    
    #check the sample data formatting
    i = 0
    for sample in self.polLIST:
        if not(isinstance(sample[0], str)):
          print("ERROR: sample " + i + " does not have a valid pollutant name.")
          break
        else:
          i = i+1
        if not(isinstance(sample[1], float)):
          print("ERROR: sample " + i + " does not have a valid pollutant concentration as a float.")
          break
        else:
          i = i+1
    if (i+1) == len(self.polLIST):
        tests_passed += 1
    
    #check the ACC_RAD
    if not(isinstance(self.ACC_RAD, float)):
        print("ERROR: Warning, your ACC_RAD is not a valid number!")
    else:
        tests_passed += 1
    
    #we are not currently checking collector or MODE
    
    if tests_passed == tests:
        return True
    print("ERROR: " + tests_passed + " out of " + tests + " tests passed... check parameters.")
    return False
  
  
  
