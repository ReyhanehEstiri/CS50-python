import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            create_new_csv(sys.argv[1], sys.argv[2])


def create_new_csv(csv_input, csv_output):
    try:
        with open(csv_input) as csvfile:
            reader = csv.DictReader(csvfile)
            with open(csv_output, "w", newline="") as new_file:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    name = row["name"].replace("\"", "").split(",")
                    writer.writerow({"first": name[1].strip(), "last": name[0].strip(), "house": row["house"].strip()})

    except FileNotFoundError:
        sys.exit(f"Could not read {argv[1]}")


if __name__ == "__main__":
    main()
