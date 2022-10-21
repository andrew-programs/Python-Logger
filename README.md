## About aLogger.py ##
This is a simple logging script that can be used to help debug programs by giving you an easy way to create and append to logs. For each line added to the log, the then-active log file's name will be updated to the time the method was called. This script uses no modules outside of the standard library. 

## Getting Started ##
To get started, initialize the logger object while passing in a **folder directory**.<br />
`logger = Logger(desiredDirectory)`

## Object Methods ##

### Logging Low Importance ###
`logger.low(message)`<br />
The logger's low method will write to the current log with your message as low importance.

**Output to current log:**
> {currentDateTime} | LOW | {message}


### Logging Medium Importance ###
`logger.medium(message)`<br />
The logger's medium method will write to the current log with your message as medium importance.

**Output to current log:**
> {currentDateTime} | MEDIUM | {message}

### Logging High Importance ###
`logger.high(message)`<br />
The logger's high method will write to the current log with your message as high importance.

**Output to current log:**
> {currentDateTime} | HIGH | {message}

### Logging Custom Status ###
`logger.log(message, importance)`<br />
The logger's log method gives you the option to add a line to the log under any status such as WARNING or BUG. If left empty, it will not show importance.

**Output to current log after passing in importance:**
> {currentDateTime} | {importance} | {message}

**Output to current log without passing in importance:**
> {currentDateTime} | {message}
