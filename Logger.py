import platform
from dataclasses import dataclass
from datetime import datetime
import os

@dataclass
class Logger:
    def __init__(self, directory: str):
        # Note for osSystem: Darwin is MacOS on M1 Chip
        self.osSystem = platform.system()
        self.osRelease = platform.release()
        self.osVersion = platform.version()

        assert directory != '', 'Please fill out directory'
        
        if self.osSystem == 'Darwin':
            self.separator = '/'
        elif self.osSystem == 'Linux':
            self.separator = '/'
        elif self.osSystem == 'Windows':
            self.separator = '\\'
        else:
            raise OSError(f'Sorry, {self.osSystem} is not supported.')
        
        self.directory = directory
        self.filePath = f'{directory}{self.separator}{datetime.now():%m-%d-%Y %H-%M-%S}.log'
        try:
            with open(f'{self.filePath}', 'x') as file:
                pass
        except FileExistsError:
            pass
            

    def log(self, message: str, importance: str=None) -> str:
        """
        This method allows you to append importance, timestamps, and logs to write a line to the currently active log file.

        Example
        -------
        >>> logger = Logger(directory)
            result = 2 + 2
            logger.log(f'Math completed, result = {result}', 'MEDIUM')
        
        Parameters
        ----------
        importance: str
            Allows the user to rate importance of new line to log. This can be left out if importance means nothing to you.
        """
        # Will attempt to append the currently active log with messages and importance. If it fails, returns string with exception.
        try:
            # Checks if importance has been provided and will append it to the message to create the line. If not given, it will not be included.
            assert message != None, 'message cannot be None'
            
            with open(f'{self.filePath}', 'a') as file:
                if importance is not None:
                    file.write(f'{datetime.now()} | {importance} | {message}\n')
                else:
                    file.write(f'{datetime.now()} | {message}\n')
            
            # Will attempt to rename file as each log happens so no mismatching of names/content.
            newPath = f'{self.directory}{self.separator}{datetime.now():%m-%d-%Y %H:%M:%S}.log'

            if self.filePath != newPath:
                os.rename(self.filePath, newPath)
                self.filePath = newPath
        except Exception:
            pass
    
    def low(self, message: str):
        """
        Allows you to append timestamps and log messages and output them to the currently active log file under low importance.

        Example
        -------
        >>> logger = Logger(directory)
            result = 2 + 2
            logger.low(f'Math completed, result = {result}')
        """
        try:
            # Checks if importance has been provided and will append it to the message to create the line. If not given, it will not be included.
            assert message != None, 'message cannot be None'
            
            with open(f'{self.filePath}', 'a') as file:
                file.write(f'{datetime.now()} | LOW | {message}\n')
            
            # Will rename file as each log happens so no mismatching of names/content and updates object's file_path.
            newPath = f'{self.directory}{self.separator}{datetime.now():%m-%d-%Y %H:%M:%S}.log'

            if self.filePath != newPath:
                os.rename(self.filePath, newPath)
                self.filePath = newPath
        except Exception:
            pass
        
    def medium(self, message: str):
        """
        Allows you to append timestamps and log messages and output them to the currently active log file under medium importance.

        Example
        -------
        >>> logger = Logger(directory)
            result = 2 + 2
            logger.medium(f'Math completed, result = {result}')
        """
        try:
            # Checks if importance has been provided and will append it to the message to create the line. If not given, it will not be included.
            assert message != None, 'message cannot be None'
            
            with open(f'{self.filePath}', 'a') as file:
                file.write(f'{datetime.now()} | MEDIUM | {message}\n')
            
            # Will rename file as each log happens so no mismatching of names/content and updates object's file_path.
            newPath = f'{self.directory}{self.separator}{datetime.now():%m-%d-%Y %H:%M:%S}.log'

            if self.filePath != newPath:
                os.rename(self.filePath, newPath)
                self.filePath = newPath
        except Exception:
            pass
    
    def high(self, message: str):
        """
        Allows you to append timestamps and log messages and output them to the currently active log file under high importance.

        Example
        -------
        >>> logger = Logger(directory)
            result = 2 + 2
            logger.high(f'Math completed, result = {result}')
        """
        try:
            # Checks if importance has been provided and will append it to the message to create the line. If not given, it will not be included.
            assert message != None, 'message cannot be None'
            
            with open(f'{self.filePath}', 'a') as file:
                file.write(f'{datetime.now()} | HIGH | {message}\n')
            
            # Will rename file as each log happens so no mismatching of names/content and updates object's file_path.
            newPath = f'{self.directory}{self.separator}{datetime.now():%m-%d-%Y %H:%M:%S}.log'

            if self.filePath != newPath:
                os.rename(self.filePath, newPath)
                self.filePath = newPath
        except Exception:
            pass
    
    def info(self, message: str):
        """
        This method allows you to append importance, timestamps, and logs to write a line to the currently active log file.

        Example
        -------
        >>> logger = Logger(directory)
            result = 2 + 2
            logger.info(f'Math completed, result = {result}')
        """
        # Will attempt to append the currently active log with messages and importance. If it fails, returns string with exception.
        try:
            # Checks if importance has been provided and will append it to the message to create the line. If not given, it will not be included.
            assert message != None, 'message cannot be None'
            
            with open(f'{self.filePath}', 'a') as file:
                file.write(f'{datetime.now()} | INFO | {message}\n')
            
            # Will attempt to rename file as each log happens so no mismatching of names/content.
            newPath = f'{self.directory}{self.separator}{datetime.now():%m-%d-%Y %H:%M:%S}.log'

            if self.filePath != newPath:
                os.rename(self.filePath, newPath)
                self.filePath = newPath
        except Exception:
            pass
