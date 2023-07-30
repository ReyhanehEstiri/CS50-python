def main():
    format_date()

def format_date():
     months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

     while True:
        date = input("Date:")
        if "/" in date:
            mm, dd, yy = date.split("/")
        else :
            mm, dd, yy = date.replace(",", "").split()
            if mm in months:
                mm = months.index(mm) + 1
            else:
                continue
        try:
            dd = int(dd)
            yy = int(yy)
            mm = int(mm)
            if dd > 31 or mm > 12:
                continue
        except ValueError:
            continue
        break

     print(f"{yy}-{mm:02}-{dd:02}")

if __name__ == "__main__":
    main()


