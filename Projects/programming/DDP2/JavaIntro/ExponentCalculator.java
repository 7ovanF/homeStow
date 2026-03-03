
class ExponentCalculator {
    private static final double LN4 = 1.386294;
    private static final double EXP = 0.41;
    private static final long ITERS = 2000000000l;
    private static double result = 1.0; // e^0 = 1

    public static void main(String[] args) {
        double superman = 1.0;
        double x = LN4 * EXP;
        
        for (int i = 1; i < ITERS; i++) {
            superman = superman * x / i;
            result += superman;
        }
        
        System.out.println(result);
    }
}