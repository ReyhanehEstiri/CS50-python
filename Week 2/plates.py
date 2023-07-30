def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    valid = False
    if len(s) >= 2 and len(s) <= 6:
        start = s[0:2]
        if s.isalpha():
            valid = True
        elif s.isalnum() and start.isalpha():
            if not s[-1].isalpha():
                for character in s[2:]:
                    if character.isalpha():
                        continue
                    elif character.isdigit() and character != "0":
                        valid = True
                    break
    return valid

main()
