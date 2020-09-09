# Problem 752

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadset = set(deadends)
        
        if "0000" in deadset:
            return -1
        
        deadset.add("0000")
        queue = collections.deque()
        queue.append(["0000", 0])
        
        while queue:
            current, moves = queue.popleft()
            
            if current == target:
                return moves
            
            for i in range(0, 4):
                for j in (1, -1):
                    next_slot = current[0:i] + "{}" + current[i+1:]
                    d = (int(current[i]) + j) % 10
                    next_slot = next_slot.format(d)
                    
                    if next_slot not in deadset:
                        queue.append([next_slot, moves + 1])
                        deadset.add(next_slot)
        
        return -1
