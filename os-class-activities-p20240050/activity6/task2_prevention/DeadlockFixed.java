import java.util.concurrent.Semaphore;

class Account {
    String name;
    int balance;

    Account(String name, int balance) {
        this.name = name;
        this.balance = balance;
    }
}

class Transfer {

    static Semaphore mutex = new Semaphore(1);

    static void transfer(Account from, Account to, int amount) {

        try {

            mutex.acquire();

            System.out.println(
                    Thread.currentThread().getName()
                    + " entered critical section");

            Thread.sleep(1000);

            from.balance -= amount;
            to.balance += amount;

            System.out.println(
                    Thread.currentThread().getName()
                    + " transferred "
                    + amount
                    + " from "
                    + from.name
                    + " to "
                    + to.name);

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            mutex.release();
        }
    }
}

public class DeadlockFixed {

    public static void main(String[] args) throws Exception {

        Account A = new Account("Account-A", 1000);
        Account B = new Account("Account-B", 1000);

        int startingTotal = A.balance + B.balance;

        System.out.println("Starting total: " + startingTotal);

        Thread t1 = new Thread(
                () -> Transfer.transfer(A, B, 100),
                "Worker-1");

        Thread t2 = new Thread(
                () -> Transfer.transfer(B, A, 200),
                "Worker-2");

        t1.start();
        t2.start();

        t1.join();
        t2.join();

        int finalTotal = A.balance + B.balance;

        System.out.println("\nFinal A: " + A.balance);
        System.out.println("Final B: " + B.balance);
        System.out.println("Final total: " + finalTotal);

        System.out.println("No deadlock occurred");
    }
}
