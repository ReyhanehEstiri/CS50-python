import re

def main():
    ip = input("IPv4 Address: ").strip()
    print(validate(ip))

def validate(ip):
    try:
        nos = ip.strip().split('.')
        if len(nos) != 4:
            return False
        for n in nos:
            if int(n)<0 or int(n)>255:
                return False
        return True
    except:
        return True


if __name__ == "__main__":
    main()