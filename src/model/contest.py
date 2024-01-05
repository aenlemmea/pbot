from dataclasses import dataclass


@dataclass(init=False)
class Contest:

    """
    Model class for the Contest object. To-be deserialized by the api call
    @contest.list

    <Optional> reports fields that can be absent.

    Enums are to be Tuple defined (due to immutability). We are not using enum.ENUM since it is pointless for such a small use case.
    """

    id: int
    name: str = "Contest"
    type: str
    phase: str
    frozen: bool
    durationSeconds: int
    startTimeSeconds: int  # Unix Format Start Time <Optional>
    relativeTimeSeconds: int  # Can be negative <Optional>

    # TODO: Figure out how to deal with these optionals with the default constructor
    # Cannot use a custom constructor due to availing data class features.

    # preparedBy: str  # <Optional>
    # websiteUrl: str  # <Optional>
    # description: str  # <Optional>
    # difficulty: int  # <Optional> From 1 to 5. Increasing difficulty

    # kind: str  # <Optional>

    # """ @kind -> Official ICPC Contest, Official School Contest, Opencup Contest, School/University/City/Region Championship, Training Camp Contest, Official International Personal Contest, Training Contest.
    # """

    # icpcRegion: str  # Region for official ICPC contests. <Optional>
    # country: str  # <Optional>
    # city: str  # <Optional>
    # season: str  # <Optional>

    # Set dataclass arg for init to False to use the below constructor.

    def __init__(
        self,
        id,
        name,
        type,
        phase,
        frozen,
        durationSeconds,
        startTimeSeconds,
        relativeTimeSeconds,
    ):
        self.id = id
        self.name = name
        self.type = type if type in ("CF", "IOI", "ICPC") else "CF"
        self.phase = (
            phase
            if phase
            in (
                "BEFORE",
                "CODING",
                "PENDING_SYSTEM_TEST",
                "SYSTEM_TEST",
                "FINISHED",
            )
            else "FINISHED"
        )
        self.frozen = frozen
        self.durationSeconds = durationSeconds
        self.startTimeSeconds = startTimeSeconds
        self.relativeTimeSeconds = relativeTimeSeconds

    # @staticmethod
    # def from_json(json_obj):
    #     return Contest(json_obj['id'],
    #     json_obj['name'], json_obj['type']
    #     ,json_obj['phase'], json_obj['frozen']
    #     ,json_obj['durationSeconds'], json_obj['startTimeSeconds'], json_obj['relativeTimeSeconds'])

    """
    TODO :: ISSUE

        Because with how the api sends the json data and the number of optional fields,
        it makes little sense to have all the parameters available for deserialization. 
        BUT this also means that if some contest data does contain additional objects, 
        we will miss out on it due to it being not available during deserialization.

        Fix ideas: Have variadic parameter (does python support it?) or use parameter unpacking to deal with it.

        We don't benefit from it however since the embed to be built on so many parameters is meaningless.
    """
