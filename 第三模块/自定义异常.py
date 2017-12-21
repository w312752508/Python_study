class ZhhException(Exception):
    def __init__(self,mes):
        self.message = mes
    def __str__(self):
        return self.message
try:
    raise ZhhException("30")
except ZhhException as e :
    print (e)

