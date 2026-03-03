public class Automorph {
    public static boolean isAutomorphic(int n) {
        int i=1;
        while (i<n) i*=10;
        return (n*n-n) % i == 0;
    }
}
