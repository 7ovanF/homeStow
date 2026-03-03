import org.junit.Test;
import static org.junit.Assert.*;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class AutomorphTest {

    @Test
    public void testGetLastDigits() {
        // Normal cases
        assertEquals(57, Automorph.getLastDigits(1957, 2));
        assertEquals(201, Automorph.getLastDigits(19201, 3));

        // Kepanjangan
        assertEquals(32, Automorph.getLastDigits(32, 21));

        // Negatif
        assertEquals(217, Automorph.getLastDigits(-5217, 3));

        // 0
        assertEquals(0, Automorph.getLastDigits(0, 4));
    }

    @Test
    public void testPower() {
        assertEquals(9, Automorph.power(3, 2));
        assertEquals(1024, Automorph.power(2, 10));

        assertEquals(-729, Automorph.power(-9, 3));
        assertEquals(9, Automorph.power(-3, 2));
    }
}
