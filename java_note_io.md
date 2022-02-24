# JAVA IO
Java I/O (Input and Output) is used to process the input and produce the output. Java uses the concept of a stream to make I/O operation fast. The java.io package contains all the classes required for input and output operations.
Streams:
1. System.out: standard output stream
2. System. in : standard input stream
3. System.err: standard error stream

### FileOutputStream class

Java FileOutputStream is an output stream used for writing data to a file

```java
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

public class JavaIOWorkBook {
    public static void writeData() throws IOException {
        FileOutputStream fos = new FileOutputStream("src/one.txt");
        fos.write(65);// to write string data use s.getBytes() it will convert to byte array
        fos.close();
    }
    public static void main(String[] args) throws IOException {
        try{
            writeData();
        }catch (Exception e){
            e.printStackTrace();
        }

    }
}
```
### FileInputStream class
Java FileInputStream class obtains input bytes from a file
```java
public static void readData() throws IOException {
        FileInputStream fis = new FileInputStream("src/one.txt");
        byte[] outStr = fis.readAllBytes();
        for(byte b:outStr){
            System.out.print((char)b);
        }

    }
```

### BufferedOutputStream/BufferedInput Class
```java
// BufferedOutputStream
public static void bufferedWriteData(){
        try{
            FileOutputStream fOS = new FileOutputStream("src/one.txt");
            BufferedOutputStream bOS = new BufferedOutputStream(fOS);
            bOS.write("I'm here for you".getBytes(StandardCharsets.UTF_8));
            bOS.flush(); // It flushes the buffered output stream.
            bOS.close();
            fOS.close();
        }catch (Exception e){
            e.printStackTrace();
        }

    }
// BufferedInputStream
public static void readData() throws IOException {
        FileInputStream fis = new FileInputStream("src/one.txt");
        BufferedInputStream bIS = new BufferedInputStream(fis);
        try{
            byte[] c = bIS.readAllBytes();
            for(byte each:c){
                System.out.print((char) each);
            }
        }catch (Exception e){

        }finally {
            fis.close();
            bIS.close();
        }

    }
```
### SequenceInputStream 

Java SequenceInputStream class is used to read data from multiple streams. It reads data sequentially (one by one).
```java
public static void sequanceReader(){
        try{
            FileInputStream fIS_1 = new FileInputStream("src/one.txt");
            FileInputStream fIS_2 = new FileInputStream("src/two.txt");
            SequenceInputStream sIS = new SequenceInputStream(fIS_1,fIS_2);
            for(byte b:sIS.readAllBytes()){
                System.out.println((char) b);
            }
            fIS_1.close();
            fIS_2.close();
            sIS.close();
        }catch (Exception e){
            e.printStackTrace();
        }

    }
```
### ByteArrayOutputStream
Java ByteArrayOutputStream class is used to write common data into multiple files. In this stream, the data is written into a byte array which can be written to multiple streams later.








