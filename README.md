### Purpose

The script logger.py is a logging utility written in Python 2.7 which logs  
messages with a priority flag and time stamp and returns messages  
for reading in priority flag and timestamp descending order.


### Requirements

No external or third-party packages are required to run the script.  The logger  
makes use of the following Python Standard Library modules:  

>Queue  
>datetime  
>time  
>calendar  
>threading  

As such, only a Python environment is required to run logger.py.


### Description

The script makes use of the Python Queue base class, specifically its  
PriorityQueue implementation, due to its multi-threading support.  

Script functionality revolves around two distinct classes which separate  
the logging and reading functions:  

>Logger  
>LogReader

The Logger class is responsible for logging messages.  As it does so,  
it checks for user-specified size-constraints/limitations and assigns a default  
priority flag for incoming messages, if none are specified (defaulting to highest  
priority).  Warnings are raised if the log queue size approaches a critical (user  
specificable limit) and no logs are accepted after capacity is reached.  

The LogReader class fetches the log information (equivalent to popping) and  
formats the time stamp to display in human-readable form from the original  
capture of epoch-time.  


### Usage

The script seeds the log data with some pre-set sample messages and  
priority flags.  In addition, several threads are used in order to populate/  
write to the log.  

Salient user-specifiable constants are:

MAX_RECS - the maximum number of log records to queue  
MAX_WARN - capacity percentage after which size warnings should be raised  
NUM_THREADS - number of threads to spawn for writing to the log  

Log messages may be written using the log method of the Logger object.  
Messages must include at least the message content and, optionally,  
a priority flag as follows:

```
Logger.log(flag,msg)
```

Sample instantiation and usage included in the script are as follows:

```
logger = Logger()
logger.log(1,"this is a message")

```

Log messages may be read individually using:

```
LogReader.get()  
```

or the entire log may be read using:

```
LogReader.readAll()
```


The script and its sample data may simply be invoked by running:

```
logger.py
```

at the command line for Python-supported environments.  

