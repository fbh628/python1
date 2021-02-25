from src.database import Database
from src.argparser import ArgParser


def main():
    db = Database("localhost", "root", "LZhwH2sC9y6Hbk3eiwT", "schulepython")

    argParser = ArgParser()
    command, arg = argParser.get()

    if command in ["show", "-s", "--show"]:
        if arg in ["books", "-b", "--books"]:
            books = db.get_books()
            print_pretty("Book", "Author", books)
        elif arg in ["authors", "-a", "--authors"]:
            authors = db.get_authors()
            print_pretty("First Name", "Last Name", authors)
        elif arg in ["publishers", "-p", "--publishers"]:
            publishers = db.get_publishers()
            print_pretty("Name", "Country", publishers)
    if command in ["save", "-sf", "--save"]:
        if arg in ["books", "-b", "--books"]:
            books = db.get_books()
            save_pretty("Book", "Author", books)
        elif arg in ["authors", "-a", "--authors"]:
            authors = db.get_authors()
            save_pretty("First Name", "Last Name", authors)
        elif arg in ["publishers", "-p", "--publishers"]:
            publishers = db.get_publishers()
            save_pretty("Name", "Country", publishers)
    elif command in ["default"]:
        print_help()
    elif command in ["help", "-h", "--help"]:
        print_help()
    else:
        print(f"Command \"{command}\" not found. Use -h to see the help page.")


def print_help():
    print("===========HELP===========")
    print("Finns Python Schul Projekt")
    print("\n")
    print("COMMAND\t\t\t| Description")
    print("show\t\t\t| asdf.")
    print("save\t\t\t| asdf.")
    print("help\t\t\t| Shows this command.")


def print_pretty(column1, column2, data):
    print("==================================================")
    print('%-25s%-25s' % (column1, column2))
    print("==================================================")
    for d in data:
        print('%-25s%-25s' % (d[0], d[1]))


def save_pretty(column1, column2, data):
    s = "==================================================\n"
    s += '%-25s%-25s\n' % (column1, column2)
    s += "==================================================\n"
    for d in data:
        s += '%-25s%-25s\n' % (d[0], d[1])
    save_file(s)


def save_file(data):
    with open("data.txt", "w") as file:
        file.write(data)


if __name__ == "__main__":
    main()
