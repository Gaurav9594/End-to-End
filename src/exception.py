import sys
from src.logger import logging
def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    # exc_tb : Will tell us where the exception occured and in which line and what is the error
    # This will list all the details about the exception/ error details
    # Filename, lineno
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = (
                f"Error occurred in script [{file_name}] "
        f"at line number [{line_number}] with message: [{str(error)}]"
    )
    return error_message
    
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    # Inherits from the built-in Exception class.
    # Error detail is tracked by system (sys)
    def __str__(self):
        return self.error_message
    
# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#     except Exception as e:
#         logging.info("Divide by 0")
#         raise CustomException(e, sys)
    
# This special error will be printed in console and log