import java.util.Scanner;

public class Worksheet2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        // kuadranKoordinat(input);
        nilaiSwitchCase(input);

        input.close();
    }

    public static void kuadranKoordinat(Scanner input) {
        // no validation
        System.out.print("Masukkan koordinat: ");
        String teksInput = input.nextLine();

        int commaPos = teksInput.indexOf(',');
        int x = Integer.parseInt(teksInput.substring(1, commaPos).trim());
        int y = Integer.parseInt(teksInput.substring(commaPos + 1, teksInput.length() - 1).trim());

        String kuadran;
        if (x == 0 || y == 0) {
            kuadran = "Di sumbu";
        } else if (x > 0) { // 1 atau 4
            if (y > 0) {
                kuadran = "1";
            } else {
                kuadran = "4";
            }
        } else { // 2 atau 3
            if (y > 0) {
                kuadran = "2";
            } else {
                kuadran = "3";
            }
        } 

        System.out.println(String.format("x = %1$d, y = %2$d, Kuadran = %3$s", x, y, kuadran));
    }

    public static void nilaiSwitchCase(Scanner input) {
        System.out.println("Input nilai: ");
        int nilai = input.nextInt();
        // String huruf = switch (nilai) {
        //     case int i when i >= 85 -> "A";
        //     case int i when i >= 70 -> "B";
        //     case int i when i >= 55 -> "C";
        //     default -> "D";
        // };
        // Not supported, apparently. IM ON JAVA 25 AINT I
    }
}