import org.junit.Test;
import static org.junit.Assert.*;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class Soal1Test {

    @Test
    public void testIsLeapYear() {
        assertFalse(Soal1.isLeapYear(1957)); // tidak habis dibagi 4
        assertTrue(Soal1.isLeapYear(2012)); // habis dibagi 4, tidak 100 atau 400
        assertFalse(Soal1.isLeapYear(1900)); // dibagi 4 dan 100, tidak 400
        assertTrue(Soal1.isLeapYear(2000)); // dibagi 4, 100, dan 400
    }

    @Test
    public void testGetMonthName() {
        // mmf, saya nggak tau konvensi nulis test yg rapi
        assertEquals("Bulan Tidak Valid", Soal1.getMonthName(0)); // Jika invalid
        assertEquals("Januari", Soal1.getMonthName(1));
        assertEquals("Februari", Soal1.getMonthName(2));
        assertEquals("Maret", Soal1.getMonthName(3));
        assertEquals("April", Soal1.getMonthName(4));
        assertEquals("Mei", Soal1.getMonthName(5));
        assertEquals("Juni", Soal1.getMonthName(6));
        assertEquals("Juli", Soal1.getMonthName(7));
        assertEquals("Agustus", Soal1.getMonthName(8));
        assertEquals("September", Soal1.getMonthName(9));
        assertEquals("Oktober", Soal1.getMonthName(10));
        assertEquals("November", Soal1.getMonthName(11));
        assertEquals("Desember", Soal1.getMonthName(12));
        assertEquals("Bulan Tidak Valid", Soal1.getMonthName(13)); // Jika invalid(2)
    }

    @Test
    public void testGetDaysInMonth() {
        // tes kasus kabisat (feb)
        assertEquals(28, Soal1.getDaysInMonth(2, 1957)); // tidak habis dibagi 4
        assertEquals(29, Soal1.getDaysInMonth(2, 2012)); // habis dibagi 4, tidak 100 atau 400
        assertEquals(28, Soal1.getDaysInMonth(2, 1900)); // dibagi 4 dan 100, tidak 400
        assertEquals(29, Soal1.getDaysInMonth(2, 2000)); // dibagi 4, 100, dan 400

        // tes bulan lainnya
        assertEquals(31, Soal1.getDaysInMonth(1, 2025));
        assertEquals(31, Soal1.getDaysInMonth(3, 2025));
        assertEquals(30, Soal1.getDaysInMonth(4, 2025));
        assertEquals(31, Soal1.getDaysInMonth(5, 2025));
        assertEquals(30, Soal1.getDaysInMonth(6, 2025));
        assertEquals(31, Soal1.getDaysInMonth(7, 2025));
        assertEquals(31, Soal1.getDaysInMonth(8, 2025));
        assertEquals(30, Soal1.getDaysInMonth(9, 2025));
        assertEquals(31, Soal1.getDaysInMonth(10, 2025));
        assertEquals(30, Soal1.getDaysInMonth(11, 2025));
        assertEquals(31, Soal1.getDaysInMonth(12, 2025));

        // tes invalid
        assertEquals(0, Soal1.getDaysInMonth(-192, 2025));
        assertEquals(0, Soal1.getDaysInMonth(201, 2025));
    }


    //-----------------------------------------------------------//
    // Test Cases dibawah ini digunakan untuk mengetest main method
    // Silahkan dipelajari bagaimana cara menguji main method yang membutuhkan input output dari user
    // Anda tidak perlu melengkapi apapun pada test cases ini
    // namun anda harus memastikan bahwa test cases dibawah ini Pass
    //-----------------------------------------------------------//

    @Test
    public void testMainLeapYearFebruary() {
        String input = "2\n2024\n";
        ByteArrayInputStream in = new ByteArrayInputStream(input.getBytes());
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        System.setIn(in);
        System.setOut(new PrintStream(out));

        Soal1.main(new String[]{});

        String output = out.toString();
        assertTrue(output.contains("Masukkan Bulan (1-12):"));
        assertTrue(output.contains("Masukkan Tahun:"));
        assertTrue(output.contains("Februari 2024 memiliki 29 hari"));

        System.setIn(System.in);
        System.setOut(System.out);
    }

    @Test
    public void testMainNonLeapYearFebruary() {
        String input = "2\n2023\n";
        ByteArrayInputStream in = new ByteArrayInputStream(input.getBytes());
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        System.setIn(in);
        System.setOut(new PrintStream(out));

        Soal1.main(new String[]{});

        String output = out.toString();
        assertTrue(output.contains("Februari 2023 memiliki 28 hari"));

        System.setIn(System.in);
        System.setOut(System.out);
    }


    @Test
    public void testMainInvalidMonth() {
        String input = "13\n2024\n";
        ByteArrayInputStream in = new ByteArrayInputStream(input.getBytes());
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        System.setIn(in);
        System.setOut(new PrintStream(out));

        Soal1.main(new String[]{});

        String output = out.toString();
        assertTrue(output.contains("Bulan Tidak Valid 2024 memiliki 0 hari"));

        System.setIn(System.in);
        System.setOut(System.out);
    }
}