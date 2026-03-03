import java.util.Scanner;
public class Worksheet5{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final int MAX_PERCOBAAN = 3;
        int percobaan = 0;
        boolean loginBerhasil = false;
        // this is a method candidate
        while (percobaan < MAX_PERCOBAAN && !loginBerhasil) {
            System.out.print("Username: "); String user = sc.nextLine();
            System.out.print("Password: "); String pass = sc.nextLine();
            if (isValidLogin(user, pass)) {
                loginBerhasil = true;
                System.out.println("Sukses!");
                int score = checkPassScore(pass);
            }
        }
        if (percobaan == MAX_PERCOBAAN) {
            System.out.println("Akun Terkunci!");
        }
        sc.close();
    }
    public static boolean isValidLogin(String username, String password) {
        final String VALID_USERNAME = "admin";
        final String VALID_PASSWORD = "password";
        if (username.equals(VALID_USERNAME) && password.equals(VALID_PASSWORD)) {
            return true;
        } else {
            return false;
        }
    }
    
    public static int checkPassScore(String pass) {
        /* ideas:
         * - put these into methods (but how? there are a lot of shared variables. returning
         *   "melebihiMinimal", "tanpaSpasi" etc in one go wont do)
         * - plus this doesnt look "1 thing per method"
         * - alternative: group validations by criteria instead, so new criterias wont be spread
         *   across validation, score incrementing, printing. but that doesnt really fulfill "do 
         *   one thing at a time" does it
         */
        // check criterias
        boolean melebihiMinimal = pass.length() >= 6;
        boolean tanpaSpasi = !pass.contains(" ");
        boolean adaHuruf = false; boolean adaAngka = false;
        for (int i = 0; i < pass.length(); i++) {
            char c = pass.charAt(i);
            if (Character.isLetter(c)) {
                adaHuruf = true;
            }
            if (Character.isDigit(c)) {
                adaAngka = true;
            }
        }
        // count score based on checks
        int score = 0;
        if (melebihiMinimal) score++;
        if (tanpaSpasi) score++;
        if (adaHuruf) score++;
        if (adaAngka) score++;
        // print out suggestions
        if (!melebihiMinimal) System.out.println("- minimal 6 karakter");
        if (!tanpaSpasi) System.out.println("- jangan memakai spasi");
        if (!adaHuruf) System.out.println("- harus punya minimal 1 huruf");
        if (!adaAngka) System.out.println("- harus punya minimal 1 angka");
        return score;
    }

}
