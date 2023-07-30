User_input = input("Input: ")

vowels = ['a', 'e', 'i', 'o', 'u']
newText = ""

for i in (User_input):
    if i.lower() not in vowels:
        newText += i

text = newText
print(text)
