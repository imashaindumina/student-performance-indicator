import sys
import logging
# We import logger here to test if both logger and exception work together
from src.logger import logging 

def error_message_detail(error, error_detail: sys):
    # exc_info() returns info about the current exception being handled
    _, _, exe_tb = error_detail.exc_info()
    
    # Extract the exact python filename where the error happened
    file_name = exe_tb.tb_frame.f_code.co_filename 
    
    # Format a clear error message with filename, line number, and error text
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exe_tb.tb_lineno, str(error)
    )
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Inherit the base exception class constructor
        super().__init__(error_message)
        
        # Get the detailed formatted error message using our function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    def __str__(self):
        # Return the detailed error message when converted to string
        return self.error_message

