from task3 import Node, lca


class TestTask3:

    n1 = Node(1, None)
    n2 = Node(2, n1)
    n3 = Node(3, n1)
    n4 = Node(4, n2)
    n5 = Node(5, n2)
    n6 = Node(6, n3)
    n7 = Node(7, n3)
    n8 = Node(8, n4)
    n9 = Node(9, n4)

    def test_root_node(self, capsys):
        lca(self.n1, self.n1)
        output, error = capsys.readouterr()
        assert output == "1\n"
        assert error == ""

    def test_leaf_nodes(self, capsys):
        lca(self.n8, self.n7)
        output, error = capsys.readouterr()
        assert output == "1\n"
        assert error == ""

    def test_root_and_leaf(self, capsys):
        lca(self.n8, self.n1)
        output, error = capsys.readouterr()
        assert output == "1\n"
        assert error == ""

    def test_siblings(self, capsys):
        lca(self.n8, self.n9)
        output, error = capsys.readouterr()
        assert output == "4\n"
        assert error == ""

    def test_uncle(self, capsys):
        lca(self.n8, self.n5)
        output, error = capsys.readouterr()
        assert output == "2\n"
        assert error == ""

    def test_father(self, capsys):
        lca(self.n4, self.n2)
        output, error = capsys.readouterr()
        assert output == "2\n"
        assert error == ""

    def test_grandfather(self, capsys):
        lca(self.n8, self.n2)
        output, error = capsys.readouterr()
        assert output == "2\n"
        assert error == ""
