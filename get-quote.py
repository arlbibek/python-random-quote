import random


def main():
    with open("quotes.txt", "rt", encoding='UTF8') as f:
        quotes = f.readlines()

    random_int = random.randint(0, len(quotes))
    print(quotes[random_int])


if __name__ == "__main__":
    main()
