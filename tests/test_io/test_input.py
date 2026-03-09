import pytest
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