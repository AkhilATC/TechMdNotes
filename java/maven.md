# Maven

## create a mvn 
We can create a simple maven example by executing the archetype:generate command of mvn tool.

- ~/.m2/repository
```
    mvn archetype:generate 
    -DgroupId=groupid 
    -DartifactId=artifactid   
    -DarchetypeArtifactId=maven-archetype-quickstart 
    -DinteractiveMode=booleanValue 
# Example
mvn archetype:generate -DgroupId=com.akhil.one -DartifactId=DemoOne -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false 
```

## Compile a mvn project
```
mvn clean compile  
```
Now, you will see a lot of execution on the command prompt. If you check your project directory, target directory is created that contains the class files.

## Run a mvn project
- To run the project, go to the project directory\target\classes
```
java <package_name>.<class>  
# Example
java com.akhil.one.App
```
## Maven package
```
mvn package  
# create a jar file -target\DemoOne-1.0-SNAPSHOT.jar
```
Now you will see that a jar file is created inside the project/target directory.
You can also run the maven project by the jar file. To do so, go to the maven project directory.
```
java -classpath target\DemoOne-1.0-SNAPSHOT.jar;.; com.akhil.one.App
```

