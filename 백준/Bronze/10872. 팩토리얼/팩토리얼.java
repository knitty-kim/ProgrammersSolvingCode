import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int answer = 1;
        for (int i = n; i >= 0; i--) {
            if (i == 0) {
                answer *= 1;
            } else {
                answer *= i;
            }
        }
        System.out.println(answer);
    }
}