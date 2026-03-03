import java.util.Scanner;

public class Soal1 {

    public static void main(String[] args) {
        // Asumsi data type input valid & yg dites hanya valuenya
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan Bulan (1-12): ");
        int month = input.nextInt();
        System.out.print("Masukkan Tahun: ");
        int year = input.nextInt();

        System.out.printf("%s %d memiliki %d hari", getMonthName(month), year, getDaysInMonth(month, year));

        input.close();
    }

    public static boolean isLeapYear(int year) {
        return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
    }

    public static String getMonthName(int month) {
        String[] monthNameArray = new String[] {
            "Januari",
            "Februari",
            "Maret",
            "April",
            "Mei",
            "Juni",
            "Juli",
            "Agustus",
            "September",
            "Oktober",
            "November",
            "Desember"
        };
        if (month < 1 || month > 12) {
            return "Bulan Tidak Valid";
        }
        return monthNameArray[month - 1];
    }

    public static int getDaysInMonth(int month, int year) {
        /**
         * Januari = 31, Feb = 28/29, Mar = 31, Apr = 30, Mei = 31, Jun = 30,
         * Jul = 31, Aug = 31, Sept = 30, Okt = 31, Nov = 30, Des = 31
         */
        if (month == 2) {
            if (isLeapYear(year)) {
                return 29;
            } else {
                return 28;
            }
        } else if (month == 1 || month == 3 || month == 5
            || month == 7 || month == 8 || month == 10 || month == 12
        ) {
            return 31;
        } else if (month == 4 || month == 6
            || month == 9 || month == 11
        ) {
            return 30;
        }
        return 0;
    }
}