import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            lines = get_line(sys.argv[1])
            headers = lines[0]
            table = lines[1::]
            print(tabulate(table, headers, tablefmt="grid"))

def get_line(file):
    lines = []
    try:
        with open(file) as file:
            for line in file:
                lines.append(line.strip().split(","))
    except FileNotFoundError:
        sys.exit("File does not exist")

    return lines


if __name__ == "__main__":
    main()
