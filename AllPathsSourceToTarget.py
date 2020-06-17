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
