import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            int tmp = sc.nextInt();
            if (tmp < x) {
                System.out.print(tmp + " ");
            }
        }
    }
}