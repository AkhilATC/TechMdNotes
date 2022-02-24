# Serialization and Deserialization in Java

__Serialization__: 📜 [object] ---> ⚙️ [Converted] ---> 🔢[Byte Stream]  
__Deserialization__: 🔢[Byte Stream]  ---> ⚙️ [Converted] ---->📜 [object]

>➡️ Serializable is a marker interface (has no data member and method). It is used to "mark" Java classes so that the objects of these classes may get a certain capability.
➡️ The Serializable interface must be implemented by the class whose object needs to be persisted.
➡️ For serializing the object, we call the writeObject() method of ObjectOutputStream class, and for deserialization we call the readObject() method of ObjectInputStream class.
---
__Serialization Example__
```java
import java.io.Serializable;

public class SerializableClassMonkey implements Serializable {
    public String bananaIcon = "\uD83C\uDF4C";
    public String titleTag;
    public int holdingNumber;
    public String bananaNum;
    SerializableClassMonkey(String titleTag,int holdingNumber){
        this.titleTag = titleTag;
        this.bananaNum = this.bananaIcon+"("+holdingNumber+")";
        this.holdingNumber = holdingNumber;

    }
}
// JavaIOWorkBook class -> writeObject() using ObjectOutputStream
import java.io.*;
import java.nio.charset.StandardCharsets;

public class JavaIOWorkBook {
    public static String fileOne = "src/one.txt";
    public static void main(String[] args) throws IOException {
        try{

            SerializableClassMonkey monkey = new SerializableClassMonkey("Mr tooky",10);
            FileOutputStream FOS = new FileOutputStream(fileOne);
            ObjectOutputStream obOS = new ObjectOutputStream(FOS);
            obOS.writeObject(monkey);// monkey object write
            obOS.flush();
            obOS.close();
        }catch (Exception e){
            e.printStackTrace();
        }

    }
}
```
---
__Deserialization Example__
```java
 public static void main(String[] args) throws IOException {
        try{

            FileInputStream FIS = new FileInputStream(fileOne);
            ObjectInputStream oIS = new ObjectInputStream(FIS);
            SerializableClassMonkey obj = (SerializableClassMonkey)oIS.readObject();// readObject cast as SerializableClassMonkey object
            System.out.println(obj.titleTag); // Mr tooky
            System.out.println(obj.bananaNum); // 🍌(10)
            System.out.println(obj.holdingNumber); // 10
        }catch (Exception e){
            e.printStackTrace();
        }

    }
```

__NB__: If you don't want to serialize any data member of a class, you can mark it as transient.
