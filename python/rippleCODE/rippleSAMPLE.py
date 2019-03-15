

class rippleSAMPLE:
  
  def __init__(loc, date, polLIST =[], ACC_RAD, collector, mode =False):
    """DEFINITION: rippleSAMPLE.__init__() creates a rippleSAMPLE() object storing the data of a sample taken. The object stores the location, date, name data, accuracy, collector of the data sample and assigns a unique ripple official sample number to it.
    
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
    self.date = date
    self.polLIST = polLIST
    self.ACC_RAD = ACC_RAD
    self.collector = collector
    if mode:
      self.mode = 'data sample'
    else:
      self.mode = 'test sample
      
 def setLoc(loc):
    """DEFINITION: sets the location of the sample
  
       Keyword arguments:
       loc -- a python TUPLE defining the location the same was taken of the form (LATITUDE, LONGITUDE)
    """
    self.loc = loc
    
 def getLoc():
    """DEFINITION: returns the location of the object
    
       Keyword returns:
       returns -- the location of the sample
    """
    return self.loc
 
 def setDate(date):
    """DEFINITION: sets the date the sample was collected on
  
       Keyword arguments:
       date -- an official date the sample was collected on for documentation purposes. Form "MM/DD/YYYY"
    """
    self.date = date
    
 def getDate():
    """DEFINITION: returns the date of the data sample
    
       Keyword returns:
       returns -- the date of sample collection
    """
    return self.date
  
 def addData(data):
    """DEFINITION: adds the data tuple (POLLUTANT, CONCENTRATION IN PPM) to the datalist.
       
       Keyword arguments:
       data -- (POLLUTANT, CONCENTRATION IN PPM) where pollutant is a string, and concentration is a float.
    """
    self.polLIST.append(data)
    
 def getDATA():
    """DEFINITION: returns the data in the sample
    
       Keyword returns:
       returns -- the data in sample collection
    """
    return self.polLIST
 
 def setAcc(acc):
    """DEFINITION: sets the accuracy radius of the sample
  
       Keyword arguments:
       acc -- a float representing the distance in meters around the sample it should be stored in the database as.
    """
    self.ACC_RAD= acc

 def getDATA():
    """DEFINITION: returns the accuracy radius of a sample
    
       Keyword returns:
       returns -- the accuracy radius of a sample in meters.
    """
    return self.ACC_RAD
  
 def getCollector():
    """DEFINITION: returns the collector of a sample
    
       Keyword returns:
       returns -- string, the collector of a sample.
    """
    return self.collector
  
 def getMode():
    """DEFINITION: returns the type of a sample
    
       Keyword returns:
       returns -- the type of a sample either test or actual.
    """
    return self.mode
    
 
 '''
 def getOfficialNumber():
 
 NOTE YOU CANNOT ERASE DATA
 NOTE YOU CANNOT CHANGE THE COLLECTOR
 NOTE YOU CANNOT CHANGE THE DATA MODE
 
 If you'd like to change these things please create a new sample...
    
 def verify():
 '''
