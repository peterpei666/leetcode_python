class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [-1] * n
        root = list(range(n))
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            root[rootY] = rootX
            return True

        for i in range(n):
            if leftChild[i] != -1:
                if parent[leftChild[i]] != -1:
                    return False
                parent[leftChild[i]] = i
                if not union(i, leftChild[i]):
                    return False
            if rightChild[i] != -1:
                if parent[rightChild[i]] != -1:
                    return False
                parent[rightChild[i]] = i
                if not union(i, rightChild[i]):
                    return False
        return sum(1 for i in range(n) if parent[i] == -1) == 1
