class UnionFind:
    def __init__(self, n: int):
        self.id = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def root(self, i: int) -> int:
        print(i, self.id)
        while i != self.id[i]:
            # path compression
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, p: int, q: int) -> bool:
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int) -> None:
        i = self.root(p)
        j = self.root(q)

        if i == j:
            return

        # make i always the smallest subtree
        if self.size[i] > self.size[j]:
            i, j = j, i

        # weighting
        self.id[i] = j
        self.size[j] += self.size[i]
