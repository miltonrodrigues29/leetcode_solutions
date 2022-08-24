class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        def dfs(node):
            if not node: return
            output.append(node.val)
            for child in node.children:
                dfs(child)
        dfs(root)
        return output