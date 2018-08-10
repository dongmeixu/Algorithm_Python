"""
给定一棵二叉树，返回所有从根节点到叶子节点的路径，其和为sum

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = []
    p = []

    def pathSum(self, root, sum):
        if not root:
            return []

        temp = []
        self.dfs(root, sum, temp)
        return self.res

    def dfs(self, root, sum, temp):
        sum -= root.val
        temp.append(root.val)

        if sum == 0 and not root.left and not root.right:
            self.res.append(temp[:])
        else:
            if root.left:
                self.dfs(root.left, sum, temp)
            if root.right:
                self.dfs(root.right, sum, temp)
        temp.pop(-1)

    # def pathSum(self, root, sum):
    #     if not root:
    #         return self.res
    #
    #     self.p.append(root.val)
    #     # 此时已经找到一条符合要求的路径
    #     if sum == root.val and not root.left and not root.right:
    #         self.res.append(self.p[:])
    #     else:
    #         if root.left:
    #             self.pathSum(root.left, sum - root.val)
    #         if root.right:
    #             self.pathSum(root.right, sum - root.val)
    #
    #     self.p.pop()
    #     return self.res


h = root = TreeNode(1)
left1 = h.left = TreeNode(2)
right1 = h.right = TreeNode(0)
left1.left = TreeNode(4)
left1.right = TreeNode(4)
right1.left = TreeNode(6)
right1.right = TreeNode(7)
print(Solution().pathSum(root, 7))
