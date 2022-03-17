#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from lib2to3.pytree import Node
from logging.config import valid_ident


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        # 1. 查找所有节点
        nodes = self.find_nodes_by_bfs(node)
        # 2. 复制节点的val
        # 返回 mapping[node] = new_node (new_node只有val)
        mapping = self.copy_node(nodes)
        # 3. 复制边
        self.copy_edges(nodes, mapping)
        return mapping[node]

    def find_nodes_by_bfs(self, node):
        queue = collections.deque([node])
        visited = set([node])
        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        return list(visited)

    def copy_node(self, nodes):
        mapping = dict()
        for node in nodes:
            mapping[node] = Node(node.val)
        return mapping
    
    def copy_edges(self, nodes, mapping):
        for node in nodes:
            # 取出对应新的节点
            new_node = mapping[node]
            for neighbor in node.neighbors:
                # 取出节点的邻接点
                new_neighbor = mapping[neighbor]
                # 添加新节点的邻接点
                new_node.neighbors.append(new_neighbor)

# @lc code=end

