from sys import argv

# since help will be printed many times, creating function


def print_help(msg=" "):
    print(
        f"""
Issue is: {msg}
Script Syntax:
    
    python sysargv.py -a  -b -c opt1 opt2 opt3 `list of files / *.extension` "
    python sysargv.py -h

    -a: Sets a flag
    -b: Sets b flag
    -c: Sets c flag
    opt1: Assigns value to Opt1
    opt2: Assigns value to Opt2
    opt3: Assigns value to Opt3
    list of files: name of files to operated on
"""
    )


flagh = flaga = flagb = flagc = opt1 = opt2 = opt3 = None

if len(argv) >= 2 and len(argv) <= 4:
    print(f"First arg is: {argv[0]}")

    if argv[1] == "-h":
        flagh = 1
        print_help(msg="called using -h flag")

    elif "-" in argv[1]:
        flaga = 1
        print(f"Flag a is: {argv[1]} setting flaga with {flaga}")
    else:
        opt1 = 1
        print(f"Option 1 is: {argv[1]}")

    try:
        if "-" in argv[2]:
            print(f"Flag 2 is: {argv[2]}")
        else:
            print(f"Option is : {argv[2]}")

    except IndexError:
        pass
        # print("python sysargv -h")

    try:
        if "-" in argv[3]:
            print(f"Flag 3 is: {argv[3]}")
        else:
            print(f"Option is : {argv[3]}")

    except IndexError:
        pass
        # print("python sysargv -h")

elif len(argv) == 5 and "*" in argv[4]:
    print(f"File wildcard is {argv[4]}")

elif len(argv) > 4:
    for dx, arg in enumerate(argv[4:]):
        print("File is {dx} is {arg}")

    # there should be a minimum of 1 arg when the code is executed else print help
else:
    print_help(msg="Not enough arguments")

# there can be 3 flags, 3 options and n number
# of files. How to see those args
# One idea is to check if an argument exists
# by seeing if it is None or has value
# Trying to access argv[2] itself will raise
# index error, so I can enclose
# each of arg in try except
