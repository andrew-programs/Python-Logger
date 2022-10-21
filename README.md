## About aLogger.py ##
This is a simple logging script that can be used to help debug programs by giving you an easy way to create and append to logs.

## Getting Started ##
To get started, initialize the object while passing in a **folder directory**.
`logger = Logger(desiredDirectory)`

## Object Methods ##

#### Logging Low Importance ####
`logger.low(message)`
This will write to the current log your message as low importance.

**Output to current log:**
> {currentDateTime} | LOW | {message}


#### Logging Medium Importance ####
`logger.medium(message)`
This will write to the current log your message as medium importance.

**Output to current log:**
> {currentDateTime} | MEDIUM | {message}

#### Logging High Importance ####
`logger.high(message)`
This will write to the current log your message as high importance.

**Output to current log:**
> {currentDateTime} | HIGH | {message}

#### Logging Custom Status ####
`logger.log(message, importance)`
This gives you the option to add a line to the log under any status such as WARNING or BUG. If left empty, it will not show importance.

**Output to current log after passing in importance:**
> {currentDateTime} | {importance} | {message}

**Output to current log without passing in importance:**
> {currentDateTime} | {message}