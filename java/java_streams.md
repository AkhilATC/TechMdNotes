## java stream example
```java
package declarative;

import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

public class JavaStreams {

    public static List<Movies> getMovies(){

        return List.of(
                new Movies("Rang de basanti","Rakeysh Omprakash Mehra",Language.HINDI,2006),
                new Movies("KGF chapter 1","Prashanth neel",Language.KANNADA,2018),
                new Movies("KGF chapter 2","Prashanth neel",Language.KANNADA,2022),
                new Movies("Lucifer","Prithviraj",Language.MALAYALAM,2019),
                new Movies("Anbe Sivam","Sundar C.",Language.TAMIL,2003),
                new Movies("Ustad Hotel","Anwar Rasheed",Language.MALAYALAM,2012)
        );
    }


    public static void main(String[] args) {

        List<Movies> movies = getMovies();

        // Filter - filter out a condition
        List<Movies> kannadaMovies = movies.stream()
                .filter(movie -> movie.getLanguage().equals(Language.KANNADA))
                .collect(Collectors.toList());
        System.out.println("Filter - Language == kannada");
        kannadaMovies.forEach(System.out::println); // list of kannada movies

        // Sort - sort by director's name
        // sort in reverse order , ==> Comparator.comparing(Movies::getDirectorName).reversed()
        List<Movies> sortedMovies = movies.stream()
                .sorted(Comparator.comparing(Movies::getDirectorName))
                .collect(Collectors.toList());
        System.out.println("Sorted movies by director's name..");
        sortedMovies.forEach(System.out::println);

        // All Match - check a condition on streams
        // Suppose all movieName is not empty
        boolean isNotEmpty = movies.stream().allMatch(p -> !p.getName().isEmpty());
        System.out.println("Found that movies doesn't contain empty string-> "+isNotEmpty);

        // Any Match - check predicate at least one match

        boolean isP_preFix = movies.stream().anyMatch(m->m.getName().startsWith("P"));
        System.out.println("Is any movie name start with prefix P -> " + isP_preFix);
        // None Match - check predicate not match for all elements
        boolean is = movies.stream().noneMatch(p -> p.getName().isEmpty());
        System.out.println(is);

        // Min - find a min from stream with a criteria
        Optional<String> oldMovie = movies.stream()
                .min(Comparator.comparing(Movies::getYear))
                .map(p -> p.getName());
        System.out.println("Old release -> " + oldMovie.orElse(null));

        // Max - find a max
        Optional<String> recentMovie = movies.stream()
                .max(Comparator.comparing(Movies::getYear))
                .map(p -> p.getName());
        System.out.println("Recent release -> " + recentMovie.orElse(null));

        // Group
        Map<String, List<Movies>> groups = movies.stream()
                .collect(Collectors.groupingBy(m -> m.getDirectorName()));
        groups.forEach((s, movies1) -> {
            System.out.println(s);
            movies1.forEach(System.out::println);
        });
    }
}
```
