import requests
import sys

def main():
    if len(sys.argv) == 2:
         try:
            n = float(sys.argv[1])
            print(get_bitcoin_rate_float(n))
         except ValueError:
             sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")

def get_bitcoin_rate_float(num):
    price = 0
    try:
        request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = request.json()
        price = response["bpi"]["USD"]["rate_float"]
        total = price * num
        return f"${total:,.4f}"
    except requests.RequestException:
        return None


if __name__ == "__main__":
    main()
