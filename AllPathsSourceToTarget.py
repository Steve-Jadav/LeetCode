# Depth First Search

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """Problem 797"""
        if (graph == None):
            return []
        
        self.result = list()
        self.findPaths(graph, 0, [0])
        return self.result
    
    def findPaths(self, graph, current, path):
        
        if current == len(graph) - 1:
            self.result.append(path)
            return 
        
        for neighbor in graph[current]:
            self.findPaths(graph, neighbor, path + [neighbor])


# Breadth First Search

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        if (graph == None or len(graph) == 0):
            return []
        
        source, destination = 0, len(graph) - 1
        result = list()
        queue = collections.deque([])
        queue.append((source, [0]))
        
        while queue:
            node, currentPath = queue.popleft()
            
            if node == destination:
                result.append(currentPath)
                
            for neighbour in graph[node]:
                queue.append((neighbour, currentPath + [neighbour]))
            
        return result
