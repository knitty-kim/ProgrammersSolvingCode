import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
class Solution {
    public int solution(int[] array, int n) {
       Map<Integer, Integer> mp = new HashMap<>();
		
		for(int i=0; i<array.length; i++) {
			mp.put(i, array[i]-n);
		}
        
        Entry<Integer, Integer> minEntry = null;
		Set<Entry<Integer, Integer>> etrySet = mp.entrySet();
		for(Entry<Integer, Integer> entry : etrySet) {
			if(Math.abs(entry.getValue())==0){
                minEntry = entry;
                break;
            }
			if(minEntry == null || Math.abs(entry.getValue()) < Math.abs(minEntry.getValue())) {
				minEntry = entry;
			}
			else if((Math.abs(entry.getValue()) == Math.abs(minEntry.getValue())) && (entry.getValue() < minEntry.getValue())) {
				minEntry = entry;
			}
		}
		
		
		int answer = array[minEntry.getKey()];
        
        return answer;
    }
}