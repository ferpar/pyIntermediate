import sys
import logging

def error_handling():
    ## Never save to variables when raising an exeption: on error, this would cause a circular 
    ## reference, which would prevent the garbage collector from removing unused variables
    print(sys.exc_info()[2].tb_frame.f_code.co_filename)
    return ('{}. {}, filename: {}, line: {}'.format(sys.exc_info()[0],
                                      sys.exc_info()[1], 
                                      sys.exc_info()[2].tb_frame.f_code.co_filename,
                                      sys.exc_info()[2].tb_lineno))

try:
    a+b
except Exception as e:
    logging.error(error_handling())
