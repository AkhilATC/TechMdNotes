# Spring boot

pom.xml for spring boot app
```pom
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.4.0</version>
    <relativePath/> <!-- lookup parent from repository -->
  </parent>
  <groupId>com.akhil.one</groupId>
  <artifactId>DemoOne</artifactId>
  <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>DemoOne</name>
  <url>http://maven.apache.org</url>
  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter</artifactId>
    </dependency>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-test</artifactId>
      <scope>test</scope>
    </dependency>
  </dependencies>
  <build>
    <plugins>
      <plugin>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
        <version>${project.parent.version}</version>
      </plugin>
    </plugins>
  </build>
</project>

```
```java
package com.akhil.one;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Hello world!
 *
 */
@SpringBootApplication
public class App 
{
    public static void main( String[] args )
    {
        SpringApplication.run(App.class,args);
    }
}
```


### @RestController in nutshell

The @RestController annotation is a convenience notation that combines __@Controller__ with ___@ResponseBody___ into a single descriptive annotation, simplifying your code
and making intent more obvious. Once we’ve annotated a class as an @RestController , we can begin creating our REST API.

### @RequestMapping

```java
@RequestMapping(value = "/coffees", method = RequestMethod.GET)
```
> Problem: An error was reported to @RestController in idea: Cannot Resolve Symbol RestController
> solution is:

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```
 
- path is specfied as value
- Http method specfied in method

@RequestMapping has several specialized convenience annotations:
1. @GetMapping
2. @PostMapping
3. @PutMapping
4. @PatchMapping
5. @DeleteMapping

### code example

```java
// restController annotation
@RestController
public class SemOwlModule {
    @RequestMapping("/")
    public String helloWorld(){
        return "Hello wrold";
    }
    // RequestMapping annotation
    @RequestMapping(value = "/list_heros", method = RequestMethod.GET)
    public ArrayList listOfHeros(){
        ArrayList<String> a = new ArrayList<String>();
        a.add("Spider Man \uD83D\uDD77");
        a.add("Thor \uD83D\uDD28");
        return a;
    }  
}
```
__@PathVariable__ annotation used get value passed as url params
```java
@GetMapping("/say_my_name/{name}")
    public String sayName(@PathVariable String name){
        return "Hello "+ name;
    }
```
__@RequestBody__ annotation used to pass payload for api

## Application Configuration

Spring Boot applications supply a variety of powerful mechanisms for developers to
dynamically configure and reconfigure their applications, even while the app is run‐
ning.

1. __*@Value*__

We can add properties in application.properties, that located in resources folder.example: App-name="DEMO APP"
> Can't declare @value annotation locally, its globally defined
```java
 @Value("${App-name}")
 public String appName;// globel intilaization
```
> @Value("${App-name:default-app-name}") provide default name

2. __*@ConfigurationProperties*__

Using @ConfigurationProperties , a developer can define properties, group related properties.

> @ConfigurationPropertiesScan annotation required main application,
> add `spring-boot-configuration-processor` dependancy in pom

```java
# pom.xml
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-configuration-processor</artifactId>
<optional>true</optional>
</dependency>
```

example:
```java
@SpringBootApplication
@ConfigurationPropertiesScan
public class SemParseApplication {

	@Bean
	@ConfigurationProperties(prefix = "config")
	SettingUps createSetups() {
		return new SettingUps();
	}

	public static void main(String[] args) {
		SpringApplication.run(SemParseApplication.class, args);
	}

}
# application.properties
config.appId="1000"
config.appName="fdfdfd"
settingUps class is a PoJo with public varibles appId,appName
-----------
api expose class initalize a object of pojo class from its constructor, 
we can access the configuration varibales via that object

```
## Example

Dependancies
- spring-boot-starter-web (spring web application)
- spring-boot-starter-thymeleaf (HTML template engine)
- spring-boot-starter-data-jpa (Data presistance)
- H2 database

> 1. create a domain class.
- @Entity , @Id , and @GeneratedValue annotations so this class gets marked as JPA entity and can be
persisted to the database.
- This class has two constructors, one with no arguments and
is needed for the JPA engine and the other with some arguments that you are going to use to populate the
database.
```java
@Entity
public class Avengers {
    @Id
    @GeneratedValue(strategy= GenerationType.AUTO)
    private Long id;

    private String heroName;
    private String heroIcon;
    private String heroWeapon;
    public Avengers(){

    }
    public Avengers(String heroName, String heroIcon, String heroWeapon) {
        this.heroName = heroName;
        this.heroIcon = heroIcon;
        this.heroWeapon = heroWeapon;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getHeroName() {
        return heroName;
    }

    public void setHeroName(String heroName) {
        this.heroName = heroName;
    }

    public String getHeroIcon() {
        return heroIcon;
    }

    public void setHeroIcon(String heroIcon) {
        this.heroIcon = heroIcon;
    }

    public String getHeroWeapon() {
        return heroWeapon;
    }

    public void setHeroWeapon(String heroWeapon) {
        this.heroWeapon = heroWeapon;
    }
    // toString method required
    public String toString(){
        String resp = this.heroName + this.heroIcon;
        return resp.toString();
    }

}
```
> 2. Create a interface that extending JpaRepository

```java
package com.OntoParserModule.ParseOwl;

import org.springframework.data.jpa.repository.JpaRepository;
/**
you need to create a persistence mechanism for the journal data. You
are going to use the Spring Data JPA technology by creating an interface and
extending it from the JpaRepository interface.
**/
public interface AvengersPresistanceLayer extends JpaRepository<Avengers,Long>{
}
```

> 3. Create a web controller class
- @Controller , which is a marker for the Spring MVC engine so this class is treated as web
controller.
- The @Autowired annotation will instantiate the JournalRepository variable aPL, so it can be
used in the index method.
```java
package com.OntoParserModule.ParseOwl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

// @Controller , which is a marker for the Spring MVC engine so this class is treated as web controller
@Controller
public class AvengersWebController {
    //The @Autowired annotation will instantiate the JournalRepository variable repo, so it can be
    //used in the index method.
    @Autowired
    AvengersPresistanceLayer aPL;

    @RequestMapping("/")
    public String index(Model model){

        System.out.println(aPL.findAll());

        model.addAttribute("Avengers", aPL.findAll());
        // model.addAttribute pass data to html - index.html,
        return "index";
    }
}
```
> 4. Initializing bean in application.java

- saveData method that is returning an InitializingBean . This particular class is always called when the Spring engine is
creating the instance to initialize it. In this case, the method will be executed before the application finishes
running.

```java
@SpringBootApplication
public class ParseOwlApplication {
	@Bean
	InitializingBean saveDb(AvengersPresistanceLayer aPL){
		return () ->{
			aPL.save(new Avengers("Captian America","\uD83E\uDDE2","Sheild"));
			aPL.save(new Avengers("Iron man","\uD83E\uDDE5", "Suite"));
		};

	}
	public static void main(String[] args) {
		SpringApplication.run(ParseOwlApplication.class, args);
	}

}
```


__@SpringBootApplication__ : 
    - it contains the @Configuration , @EnableAutoConfiguration , and
@ComponentScan annotations.
    - Spring Boot will use
auto-configuration based on your classpath, your annotations, and your configuration to add the right
technology and create a suitable application.
    - You can also create a standalone application, by going to the command line and executing this:
> mvn package // This command will create a JAR file in the target folder.
> java -jar target/(generatedjar).jar


