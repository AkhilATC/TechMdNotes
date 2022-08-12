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

# Maven Repository

- Maven repository refers to the directories of packaged JAR files that contain metadata

- The metadata refers to the POM files relevant to each projects

- This metadata is allows mvn to download dependancies

### 3 types of repositories

1. Local Repository

2. Remote Repository

3. Central Repository





# Maven - pom

- All POM file require the __project__ element and 3 mandatory fields
	1. groupId
	2. artifactId
	3. version


```xml
<project xmlns = "http://maven.apache.org/POM/4.0.0"
   xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation = "http://maven.apache.org/POM/4.0.0
   http://maven.apache.org/xsd/maven-4.0.0.xsd">
   <modelVersion>4.0.0</modelVersion>
   <groupId>com.companyname.project-group</groupId>
   <artifactId>project</artifactId>
   <version>1.0</version>
</project>

```

## Build life cycles , Phases and Goals

- Build life cycles consist of a sequance of build phases 
and each build phase consists of a sequance of goals

- Each goal is responsible for a particular task

- When a phase is run all the goals related to that phase and its plugins
are also compiled


__Build life cycle__


3 build-in life cycles:

	1. Default
	2. Clean
	3. Site

Build phases :
1. compile
2. test-compile
3. test
4. package
5. integration-test
6. verify
7. install 
8. Deploy


