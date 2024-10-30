### 1.1: User Input Validation
Write a function that asks the user for a number. If the number is negative, raise a `ValueError` with a custom error message saying "Negative numbers are not allowed."

Next, add a try-except block so that the user is asked for a new number if the previous was not satisfactory.

---

### 1.2: Dictionary .get()
Write a function `get_value(d, key, backup_value=None)` that takes a dictionary `d`, `key` and a default value. This function should mimic the dictionary.get() without actually using .get()
- If the `key` does not exist in the dictionary, return the backup_value
- If the `key` does exist, return the d[key]

