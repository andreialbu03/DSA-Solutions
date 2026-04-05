class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False
        
        s1_map, window_map = {}, {}
        
        # Initialize the maps for the first window
        for i in range(n1):
            s1_map[s1[i]] = s1_map.get(s1[i], 0) + 1
            window_map[s2[i]] = window_map.get(s2[i], 0) + 1
            
        if s1_map == window_map:
            return True
            
        # Slide the window across s2
        for i in range(n1, n2):
            new_char = s2[i]
            old_char = s2[i - n1]
            
            # Add new character
            window_map[new_char] = window_map.get(new_char, 0) + 1
            
            # Remove old character and clean up dictionary keys
            window_map[old_char] -= 1
            if window_map[old_char] == 0:
                del window_map[old_char]
                
            if s1_map == window_map:
                return True
                
        return False