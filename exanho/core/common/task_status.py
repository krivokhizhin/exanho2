import enum

class TaskStatus(enum.Enum):
    NEW = 1
    SCHEDULED = 2
    INPROCESS = 3
    DONE = 4
    ERROR = 5
    INTERRUPTED = 6