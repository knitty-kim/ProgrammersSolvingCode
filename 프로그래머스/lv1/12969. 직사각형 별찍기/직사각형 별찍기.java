import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        char[][] answer = new char[b][a];

        for (int i = 0; i < b; i++) {
            for (int j = 0; j < a; j++) {
                answer[i][j] = '*';
            }
        }
        
        for (int i = 0; i < b; i++) {
            for (int j = 0; j < a; j++) {
                System.out.print(answer[i][j]);
            }
            System.out.println();
        }
    }
}