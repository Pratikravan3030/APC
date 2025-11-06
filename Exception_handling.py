# exception handling
try:
    # code that may raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"Result: {result}")
finally:
    print("Execution completed.")


