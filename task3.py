class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


def lca(node1, node2):
    """
    Worst case time complexity: O(n^2).
    Best case time complexity: Ω(1).
    Space complexity: O(n).

    """

    node1_values = [node1.value]
    node2_values = [node2.value]
    
    if node1.value == node2.value:
        print(node1.value)
        return
  

    while True:
        if node1.parent:
            node1 = node1.parent
            if node1.value in node2_values:
                print(node1.value)
                return
            node1_values.append(node1.value)

        if node2.parent:
            node2 = node2.parent
            if node2.value in node1_values:
                print(node2.value)
                return
            node2_values.append(node2.value)


n1 = Node(1, None)
n2 = Node(2, n1)
n3 = Node(3, n1)
n4 = Node(4, n2)
n5 = Node(5, n2)
n6 = Node(6, n3)
n7 = Node(7, n3)
n8 = Node(8, n4)
n9 = Node(9, n4)

lca(n6, n7)
