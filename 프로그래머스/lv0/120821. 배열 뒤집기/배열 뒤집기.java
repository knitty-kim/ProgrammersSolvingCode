import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {
    public int[] solution(int[] num_list) {
        Integer[] alist = new Integer[num_list.length];
		for(int i=0;i<num_list.length;i++) {
			alist[i] = (Integer)num_list[i];
		}
		List<Integer> list = Arrays.asList(alist);
		Collections.reverse(list);
		
		//list.toArray() 는 Object[]를 리턴, 따라서 캐스팅을 해줘야한다
		//따라서 (Integer[])을 앞에 붙여줘야 한다
		
		//list.toArray(T[] a)는 파라미터로 주어진 배열과 같은 타입의 배열을 리턴
		//new Integer[list.size()]와 같은 형식으로 쓰자
		Integer[] blist = list.toArray(new Integer[0]);
        
        int[] answer = Arrays.stream(blist).mapToInt(i->i).toArray();
        return answer;
    }
}