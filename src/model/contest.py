from dataclasses import dataclass

@dataclass
class Contest:

    '''
    Model class for the Contest object. To-be deserialized by the api call
    @contest.list 

    <Optional> reports fields that can be absent.

    Enums are to be Tuple defined (due to immutability) 
    '''

    id : int = 1
    name : str = ""
    type = (CF, IOI, ICPC)
    phase = (BEFORE, CODING, PENDING_SYSTEM_TEST, SYSTEM_TEST, FINISHED)
    frozen : bool = True
    durationSeconds : int = 120 * 60
    startTimeSeconds : int = 2403390598 # Unix Format Start Time <Optional>
    relativeTimeSeconds : int = 34354654 # Can be negative <Optional>
    preparedBy : str = "rui" # <Optional>
    websiteUrl : str = "www.holaforces.com" # <Optional>
    description : str = "Local" # <Optional>
    difficulty : int = 1 # <Optional> From 1 to 5. Increasing difficulty
    
    kind : str = "" # <Optional> 
    
    ''' @kind -> Official ICPC Contest, Official School Contest, Opencup Contest, School/University/City/Region Championship, Training Camp Contest, Official International Personal Contest, Training Contest.
    '''

    icpcRegion : str = "" # Region for official ICPC contests. <Optional>
    country : str = "India" # <Optional>
    city : str = "Bagdogra" # <Optional>
    season : str = "idk" # <Optional>
