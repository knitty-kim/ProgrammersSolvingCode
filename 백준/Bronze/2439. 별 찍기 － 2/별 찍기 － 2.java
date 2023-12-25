import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int i = 1; i <= T; i++) {
            for (int k = 1; k <= T-i; k++) {
                System.out.print(" ");
            }
            for (int j = T-i+1; j <= T; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}