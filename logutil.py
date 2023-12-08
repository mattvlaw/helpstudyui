import time

class logger:
    def __init__(self, path="log.txt", participant_id=0):
        self.logfile = path
        self.participant_id = participant_id

    def set_participant_id(self, pid):
        self.participant_id = pid
    def log(self, msg=None, ts=None):
        # if msg is none, it's a button press.
        # otherwise, it's help message
        if ts is None:
            ts = time.time()
        if msg is None:
            event = "button"
        else:
            event = "msg"
        with open(self.logfile, "a+") as outfile:
            outfile.write(f"{ts}, {self.participant_id}, {event}, {msg}\n")

        