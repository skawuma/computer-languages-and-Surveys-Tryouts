import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        fact();
    }

    public static void fact() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a positive Integer: ");
        int n = scanner.nextInt();
        
        while (n < 0) {
            System.out.print("Sorry, only positive numbers, enter again: ");
            n = scanner.nextInt();
        }
        
        if (n == 0) {
            System.out.println("The factorial of 0 is 1");
        } else {
            int f = 1;
            for (int i = 1; i <= n; i++) {
                f *= i;
            }
            System.out.println("The factorial of " + n + " is " + f);
        }
        scanner.close();
    }
}

