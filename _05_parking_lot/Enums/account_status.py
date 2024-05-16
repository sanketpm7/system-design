from enum import Enum

class AccountStatus(Enum):
    ACTIVE      = 1
    BLOCKED     = 2
    BANNED      = 3
    COMPROMISED = 4
    ARCHIEVED   = 5
    UNKNOWN     = 6