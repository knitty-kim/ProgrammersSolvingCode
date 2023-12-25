import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int count = 0;
        for (int i = 1; i <= N; i++) {
            String poll = sc.next();
            String tmp = poll.replace("X", "");
            if (tmp.length() >= ((double)M/2)) {
                count++;
            }
        }
        System.out.println(count);
    }
}