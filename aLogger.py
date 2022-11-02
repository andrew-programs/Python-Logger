from platform import system
from datetime import datetime
from os import rename

class Logger:
    def __init__(self, directory: str):
        if directory.endswith('/') or directory.endswith('\\'):
            self.directory = directory[:-1]
        else:
            self.directory = directory
        
        osName = system()
        
        # Checks if OS is either MacOS, Windows, or Linux and generates a separator.
        if osName == 'Darwin' or osName == 'Linux':
            self.separator = '/'
        elif osName == 'Windows':
            self.separator = '\\'
        else:
            raise OSError(f'Sorry, {osName} is not supported.')
        
        self.filePath = f'{self.directory}{self.separator}{datetime.now():%m-%d-%Y %H-%M-%S}.log'
        
        # Creates log file.
        try:
            with open(f'{self.filePath}', 'x') as file:
                pass
        except FileExistsError:
            raise FileExistsError('For some reason, this file already exists')

    # Creates a new line in current log as any importance passed into the method.
    def log(self, message: str, importance: str=None) -> None:
        """Creates a new line in current log as any importance passed into the method."""
        
        assert message != None, 'message cannot be None'

        # Attempts to append the currently active log with messages and importance. If it fails, returns string with exception.
        try:
            # Creates a new line in current log and renames log to current datetime.
            with open(f'{self.filePath}', 'a') as file:
                if importance == None:
                    file.write(f'{datetime.now()} | {message}\n')
                else:
                    file.write(f'{datetime.now()} | {importance} | {message}\n')
                self.__renameLog()
        
        except Exception as exception:
            print(f'Could not print to log due to exception : {exception}')
    
    # Creates a new line in current log as low importance.
    def low(self, message: str) -> None:
        """Creates a new line in current log as low importance."""
        
        assert message != None, 'message cannot be None'
        
        # Attempts to append the currently active log with messages and importance. If it fails, prints exception.
        try:
            # Logs message in current log and renames log to current datetime.
            with open(f'{self.filePath}', 'a') as file:
                file.write(f'{datetime.now()} | LOW | {message}\n')
                self.__renameLog()

        except Exception as exception:
            print(f'Could not print to log due to exception : {exception}')
    
    # Creates a new line in current log as medium importance.
    def medium(self, message: str) -> None:
        """Creates a new line in current log as medium importance."""
        
        assert message != None, 'message cannot be None'

        # Attempts to append the currently active log with messages and importance. If it fails, prints exception.
        try:
            # Logs message in current log and renames log to current datetime
            with open(f'{self.filePath}', 'a') as file:
                file.write(f'{datetime.now()} | MEDIUM | {message}\n')
                self.__renameLog()
            
        except Exception as exception:
            print(f'Could not print to log due to exception : {exception}')
    
    # Creates a new line in current log as high importance.
    def high(self, message: str) -> None:
        """Creates a new line in current log as high importance."""
        
        assert message != None, 'message cannot be None'

        # Attempts to append the currently active log with messages and importance. If it fails, prints exception.
        try:
            # Logs message in current log and renames log to current datetime
            with open(f'{self.filePath}', 'a') as file:
                file.write(f'{datetime.now()} | HIGH | {message}\n')
                self.__renameLog()
    
        except Exception as exception:
            print(f'Could not print to log due to exception : {exception}')
    
    # Creates a new line in current log as information.
    def info(self, message: str) -> None:
        """Creates a new line in current log as information."""
        
        assert message != None, 'message cannot be None'

        # Attempts to append the currently active log with messages and importance. If it fails, returns string with exception.
        try:
            # Logs message in current log and renames log to current datetime
            with open(f'{self.filePath}', 'a') as file:
                file.write(f'{datetime.now()} | INFO | {message}\n')
                self.__renameLog()

        except Exception as exception:
            print(f'Could not print to log due to exception : {exception}')
    
    # Renames current log file.
    def __renameLog(self) -> None:
        """Method that renames the current log, please only use this if you have some idea of what you're doing."""
        
        # Creates new path to file
        newPath = f'{self.directory}{self.separator}{datetime.now():%m-%d-%Y %H-%M-%S}.log'
        
        # Checks if current file path is the same as new file path and renames if not.
        if self.filePath != newPath:
            rename(self.filePath, newPath)
            self.filePath = newPath