class Solution {
    public double solution(int[] numbers) {
        double d = 0;
		
		for(int i : numbers) {
			d += (double)i;
		}
		
		d /= numbers.length;
        
        
        return d;
    }
}