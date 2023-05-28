# Rainbow-Table-Generator-for-md5-hash
This repository contains a rainbow table generator for md5 hash. The generator creates a file called rainbowTable.txt in a folder named Files, which needs to be created in the same directory as the code files.

# Usage
To use the rainbow table generator, you need to call the computeTable function. Here is an example of how to use it:

`computeTable(passwordPolicy, minPasswordLength, maxPasswordLength)`

**Parameters:**
The computeTable function accepts the following parameters:

**passwordPolicy:** A single string representing the selected password policy. The available password policies are:

uppercase: Only uppercase letters are allowed.

lowercase: Only lowercase letters are allowed.

numeric: Only numeric digits are allowed.

alpha: Only alphabetic characters (both uppercase and lowercase) are allowed.

alphanumeric: Alphanumeric characters (uppercase, lowercase, and numeric) are allowed.


**minPasswordLength:** The minimum length of the password.

**maxPasswordLength:** The maximum length of the password.


# Requirements
Before using the rainbow table generator, make sure you have the following packages installed:

**pathlib:** You can install it by running pip install pathlib.

**hashlib:** You can install it by running pip install hashlib.

Please ensure that these packages are installed in your Python environment before executing the code.

# Contribution
Contributions to this repository are welcome. If you find any issues or want to add new features, please create a pull request or open an issue.

Thank you for using the Rainbow-Table-Generator-for-md5-hash repository!
