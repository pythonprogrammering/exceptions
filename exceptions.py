# 1. Demonstrating different types of errors
try:
    # SyntaxError
    # my_variable =? 123  # Uncomment to see SyntaxError in action

    # IndentationError
    #    a = 1  # Uncomment to see IndentationError in action

    # NameError
    print(b)  # Variable 'b' is not defined

    # IndexError
    l = [1, 2, 3]
    print(l[3])  # Index 3 is out of range

    # KeyError
    d = {"a": 1, "b": 2}
    print(d["c"])  # Key 'c' does not exist in dictionary

except NameError as e:
    print("Caught a NameError:", e)
except (IndexError, KeyError) as e:
    print("Caught an IndexError or KeyError:", e)
except Exception as e:
    print("Caught a general Exception:", e)

# 2. Manually raise an exception
try:
    raise SyntaxError("Incorrect syntax, pal!")  # Raise a SyntaxError manually
except SyntaxError as e:
    print("Caught a manually raised SyntaxError:", e)


# 3. Catching specific errors and multiple in one handler
def fetch_data():
    return {"name": "Kristian", "interests": "Python"}


# Try block is used when you know there’s a chance the code might not work as expected.
try:
    data = fetch_data()
    # Trying an operation that could raise a KeyError
    print(data["hobby"])  # Key 'hobby' does not exist
except (KeyError, TypeError) as e:
    # except is used to handle specific errors; for example, KeyError or TypeError here
    print("Caught KeyError or TypeError:", e)
else:
    # else: Executes if no exception occurs in the try block
    print("Data fetched successfully:", data)
finally:
    # finally: Always runs, used for cleanup like closing connections or unsubscribing from services
    print("Finished fetching process.")


# 4. Custom exceptions
class CustomError(Exception):
    """Custom exception for specific error handling."""

    pass


try:
    raise CustomError("This is a custom exception message!")
except CustomError as e:
    print("Caught CustomError:", e)

# Demonstrates:
# - SyntaxError, IndentationError, NameError, IndexError, KeyError
# - raise to manually raise an exception
# - try-except handling specific and multiple exceptions
# - else: if no error occurs
# - finally: for actions that run regardless of errors
