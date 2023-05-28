from hashlib import md5
from itertools import product
import pathlib
import json

def generateHash_md5(password):
    "function to generate md5 hashes"
    return md5(password.encode()).hexdigest()

def computeTable(passwordPolicy, minPasswordLength, maxPasswordLength):
    "function to compute rainbow table using selected password policy"

    print()
    print("Generating Rainbow Table for password cracking...")
    print()

    #only doing the specified cases for simplicity
    policy = ["uppercase", "lowercase", "numeric", "alpha", "alphanumeric"]

    charList = []
    crackDict = {}

    #get the path of the directory where the script is running
    path = pathlib.Path(__file__).parent.absolute()     
    path = str(path)
    
    filepath = path + r"\Files\rainbowTable.txt"

    # check if password policy is valid
    if passwordPolicy not in policy:
        return "Invalid password policy. Please specify one of the following: uppercase, lowercase, numeric, alpha, alphanumeric"  

    # give a list of all possible characters according to chosen password policy
    elif passwordPolicy == "uppercase":
        charList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']   
    elif passwordPolicy == "lowercase":
        charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    elif passwordPolicy == "numeric":
        charList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    elif passwordPolicy == "alpha":
        charList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    elif passwordPolicy == "alphanumeric":
        charList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for passwordLength in range(minPasswordLength, maxPasswordLength + 1):
        # generate a list of all possible combinations of characters and their md5 hash using product function from itertools library
        for combination in product(charList, repeat = passwordLength):
            password = ''.join(combination)
            
            #write to file in format: md5 hash, plaintext password
            crackDict[generateHash_md5(password)] = password
    
    #writing the created dictionary into a file as a json object
    #used dictionary for faster lookup
    #create a file to store the computed rainbow table at specified path
    try:
        filePtr = open(filepath, "w", encoding = "utf-8")       #store inverted index in a file
    except IOError:
        print("Error: Operation failed.")
    else:
        filePtr.write(json.dumps(crackDict))
        filePtr.close()
