# User-defined exception
class CustomError(Exception):
    pass
def risky_function():
    raise CustomError("This is a custom error message.")
try:
    risky_function()
except CustomError as e:    
    print(f"Caught a custom error: {e}")
