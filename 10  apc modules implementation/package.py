from mypackage import module1

# Directory structure:
# mypackage/
#   __init__.py
#   module1.py
# package.py

# --- mypackage/module1.py ---
def greet(name):
    return f"Hello, {name}!"

# --- package.py ---



print(module1.greet("Ishaan"))