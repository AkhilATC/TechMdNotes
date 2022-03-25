
ObjectMapper is one of the most important class available in the Jackson library. 
It is used to read and write JSON data. 
It is responsible for reading data from or to POJO file and to and from a JSON Tree Model.
```pom
<dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>2.11.1</version>
        </dependency>
```
Suppose we have a Student.class as POJO
```java
public class Student {
    private String nameIs;
    private String age;
    private String className;

    public String getNameIs() {
        return nameIs;
    }

    public String getAge() {
        return age;
    }

    public String getClassName() {
        return className;
    }

    public void setNameIs(String nameIs) {
        this.nameIs = nameIs;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public void setClassName(String className) {
        this.className = className;
    }
}
```
----
```java

public class ObjectMap {

    public static void main(String[] args) throws JsonProcessingException {
        ObjectMapper mapper = new ObjectMapper();
        String onjInput = "{\"nameIs\":\"akhil\",\"age\":\"33\",\"className\":\"sss\"}";
        Student students = mapper.readValue(onjInput, Student.class);
        System.out.println(students);
        // serialize students into json string
        onjInput = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(students);
        System.out.println(onjInput);
    }
}
//output
/**{
  "nameIs" : "akhil",
  "age" : "33",
  "className" : "sss"
}**/

```

