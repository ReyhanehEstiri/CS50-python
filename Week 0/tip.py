def main():
    dollar_string = input("How much was the meal? ")
    percent_string = input("What percentage would you like to tip? ")

    try:
        dollars = float(dollar_string.replace("$", "").strip())
        percent = float(percent_string.replace("%", "").strip()) / 100.0
        if dollars <= 0 or percent <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter positive numbers only.")
        return

    tip = dollars * percent
    print(f"Leave ${tip:.2f} as a tip.")


if __name__ == "__main__":
    main()
