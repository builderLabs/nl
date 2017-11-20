from Queue import PriorityQueue                       # Python Queue class supports multi-threading

import datetime
from calendar import timegm
from time import gmtime, sleep
from threading import Thread, current_thread


class Logger(PriorityQueue):

    def log(self, *args, **kwargs):
        # exercise size-management
        if self.full():
            return "Maximum allowed records posted to log."

        if MAX_RECS > 0:
            current = (self._qsize() * 1.0) / self.maxsize
            if current >= MAX_WARN:
                print "Warning - approaching log capacity limit at: " + str(current) + "..."

        if len(args) < 1:
            return "Please provide a record/message to log."

        rnk = 5              # top-priority rank assigned by default
        if len(args) > 1:
            rnk = args[0]
            msg = args[1]
        else:
            msg = args[0]
  
        # shorthand of *-1 to facilitate time desc order return
        self.put((1.0 / rnk, timegm(gmtime()) * -1, msg))
        # enforce 1-second sleep to test timestamp-order retrieval
        sleep(1)


class LogReader():

    def get(self):
        print logger.title
        if not logger.empty():
            rec = logger.get()
            return str(int(1 / rec[0])) + " - " + datetime.datetime.fromtimestamp(rec[1] * -1).strftime('%Y-%m-%d %H:%M:%S => ') + rec[2]        
        return "Log records exhausted."     # optional error-handling: raise KeyError

    def readAll(self):
        print logger.title
        while not logger.empty():
            rec = logger.get()
            print str(int(1 / rec[0])) + " - " + datetime.datetime.fromtimestamp(rec[1] * -1).strftime('%Y-%m-%d %H:%M:%S => ') + rec[2]




# --- testing -------------------------------------------------------

# max recs  in our queue to control for memory (0 means infinite/no limit)
MAX_RECS = 50
MAX_WARN = 0.8         # warn when our queue is this full
NUM_THREADS = 2

logger = Logger()
logger.maxsize = MAX_RECS
logger.title = "\nPRIORITY | TIMESTAMP | MESSAGE"
logReader = LogReader()


# test no record/message case:
print logger.log()                         # should return error msg

# test manual entry:
logger.log(1, "low priority msg")

# seed some more log data:
messages = [["default high priority msg"], [5, "high priority msg"], [1, "abc"], [
    2, "def"], [2, "ghi"], [3, "jkl"], [1, "mno"], [1, "pqr"], [3, "stu"], [2, "vwx"]]

# log using several threads ( using thread-safe Queue base class )
for msg in messages:
    for thr in range(NUM_THREADS):
        runner = Thread(target=logger.log, args=msg)
        runner.start()
        sleep(1)     # to illustrate timestamp-based prioritization


# read some individual lines in priority-timestamp order (both desc)
print "\nReading some lines individually:\n"
print logReader.get()
print logReader.get()

# read all remaining  messages at once
print "\nReading remainder of log queue...\n"
logReader.readAll()
