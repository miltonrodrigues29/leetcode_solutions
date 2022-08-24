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
# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         if not root:
#             return []
#         q = deque([root])
#         output = []
#         while q:
#             cand = q.popleft()
#             output.append(cand.val)
#             for child in reversed(cand.children):
#                 q.appendleft(child)
#         return output