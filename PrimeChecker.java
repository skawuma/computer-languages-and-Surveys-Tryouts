import java.util.Scanner;
/** Represents a  PrimeChecker.
 * @author Samuel Kawuma
 * @version 1.5
 * @date 9/1/24
 */


public class PrimeChecker {

      /** Calcualtes Factorial of given Integer Input.
     * @returns a  boolean , true if a number is prime
     * And false is a number is not a prime
     */
    public static boolean isPrime(int n) {
        if (n <= 1)                   return false;
        if (n <= 3)                   return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
          /**
         *  Creates Object of Scanner class
         */
        Scanner scanner = new Scanner(System.in);
        int number;
        do {
            System.out.print("Enter a positive number (0 or negative to exit): ");
            number = scanner.nextInt();
            if (number <= 0)     break;
            if (isPrime(number)) System.out.println(number + " is a prime number.");
            else                 System.out.println(number + " is not a prime number.");
        } while (true);
        scanner.close();
    }
}
