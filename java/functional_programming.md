# Functional programming (java.util.function)

Suppose we need to increment a number by one , normal way we define a
static function take number as argument and return increment that value by one
and return;

## Function<T,R>

- T - the type of the input to the function
- R - the type of the result of the function

```java
package FunctionalProgramming;

import java.util.function.Function;

public class Functional {

    public static void main(String[] args) {
        int number = 0;
        // Now we need to increment number by 1
        System.out.println(addByOne(number));
        // increment by 1 by functional approach
        int result = incrementByOneFunctional.apply(number);
        System.out.println(result);

    }
    static Function<Integer,Integer> incrementByOneFunctional = num -> num+1; // takes 1 argument and produce 1 result
    static int addByOne(int num){
        return num+1;
    }
}
```

### Chain functions

Suppose we need to run a function and then execute another d=function with that output, In such kind of scenario we can use .andThen.

```java
package FunctionalProgramming;

import java.util.function.Function;

public class Groot {

    public static void main(String[] args) {
        String groot = "Groot";
        // grootOut function first runs bindAvatar and then execute bindDialog 
        System.out.println(grootOut.apply(groot)); // Groot🌱: I'm grooott....!
    }
    
    // bind String with icon 
    static Function<String,String> bindAvatar = (x)->{ return x.concat("\uD83C\uDF31");};
    // // bind String with dialog 
    static Function<String,String> bindDialog = (x)->{ return x.concat(": I'm grooott....!");};
    // after bindAvatar ,andThen execute bindDialog
    static Function<String, String> grootOut =  bindAvatar.andThen(bindDialog);
}
```

## BiFunction<T,U,R>
 

- T - the type of the first argument to the function
- U - the type of the second argument to the function
- R - the type of the result of the function

```java
package FunctionalProgramming;

import java.util.function.BiFunction;

public class BiFunctional {

    public static void main(String[] args) {
        int number = 10;
        Integer res = addBy2AndMultiply.apply(10, 3);
        System.out.println(res);
    }
    
    static BiFunction<Integer,Integer,Integer> addBy2AndMultiply = (x,y) -> {
        return (x+2)*y;
    };
}
```


## Consumer<T>

Accept single input argument and return no result

```java
package FunctionalProgramming;

import java.util.function.Consumer;

public class ConsumerFunctional {

    public static void main(String[] args) {
        // normal approach
        Avenger avenger = new Avenger("Thor","You people are so petty, and tiny.");
        showAvenger(avenger);
        // Consumer Function interface
        showMessage.accept(avenger);

    }
    static Consumer<Avenger> showMessage = avenger -> {
        System.out.println(avenger.getName()+ " -> "+avenger.getMsg());
    };

    static void showAvenger(Avenger avenger){
        System.out.println(avenger.getName()+ " : "+avenger.getMsg());
    }

    static class Avenger{
        private String name;
        private String msg;

        public Avenger(String name, String msg) {
            this.name = name;
            this.msg = msg;
        }

        public void setName(String name) {
            this.name = name;
        }

        public void setMsg(String msg) {
            this.msg = msg;
        }

        public String getName() {
            return name;
        }

        public String getMsg() {
            return msg;
        }


    }
}
    
```
## BiConsumer<T,U>

```java
package FunctionalProgramming;

import java.util.function.BiConsumer;
import java.util.function.Consumer;

public class ConsumerFunctional {

    public static void main(String[] args) {
        // normal approach
        Avenger avenger = new Avenger("Thor","You people are so petty, and tiny.");
       
        // BiConsumer
        showMessageV2.accept(avenger,true);

    }
    

    static BiConsumer<Avenger,Boolean> showMessageV2= (avenger,isDisplay) ->{
        String head = isDisplay == true ? avenger.getName().concat("\uD83D\uDD28") : avenger.getName();
        System.out.println(head+" : "+avenger.getMsg());
    };

    

    static class Avenger{
        private String name;
        private String msg;

        public Avenger(String name, String msg) {
            this.name = name;
            this.msg = msg;
        }

        public void setName(String name) {
            this.name = name;
        }

        public void setMsg(String msg) {
            this.msg = msg;
        }

        public String getName() {
            return name;
        }

        public String getMsg() {
            return msg;
        }


    }
}
```
## Predicate<T>

```java
package FunctionalProgramming;

import java.util.List;
import java.util.function.Predicate;

public class PredicateFunctional {

    public static List<String> avengers = List.of("Thor", "Iron man", "Captain america");

    public static void main(String[] args) {
        System.out.println(isGodOfThunder.test("Thor"));
        System.out.println(isGodOfThunder.and(isString).test("Thor"));
    }

    static Predicate<String> isGodOfThunder = p -> {
        return avengers.contains(p) && p.startsWith("T");
    };
    static Predicate<String> isString = p -> {
        return p.length()>0;
    };


}
```

## Supplier<T>

You can return any kind of data, for example custom class, object,map,list;

```java

package FunctionalProgramming;

import java.util.function.Supplier;

public class SupplierFunctional {

    public static void main(String[] args) {
        // Supplier return results
        System.out.println(getUrlForBrowse.get());
    }
    // u can return any kind of values-> here we return String Value
    static Supplier<String> getUrlForBrowse = () ->{
        return "http://github/AkhilATC/";
    };

}

```
