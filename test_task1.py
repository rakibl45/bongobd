from task1 import print_depth


class TestTask1:

    def test_empty_dataset(self, capsys):
        data = {}
        print_depth(data)
        output, error = capsys.readouterr()
        assert output == ""
        assert error == ""

    def test_single_dict(self, capsys):
        data = {
            "key1": 1
        }
        print_depth(data)
        output, error = capsys.readouterr()
        assert output == "key1 1\n"
        assert error == ""

    def test_sample_data(self, capsys):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }
        print_depth(data)
        output, error = capsys.readouterr()
        assert output == (
            "key1 1\n"
            "key2 1\n"
            "key3 2\n"
            "key4 2\n"
            "key5 3\n"
        )
        assert error == ""
