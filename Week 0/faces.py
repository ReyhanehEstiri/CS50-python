def convert(s: str):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    print(s)
convert("Hello :) Goodbye :(")
