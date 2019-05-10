from union_find import UnionFind

def test_one_union():
    uf = UnionFind(9)
    uf.union(4, 3)
    assert uf.connected(3, 4) == True

def test_multiple_unions():
    uf = UnionFind(10)
    uf.union(4, 3)
    uf.union(3, 8)
    uf.union(6, 5)
    uf.union(9, 4)
    uf.union(2, 1)
    uf.union(5, 0)
    uf.union(7, 2)
    uf.union(6, 1)

    assert uf.connected(8, 4) == True
    assert uf.connected(1, 9) == False
    assert uf.connected(0, 1) == True
