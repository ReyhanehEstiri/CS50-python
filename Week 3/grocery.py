def main():
    displaylist()

def displaylist():
    grocerylist = {}
    while True:
        try:

            item = input().upper()
            if item in grocerylist:
                grocerylist[item] +=1
            else:
                grocerylist[item] = 1
        except EOFError:
            sortedlist = dict(sorted(list(grocerylist.items())))
            for item in sortedlist:
                print(sortedlist[item], item, sep=" ")
            break

if __name__ == "__main__":
    main()
