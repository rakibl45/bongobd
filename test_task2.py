import pytest

from task2 import print_depth, Person


class TestTask2:

    @pytest.fixture
    def person_a(self):
        return Person("Rakibul", "Bashar", None)

    @pytest.fixture
    def person_b(self, person_a):
        return Person("Abul", "Bashar", person_a)

    @pytest.fixture
    def person_c(self, person_b):
        return Person("Bashir", "Uddin", person_b)

    def test_person_object(self, capsys, person_a):
        print_depth(person_a)
        output, error = capsys.readouterr()
        assert output == (
            "Rakibul: 1\n"
            "Bashar: 1\n"
            "None: 1\n"
        )
        assert error == ""

    def test_empty_dataset(self, capsys):
        data = {}
        print_depth(data)
        output, error = capsys.readouterr()
        assert output == ""
        assert error == ""

    def test_single_dict(self, capsys):
        data = {
            "Key": 1
        }
        print_depth(data)
        output, error = capsys.readouterr()
        assert output == "Key 1\n"
        assert error == ""

    def test_sample_data(self, capsys, person_c):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": person_c,
                }
            },
        }
        print_depth(data)
        output, error = capsys.readouterr()
        assert output == (
            "key1 1\n"
            "key2 1\n"
            "key3 2\n"
            "key4 2\n"
            "key5 3\n"
            "user 3\n"
            "Bashir: 4\n"
            "Uddin: 4\n"
            "Abul Bashar: 4\n"
            "Abul: 5\n"
            "Bashar: 5\n"
            "Rakibul Bashar: 5\n"
            "Rakibul: 6\n"
            "Bashar: 6\n"
            "None: 6\n"
        )
        assert error == ""

