import random

def main():
    score = 0
    chances = 3
    lvl = get_level()
    for _ in range(10):
        if chances == 3:
            x, y = generate_integer(lvl)
        user_answer = input(f"{x} + {y} = ")
        answer = x + y
        if user_answer.isdigit() and int(user_answer) == answer:
            score += 1
            chances = 3
        else:
            print("EEE")
            chances -= 1
            if chances == 0:
                print(f"{x} + {y} = {answer}")
                chances = 3
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 0 >= n or n > 3:
                raise ValueError
            break
        except ValueError:
            continue
    return n


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()
