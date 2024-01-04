from dataclasses import dataclass


@dataclass
class Contest:

    """
    Model class for the Contest object. To-be deserialized by the api call
    @contest.list

    <Optional> reports fields that can be absent.

    Enums are to be Tuple defined (due to immutability)
    """

    id: int
    name: str = "Contest"
    type = (CF, IOI, ICPC)
    phase = (BEFORE, CODING, PENDING_SYSTEM_TEST, SYSTEM_TEST, FINISHED)
    frozen: bool
    durationSeconds: int
    startTimeSeconds: int  # Unix Format Start Time <Optional>
    relativeTimeSeconds: int  # Can be negative <Optional>
    preparedBy: str  # <Optional>
    websiteUrl: str  # <Optional>
    description: str  # <Optional>
    difficulty: int  # <Optional> From 1 to 5. Increasing difficulty

    kind: str  # <Optional>

    """ @kind -> Official ICPC Contest, Official School Contest, Opencup Contest, School/University/City/Region Championship, Training Camp Contest, Official International Personal Contest, Training Contest.
    """

    icpcRegion: str  # Region for official ICPC contests. <Optional>
    country: str  # <Optional>
    city: str  # <Optional>
    season: str  # <Optional>
