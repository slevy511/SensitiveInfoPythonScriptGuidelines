# main.py

''' Installing dotenv

https://pypi.org/project/python-dotenv/
"pip install python-dotenv"

'''

from dotenv import dotenv_values


sensitive_info = dotenv_values(".env")
passwords = dotenv_values(".env.passwords")
keys = dotenv_values(".env.keys")



def main():

    print("API KEY 1: " + keys["KEY1"])
    print(" API KEY 2: " + sensitive_info["KEY2"])

    print("PASSWORD 1: " + passwords["PASSWORD1"])
    print("PASSWORD 2: " + sensitive_info["PASSWORD2"])




if __name__ == "__main__":
    main()

