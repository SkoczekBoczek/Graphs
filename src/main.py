import sys
import re
import random

def printMenu():
    print("================================")
    print("{}        {}".format("Help", "Shows this menu"))
    print("{}        {}".format("Exit", "Exits the program (or ctrl+D)"))
    print("================================")

def cleanInput(raw_data):
    data = []
    if isinstance(raw_data, list):
        input_str = ' '.join(raw_data)
    else:
        input_str = raw_data
    
    numbers = re.split(r'[,\s]+', input_str.replace(',', ' ').strip())
    
    for num in numbers:
        if num:
            try:
                data.append(int(num))
            except ValueError:
                print(f"'{num}' is invalid ")
    
    return data

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ["--generate", "--user-provided"]:
        print("Usage: python3 src/main.py --generate")
        print("Or:    python3 src/main.py --user-provided")
        sys.exit(1)
    print("Enter number of vertexes!")
    vertexes = int(input("nodes> "))

    graph = {}

    if sys.argv[1] == "--generate":
        saturation = int(input("saturation> "))
        if saturation < 0 or saturation > 100:
            print(f"'{saturation}' is out of range")
            sys.exit(1)

    elif sys.argv[1] == "--user-provided":
        for i in range(1, vertexes + 1):
            print("Enter successors for vertex", i)
            while True:
                successorsInput = input(f"{i}>").strip()
                successors = cleanInput(successorsInput)

                cleanedSuccessors = []
                errorsFound = False
                for x in successors:
                    if x == i:
                        print("Self loop, try again")
                        errorsFound = True
                    elif x < 0 or x > vertexes:
                        print(f"'{x}' is out of range, try again")
                        errorsFound = True
                    elif x in cleanedSuccessors:
                        print(f"'{x}' is a duplicate, try again")
                        errorsFound = True
                    else: 
                        cleanedSuccessors.append(x)
                
                if errorsFound:
                    print("Please try again")
                    continue

                graph[i] = successors
                break
    
    print("\nGraph representation:")
    for node, successors in graph.items():
        print(f"{node} -> {successors}")

if __name__ == "__main__":
    main()