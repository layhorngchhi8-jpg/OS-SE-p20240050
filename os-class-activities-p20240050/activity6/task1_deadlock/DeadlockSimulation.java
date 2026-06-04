import java.util.concurrent.Semaphore;

class Account {
    String name;
    int balance;
    Semaphore lock = new Semaphore(1);

    Account(String name, int balance) {
        this.name = name;
        this.balance = balance;
    }
}

class Transfer {

    static volatile boolean completed = false;

    static void transfer(Account from, Account to, int amount) {

        try {

            System.out.println(Thread.currentThread().getName()
                    + " locking " + from.name);

            from.lock.acquire();

            System.out.println(Thread.currentThread().getName()
                    + " acquired " + from.name);

            Thread.sleep(1000);

            System.out.println(Thread.currentThread().getName()
                    + " waiting for " + to.name);

            to.lock.acquire();

            from.balance -= amount;
            to.balance += amount;

            completed = true;

            System.out.println(Thread.currentThread().getName()
                    + " transfer completed");

            to.lock.release();
            from.lock.release();

        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

public class DeadlockSimulation {

    public static void main(String[] args) throws Exception {

        Account A = new Account("Account-A", 1000);
        Account B = new Account("Account-B", 1000);

        System.out.println("Starting Balances:");
        System.out.println("A = " + A.balance);
        System.out.println("B = " + B.balance);

        Thread t1 = new Thread(
                () -> Transfer.transfer(A, B, 100),
                "Worker-1");

        Thread t2 = new Thread(
                () -> Transfer.transfer(B, A, 200),
                "Worker-2");

        t1.start();
        t2.start();

        Thread.sleep(5000);

        if (!Transfer.completed) {

            System.out.println("\nDeadlock detected: transactions are stuck");

            System.out.println("Worker-1 is waiting for Account-B");
            System.out.println("Worker-2 is waiting for Account-A");
        }
    }
}
