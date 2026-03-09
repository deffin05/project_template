def write_console(input_value):
    """
    Print the input in the console.
    """
    print(input_value)

def write_file(filename, input_value):
    """
    Writes the given input to the given filename.
    """
    with open(filename, 'w') as f:
        f.write(input_value)
