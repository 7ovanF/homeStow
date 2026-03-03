public class LeowVincentVintizel {
    public static void main(String[] args) {
        double value = 2.0;
        double logResult = naturalLog(value);
        System.out.println(logResult);
    }
    
    public static double naturalLog(double x) {
        double b = x - 1;
        double a = b;
        double result = b;
        
        for (int i = 2; i < 10000; i++) {
            a = a * b * (1 - i) / i;
            result += a;
        }
        
        return result;
    }
}