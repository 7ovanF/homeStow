import java.util.Scanner;

public class Worksheet3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        number3(input);
        number4(input);
        input.close();
    }
    public static void number3(Scanner input) {
        
    }
    public static void number4(Scanner input) {
        System.out.print("Masukkan nilai n: ");
        int n = input.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = n; j > i; j--) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }
}

