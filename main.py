from app.io.input import *
from app.io.output import *

def main():
    console_input = read_console()
    file_input = read_file_python("data/input.txt")
    pandas_input = read_file_pandas("data/input.csv")

    write_console(console_input)
    write_console(file_input)
    write_console(pandas_input)

    write_file("data/output_console.txt", console_input)
    write_file("data/output_file.txt", file_input)

if __name__ == "__main__":
    main()