import pandas as pd

def read_console():
    """
    Read the input from console and return it as a string.
    """
    return input("Input something: ")

def read_file_python(filename):
    """
    Reads a file with the given filename and return it as a string.
    """
    with open(filename, 'r') as f:
        return f.read()

def read_file_pandas(filename):
    """
    Reads a csv file with the given filename and return it as a Pandas DataFrame.
    """
    return pd.read_csv(filename)
