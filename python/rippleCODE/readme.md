# here is the description

### Essentiall RIPPLECODE is a python library that allows python-controlled robots to DIRECTLY WRITE ripple database files, decode these files, get data from these files, etc. It is used to interface ROBOTS with the ripple online database.

rippleREAD - will take the input of ripple files and provide a repository to read them in terminal/etc 

rippleWRITE - will take the inputed data and location and created .rpl files (just.txt files or JSON files) and contains methods to edit/manipulate them

<<ALSO HAS A **CAUTION DATA HAS BEEN CHANGED** flag every time you edit data, it does NOT DELETE OLD DATA it creates a strikthrough>>

rippleCONVERT - converts traditional data formats to rpl, converts rpl to traditional data formats 

## Structure of Package
      /rippleCODE

            __init.py__
      
            rippleREAD.py
      
            rippleWRITE.py
      
            rippleCONVERT.py
      
            readme.md
      
            setup.py
            
            LICENSE (MIT)
            
            /samples
                  
                  example.rpl

