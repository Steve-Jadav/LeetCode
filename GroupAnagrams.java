import java.util.HashMap;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<String, List<String>>();
        
        for (String string: strs) {
            char charArray[] = string.toCharArray();
            Arrays.sort(charArray);
            String sorted = new String(charArray);
            
            if (map.containsKey(sorted)) {
                map.get(sorted).add(string);
            }
            
            else {
                List<String> list = new ArrayList<>();
                list.add(string);
                map.put(sorted, list);
            }
        }
        
        List<List<String>> result = new ArrayList<>();
        for (String s: map.keySet()) {
            List<String> temp = map.get(s);
            result.add(temp);
        }
        
        return result;
    }
}
