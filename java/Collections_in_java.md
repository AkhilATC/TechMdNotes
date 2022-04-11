# Collections in Java
The Collection in Java is a framework that provides an architecture to store and manipulate the group of objects.

1. Interfaces
    - Set
    - List
    - Queue
    - Deque
2. Classes
    - ArrayList
    - Vector
    - LinkedList
    - PriorityQueue 
    - HashSet
    - LinkedHashSet
    - TreeSet

## List Interface
>ArrayList,LinkedList,Vector,Stack uses List Interface
```java
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Stack;
import java.util.Vector;

public class JavaCollectionsWalkThrough {

    public static void main(String[] args) {
        /*2.ArrayList
            Duplicate and different type store
            Insertion order and not syncronized
         */
        ArrayList<String> marvelList = new ArrayList<String>();
        marvelList.add("Iron man");
        marvelList.add("Captain America");
        marvelList.add("Thor");
        for (Object marvel: marvelList){
            System.out.println(marvel);

        }

        /*2.LinkedList
            Store duplicate,
            Insertion order and not syncronized
            manipulation is fast
        *  */
        LinkedList<String> listOfGodInMarvels = new LinkedList<String>();
        listOfGodInMarvels.add("Thor");
        listOfGodInMarvels.add("Loki");
        System.out.println(listOfGodInMarvels);
        /*3.Vector
        syncronized
         */
        Vector<String> hailHydra = new Vector<>();
        hailHydra.add("----");
        hailHydra.add("Hydra");
        System.out.println(hailHydra);
        /*Stack
        LIFO,

         */
        Stack<String> peterParker = new Stack<>();
        peterParker.push("Andrew");
        peterParker.push("Tom");
        peterParker.push("Zendiya");
        peterParker.pop();
        System.out.println(peterParker);
    }
}
```
## Queue Interface
> PriorityQueue, Deque, and ArrayDeque which implements the Queue interface.
```java
PriorityQueue priortyQ = new PriorityQueue(); 
//In Deque, we can remove and add the elements from both the side.
Deque<String> deque = new ArrayDeque<String>();  

```
## Set Interface
>Set is implemented by HashSet, LinkedHashSet, and TreeSet.
```java
HashSet<String> set=new HashSet<String>();  
LinkedHashSet<String> set=new LinkedHashSet<String>(); 
TreeSet<String> set=new TreeSet<String>();  
```



