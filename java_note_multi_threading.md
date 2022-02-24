# Multithreading in Java

Multithreading in Java is a process of executing multiple threads simultaneously.

## Java Thread methods

- start() // starts execution of threads
- run() // do an action for a thread.
- sleep() // sleep a thread for a fixed time - access modifier is static
- currentThread() // It returns a reference to the currently executing thread object. (static)
- join() // It waits for a thread to die.

# Java Program for Demonstrating Thread States
```java
public class InitClass implements Runnable{

    private final String tName;

    public InitClass(String tName){
        this.tName = tName;
    }
    @Override
    public void run() {
        System.out.println("In-side of InitClass run method");
        System.out.println("=== === ===");
        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Thread Execution done"+Thread.currentThread().getState());
        System.out.println("--->>>>"+this.tName);
    }

    public static void main(String[] args) throws InterruptedException {
        Thread t = new Thread(new InitClass("Akhil"));
        Thread t2 = new Thread(new InitClass("T Cheriyan"));
        System.out.println(t.getState());
        System.out.println(t2.getState());
        System.out.println("==================");
        t.start();
        System.out.println("Thread 1 status"+ t.getState());
        t2.start();
        System.out.println("Thread 2 status"+ t2.getState());
        t2.join();
        System.out.println("final state of t2"+t2.getState());


    }
}
```
## How to create a thread in Java

There are two ways to create a thread:
1. By extending Thread class
```java
public class TheadExtenderClass extends Thread{

    public TheadExtenderClass(){
        System.out.println("✨ ---- Constructor invocation ---- ✨");
    }

    @Override
    public void run() {
        System.out.println("Thread --->>> Started "+Thread.currentThread().getState());
    }

    public static void main(String[] args) {
        TheadExtenderClass tEC =  new TheadExtenderClass();
        tEC.start();
        tEC.run();
    }
}
```
2. By implementing Runnable interface.
```java
public class RunableThreadExample implements Runnable {

    @Override
    public void run() {
        System.out.println("---- Thread rununing initiated ----");
    }

    public static void main(String[] args) {
        System.out.println("-------");
        RunableThreadExample rTE = new RunableThreadExample();
        Thread t = new Thread(rTE,"Akhil");
        Thread t2 = new Thread(rTE,"T C");
        System.out.println(t.getName());
        System.out.println(t2.getName());
        System.out.println("================");
        t.start();
        t2.start();
    }
}
```
## Thread Scheduler in Java

A component of Java that decides which thread to run or execute and which thread to wait is called a thread scheduler in Java.

## Daemon Thread in Java

Daemon thread in Java is a service provider thread that provides services to the user thread. 
```java
public class DemonThread extends Thread{

    @Override
    public void run() {
        System.out.println("i'm "+Thread.currentThread().getName());
        System.out.println("====>>>> Run following Thread is a daemon " + Thread.currentThread().isDaemon());
    }

    public static void main(String[] args) {
        new DemonThread().start();
        Thread t = new Thread(new DemonThread());
        t.setName("Daemon \uD83D\uDC7F");
        t.setDaemon(true);
        t.start();

    }
}
```
## Java Thread Pool
Java Thread pool represents a group of worker threads that are waiting for the job and reused many times.
```java
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Executor;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ThreadPoolExecution implements Runnable{
    private String Messager;
    ThreadPoolExecution(String msgr){
        this.Messager = msgr;
    }
    @Override
    public void run() {
        System.out.println("--- Run ---");
        System.out.println(this.Messager);
    }

    public static void main(String[] args) {
        ExecutorService eS = Executors.newFixedThreadPool(2);

        List<String> listOfName = new ArrayList<>();
        listOfName.add("I'm Monster : \uD83D\uDC7F");
        listOfName.add("I'm tried : \uD83D\uDE2B" );
        listOfName.add("I'm Aliean : \uD83D\uDC7E");

        for(String each: listOfName){
            Runnable worker = new ThreadPoolExecution(each);
            eS.execute(worker);
        }
        eS.shutdown();
        System.out.println(eS.isTerminated());

    }

}
```

## ThreadGroup in Java

Java provides a convenient way to group multiple threads in a single object. In such a way, we can suspend, resume or interrupt a group of threads by a single method call.
```java
public class ThreadGroupDemo implements Runnable{
    @Override
    public void run() {
        System.out.println("Runnning Thread = "+Thread.currentThread().getName());
    }

    public static void main(String[] args) {
        ThreadGroup tGMain = new ThreadGroup("MAIN GROUP");
        Thread t = new Thread(tGMain,new ThreadGroupDemo(),"INIT");
        Thread t2 = new Thread(tGMain,new ThreadGroupDemo(),"Second");
        Thread t3 = new Thread(tGMain,new ThreadGroupDemo(),"third");
        t.start();
        t2.start();
        t3.start();
    }
}

```
## Java Shutdown Hook
In nutshell, the shutdown hook can be used to perform cleanup resources or save the state when JVM shuts down normally or abruptly. Performing clean resources means closing log files, sending some alerts, or something else. So if you want to execute some code before JVM shuts down, use the shutdown hook.

## Synchronization in Java
Synchronization in Java is the capability to control the access of multiple threads to any shared resource.
There are two types of thread synchronization mutual exclusive and inter-thread communication.

1. Mutual Exclusive
    - Synchronized method.
    - Synchronized block.
    - Static synchronization.
2. Cooperation (Inter-thread communication in java)


#### Synchronized method.

```java
/** Shared object class **/
public class SharedObjectClass {

    synchronized void printAvatar(int numberOftimes,String tName){
        System.out.println("Print Avatar");
        for(int i=0;i<numberOftimes;i++){
            System.out.println(i + " ---->>> "+"\uD83D\uDC7E"+" from "+tName);
        }
    }
    
}
```
SharedObjectClass have a synchronized method called printAvatar. 
```java
public class SyncJavaExample2  implements Runnable{

    public SharedObjectClass SOC;
    SyncJavaExample2(SharedObjectClass SOC){
        this.SOC = SOC; // consume SharedObjectClass resource
    }

    @Override
    public void run() {
        System.out.println("Thread is running ->"+Thread.currentThread().getName());
        this.SOC.printAvatar(3,Thread.currentThread().getName().toString());
    }

    public static void main(String[] args) {

    }
}

public class SyncjavaExample implements Runnable{
    public SharedObjectClass SOC;
    SyncjavaExample(SharedObjectClass SOC){
            this.SOC = SOC;
    }

    @Override
    public void run() {
        System.out.println("Thread is running ->"+Thread.currentThread().getName());
        this.SOC.printAvatar(5,Thread.currentThread().getName().toString());
    }

    public static void main(String[] args) {
        Thread t = new Thread(new SyncjavaExample(new SharedObjectClass()));
        t.setName("Thread One");
        t.start();
    }
}
public class DemonThread {
    public static void main(String[] args) {

        SharedObjectClass ob = new SharedObjectClass(); // object of SharedObjectClass
        SyncjavaExample sJE1 = new SyncjavaExample(ob);
        SyncJavaExample2 sjE2 = new SyncJavaExample2(ob);
        Thread t1 = new Thread(sJE1);
        t1.setName("Thread ONE ");
        Thread t2 = new Thread(sjE2);
        t2.setName("Thread TWO ");
        t1.start();
        t2.start();

    }
}

```
#### Syncronized block
```java
 void printTable(int n){    
   synchronized(this){//synchronized block    
     for(int i=1;i<=5;i++){    
      System.out.println(n*i);    
      try{    
       Thread.sleep(400);    
      }catch(Exception e){System.out.println(e);}    
     }    
   }    
 }//end of the method    
} 
```
---
#### Static Synchronization
If you make any static method as synchronized, the lock will be on the class not on object.

# Inter-thread Communication in Java

Inter-thread communication or Co-operation is all about allowing synchronized threads to communicate with each other.It is implemented by following methods of Object class:
    - wait()
    - notify()
    - notifyAll()
    
```java 
// Example
public class InterCommunicationResourses {

    public boolean isReady = false; // 

    public synchronized void initiateLaunching(){
        System.out.println(isReady);
        System.out.println("--- --- --- ---- ----");
        System.out.println("Connecting Ground \uD83D\uDCDF");
        if(!isReady){
            try{
                System.out.println("--- Waiting for Ground clearance ----");

                wait();
            }catch (Exception e){

            }
        }
        this.launchVechcle();

    }

    public synchronized void clearForLaunch(){
        System.out.println("--- Ground Response: Checking Stable Conditions ---");
        System.out.println(" Weather : "+"✅");
        System.out.println(" Fuel Monetizing : "+"✅");
        System.out.println(" System : "+"✅");
        System.out.println("Cleared... Confirm ✅ ✅ ✅");
        System.out.println("+++++++++++++++++");

        this.isReady = true;
        notify();
    }

    public void launchVechcle(){
        System.out.println("--- Start countdown ---");
        for(int i=10;i>=0;i--){
            System.out.println("⏲️: "+i);
            if(i==1){
                System.out.println("Ignition Started \uD83D\uDD25");
            }
        }
        System.out.println("==== ===== ==== Lift Off ==== ==== ====");
        System.out.println("\uD83D\uDE80");
    }

    public static void main(String[] args) {
    }

}
```
---
```
Above Class InterCommunicationResourses includes a public variable isReady , and two syncronized functions
- initiateLaunching()
- clearForLaunch()
if(!isReady) : wait() intialted, clearForLaunch change bit value and call notify(), it will continue remaining thread execution
```

```java
public class LaunchRocketWithThreadCommunication {

    public static void main(String[] args) {
        final InterCommunicationResourses iCRs = new InterCommunicationResourses();
        Thread liftOff = new Thread(){
            public void run(){
                iCRs.initiateLaunching();
            }
        };
        liftOff.start()// call initiateLaunching(); wre isReady is false and enter into wait()
        try {
            Thread.sleep(1000);
        }catch (Exception e){
            System.out.println("----");
        }
        Thread clearForLiftOff = new Thread(){
            public void run(){
                iCRs.clearForLaunch();
            }
        };

        clearForLiftOff.start();// After clearForLaunch will notify and continue thread 1 execution
    }
}

```
---
``` Output
false
--- --- --- ---- ----
Connecting Ground 📟
--- Waiting for Ground clearance ----
--- Ground Response: Checking Stable Conditions ---
 Weather : ✅
 Fuel Monetizing : ✅
 System : ✅
Cleared... Confirm ✅ ✅ ✅
+++++++++++++++++
--- Start countdown ---
⏲️: 10
⏲️: 9
⏲️: 8
⏲️: 7
⏲️: 6
⏲️: 5
⏲️: 4
⏲️: 3
⏲️: 2
⏲️: 1
Ignition Started 🔥
⏲️: 0
==== ===== ==== Lift Off ==== ==== ====
🚀

Process finished with exit code 0
```

#### Interrupting a Thread

If any thread is in sleeping or waiting state (i.e. sleep() or wait() is invoked), calling the interrupt() method on the thread, breaks out the sleeping or waiting state throwing InterruptedException. 









