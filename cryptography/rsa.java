import java.lang.*;

class RSA {
    public static boolean isPrime(int num) {
        boolean prime = true;
        for (int i = 2; i <= num / 2; i++) {
            if (num % i == 0) {
                prime = false;
                break;
            }
        }
        return prime;
    }
    
    public static void findPrimeFactors(int num) {
        for (int i = 1; i <= num; i++) {
            if (num % i == 0 && isPrime(i)) {
                System.out.print(i + " ");
            }
        }
    }
    
    public static int findPrivateKey(int e, int p, int q) {
        int d = 0;
        while ((e * d) % ((p - 1) * (q - 1)) != 1) {
            d++;
        }
        return d;
    }
    
    public static void main(String[] args) {
        System.out.println("RSA");
    }
}