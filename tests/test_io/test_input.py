import pytest
import pandas as pd
from app.io.input import *

def test_read_file_python_normal(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("123\n456")

    result = read_file_python(test_file)

    assert result == "123\n456"

def test_read_file_python_empty_file(tmp_path):
    test_file = tmp_path / "empty.txt"
    test_file.write_text("")

    result = read_file_python(test_file)

    assert result == ""

def test_read_file_python_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_file_python("aoaooaoaoaooaoaoaoaoaoaoaoa.txt")


def test_read_file_pandas_normal(tmp_path):
    test_file = tmp_path / "test.csv"

    test_file.write_text("name,age\nIvan,25\nDmytro,19")

    df = read_file_pandas(test_file)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == ["name", "age"]


def test_read_file_pandas_empty_csv(tmp_path):
    test_file = tmp_path / "empty.csv"
    test_file.write_text("col1,col2\n")

    df = read_file_pandas(test_file)

    assert df.empty
    assert list(df.columns) == ["col1", "col2"]


def test_read_file_pandas_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_file_pandas("wertyuiosdfg.csv")