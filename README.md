# Algorithms Cheatsheet

## Table of Contents
- [Algorithms Cheatsheet](#algorithms-cheatsheet)
  - [Table of Contents](#table-of-contents)
  - [Substring Matching](#substring-matching)
      - [Rabin-Karp](#rabin-karp)
      - [KVM](#kvm)
  - [Queue and Stack](#queue-and-stack)
      - [Queue and BFS](#queue-and-bfs)
      - [Stack and DFS](#stack-and-dfs)
  - [Recursion](#recursion)
      - [Memoization](#memoization)
      - [Tail recursion](#tail-recursion)
  - [Binary Tree](#binary-tree)
      - [Traversals](#traversals)
  - [Hashtables](#hashtables)
      - [Hashmap](#hashmap)
      - [Hashset](#hashset)
  - [Sorting](#sorting)
      - [Quicksort](#quicksort)
      - [Mergesort](#mergesort)
  - [Binary Search](#binary-search)
      - [Common](#common)
      - [Leftmost](#leftmost)
      - [Rightmost](#rightmost)
  - [Graphs](#graphs)
      - [Union-Find](#union-find)
  - [Heaps](#heaps)
  - [Dynamic Programming](#dynamic-programming)
  - [Greedy Algorithms](#greedy-algorithms)

## Substring Matching

#### Rabin-Karp
```python
from functools import reduce


def rabinKarp(haystack: str, needle: str) -> int:
    # needle is not substring of haystack
    if len(needle) > len(haystack):
        return -1

    BASE = ord('z') - ord('a') + 1  # number of letters = 26

    haystackHash = reduce(lambda h, c: h * BASE + ord(c),
                          haystack[:len(needle)], 0)
    needleHash = reduce(lambda h, c: h * BASE + ord(c), needle, 0)

    power_s = BASE**max(len(needle) - 1, 0)  # BASE^(s-1)

    for i in range(len(needle), len(haystack)):
        if needleHash == haystackHash and needle == haystack[i -
                                                             len(needle):i]:
            return i - len(needle)

        # roll hash
        haystackHash -= ord(haystack[i - len(needle)]) * power_s
        haystackHash = haystackHash * BASE + ord(haystack[i])

    if haystackHash == needleHash and haystack[-len(needle):] == needle:
        return len(haystack) - len(needle)
    return -1  # s is not a substring of t.
```

#### KVM
```python
def partialMatchTable(self, needle: str):
    ret = [0]

    for i in range(1, len(needle)):
        j = ret[i - 1]
        while j > 0 and needle[j] != needle[i]:
            j = ret[j - 1]
        ret.append(j + 1 if needle[j] == needle[i] else j)
    return ret


def strStr(self, haystack: str, needle: str) -> int:
    if not needle: return 0
    partial = self.partialMatchTable(needle)
    j = 0

    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = partial[j - 1]

        if haystack[i] == needle[j]:
            j += 1

        if j == len(needle): return i - j + 1

    return -1
```


## Queue and Stack

#### Queue and BFS
```
int BFS(Node root, Node target) {
    Queue<Node> queue;  // store all nodes which are waiting to be processed
    Set<Node> visited;  // store all the nodes that we've visited
    int step = 0;       // number of steps neeeded from root to current node
    // initialize
    add root to queue;
    add root to visited;
    // BFS
    while (queue is not empty) {
        step = step + 1;
        // iterate the nodes which are already in the queue
        int size = queue.size();
        for (int i = 0; i < size; ++i) {
            Node cur = the first node in queue;
            return step if cur is target;
            for (Node next : the neighbors of cur) {
                if (next is not in used) {
                    add next to queue;
                    add next to visited;
                }
                remove the first node from queue;   
            }
        }
    }
    return -1;          // there is no path from root to target
}
```

#### Stack and DFS
```
boolean DFS(int root, int target) {
    Set<Node> visited;
    Stack<Node> stack;
    add root to stack;
    while (s is not empty) {
        Node cur = the top element in stack;
        remove the cur from the stack;
        return true if cur is target;
        for (Node next : the neighbors of cur) {
            if (next is not in visited) {
                add next to visited;
                add next to stack;
            }
        }
    }
    return false;
}
```


## Recursion

#### Memoization
```python
def memoize(function):
    cache = {}
    
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            val = function(*args)
            cache[args] = val
            return val
    return decorated_function

@memoize
def fib(n: int, a: int = 0, b: int = 1):
    if n == 0: return a
    if n == 1: return b
    return fib(n-1, b, a+b)
```

#### Tail recursion
> TODO


## Binary Tree

#### Traversals
> TODO


## Hashtables
#### Hashmap
> TODO
#### Hashset
> TODO


## Sorting
#### Quicksort
> TODO
#### Mergesort
> TODO


## Binary Search

#### Common
```python
def binarySearch(nums, target):
    if len(nums) == 0: return -1

    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1

    return -1
```

#### Leftmost
```python
def binarySearch(nums, target):
    if len(nums) == 0: return -1
    
    l, r = 0, len(nums)

    while l < r:
        m = l + (r - l) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    
    if l > len(nums) or (l < len(nums) and nums[l] != target):
        return -1
    return l
```

#### Rightmost
```python
    def binarySearch(nums, target):
        if len(nums) == 0: return -1

        l, r = 0, len(nums)

        while l < r:
            m = l + (r - l) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m
        
        if l - 1 > len(nums) or (l - 1 < len(nums) and nums[l-1] != target):
            return -1
        return l - 1
```
## Graphs
#### Union-Find

```python
    class UnionFind:
        def __init__(self, nodes):
            self.group = [node for node in nodes]

        def find(self, node) -> int:
            while node != self.group[node]:
                # Path Compression
                group_node = self.group[node]
                self.group[node] = self.group[group_node]
                node = group_node
            return node

        def same_set(self, node_a, node_b) -> bool:
            return self.find(node_a) == self.find(node_b)

        def unite(self, node_a, node_b) -> None:
            group_a = self.find(node_a)
            group_b = self.find(node_b)
            self.group[group_a] = group_b
```

## Heaps
```python
class heap:
    def __init__(self, L=[]):
        self.heap = []

        for elem in L:
            self.insert(elem)

    def __len__(self):
        return len(self.heap)

    def __getitem__(self, i):
        return self.heap[i]

    def __setitem__(self, k, v):
        self.heap[k] = v

    def __str__(self):
        return f"heap({self.heap})"

    def __repr__(self):
        return str(self)

    def insert(self, val):
        self.heap.append(val)
        self.bubbleUp(-1)

    def bubbleUp(self, i):
        i = i % len(self)

        while i > 0:
            child, parent = i, i // 2

            if self[child] < self[parent]:
                self[child], self[parent] = self[parent], self[child]
            i = i // 2

    def minChild(self, i):
        if 2 * i + 1 >= len(self):
            return 2 * i

        return 2 * i + 1 if self[2 * i + 1] < self[2 * i] else 2 * i

    def bubbleDown(self, i):
        while 2 * i < len(self):
            minChildIdx, parent = self.minChild(i), i

            if minChildIdx == parent:
                break

            if self[parent] > self[minChildIdx]:
                self[parent], self[minChildIdx] = self[minChildIdx], self[
                    parent]
            i = minChildIdx

    def pop(self):
        return self.heap.pop()

    def popMin(self):
        ret = self[0]

        if len(self) > 1:
            self[0] = self.pop()
        else:
            self.pop()

        self.bubbleDown(0)
        return ret
``` 

```python
import heapq

L, k = [9, 5, 3, 6, 7, 1], 3

heapq.heapify(L) # transforms the elements in L into a heap in-place
heapq.nlargest(k, L) # returns the k largest elements in L
heapq.nsmallest(k, L) # returnts the k smallest elements in L
heapq.heappush(h, e) # pushes a new element on the heap
heapq.heappop(h) # pushes the smallest element from the heap
heapq.heappushpop(h, a) # pushs a on the heap and then pops the smallest element
e = h[0] # returns the samllest element on the heap without popping it
```


## Dynamic Programming
> TODO


## Greedy Algorithms
> TODO

