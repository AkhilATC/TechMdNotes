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


# Understanding Spring Boot and Spring MVC

## 🎯 Implementing a web app with Spring MVC

To add a web page to your app, you follow two steps:
1. Write an HTML document with the content you want to be displayed by the browser.
2. Write a controller with an action for the web page created at point 1.


> The second step you take is writing a controller with a method that links the HTTP request
> to the page you want your app to provide in response. The controller is a component of the
> web app that contains methods (often named actions) executed for a specific HTTP request.

```java
// home.html is located in resource/static folder
@Controller
public class WebInterfaceController {

    @RequestMapping("/render")
    public String renderHomeHtml(){
        return "home.html";
    }
}
```
- We annotate the class with the @Controller stereotype annotation.
- We use the @RequestMapping annotation to associate the action with an HTTP request path.
- We return the HTML document name that contains the details we want the browser to display.

## 🎯 Implementing web apps with a dynamic view

1. Controller not only to return the view name but somehow also send data to the view. 
The view will incorporate this data to define the HTTP response.


2. the template engine is a dependency that allows us to easily send data from the controller to
the view and display this data in a specific way.(template engine named Thymeleaf)

```
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
```

- Controller uses model and add attributes , that later send to view
- This parameter of type __Model__ stores the data we want the controller to send to the view.
- In this __Model__ instance, we add the values we want to send to the view and identify each of them with a unique name.
- To add a new value that the controller sends to the view, we call the addAttribute() method.
- Write your dynamic html in resource/template folder
- Defines the Thymeleaf “th” prefix in html  (xmlns:th="http://www.thymeleaf.org")
- Uses the “th” prefix to use the values sent by the controller (<span th:text="${User}"></span>!</h1>)

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Home Page</title>
</head>
<body>
<h1>Welcome
    <span th:text="${User}"></span>!</h1>
</body>
</html>

```
#### Getting a value through a request parameter

```java
// http://localhost:8080/render?userName=Rayan
@RequestMapping("/render")
    public String renderHomeHtml(
            @RequestParam String userName,
            Model page){
        page.addAttribute("User",userName);
        return "home.html";
    }
```

Above method takes two parameters:
1. Model page
2. @RequestParam String userName
3. A request parameter is mandatory by default.
4. If you wish the value to be optional then uses @RequestParam(optional=true) .

#### Getting a value through a request path

```java
 @RequestMapping("/render/{id}")
    public String renderHomeHtmlWithPathValue(
            @PathVariable String id,
            Model page
    ){
        page.addAttribute("User",id);
        return "home.html";
    }
```
1. To define a path variable, you assign it a name and put it in the path between curly braces.
2. You mark the parameter where you want to get the path variable value with the @PathVariable annotation. The name of the parameter must
be the same as the name of the variable in the path.

## 🎯 Implementing REST services

we annotate the controller class with the __@Controller__ stereotype
annotation. This way, an instance of the class becomes a bean in the Spring context, and
Spring MVC knows this is a controller that maps its methods to specific HTTP paths.

- ℹ️ 200 OK if no exception was thrown on the server side while processing the request.
- ℹ️ 404 Not Found if the requested resource doesn’t exist.
- ℹ️ 400 Bad Request if a part of the request could not be matched with the way the server
expected the data.
- ℹ️ 500 Error on server if an exception was thrown on the server side for any reason while
processing the request. Usually, for this kind of exception, the client can’t do anything,
and it’s expected someone should solve the problem on the backend.

__@GetMapping__ annotation to specify the action path and HTTP method.

__@ResponseBody__ annotation tells the dispatcher servlet that the controller’s action doesn’t
return a view name but the data sent directly in the HTTP response.

```java
@Controller
public class RestInterface {

    @RequestMapping(value="/rest",method = RequestMethod.GET)
    @ResponseBody
    public String responseRest(){
        return "hello";
    }
}
```
❶ We use the __@Controller__ annotation to mark the class as a Spring MVC controller
❷ We use the __@GetMapping__ annotation to associate the GET HTTP method and a path with the controller’s action.
❸ We use the __@ResponseBody__ annotation to inform the dispatcher servlet that this method doesn’t return a view name but the HTTP response
directly.

Spring offers the __@RestController__ annotation, a combination of __@Controller__ and __@ResponseBody__ .
You use __@RestController__ to instruct Spring that all the controller’s actions are REST endpoints

#### Sending objects as a response body

Data Transfer Object (DTO)
- First define a DTO class
```java
@Data
public class KingResponseObject {
    private String kingName;
    private String clanName;

    public KingResponseObject(String kingName, String clanName) {
        this.kingName = kingName;
        this.clanName = clanName;
    }  

}
```
- RestController class
```java

@Controller
public class RestInterface {

    @RequestMapping(value="/rest",method = RequestMethod.GET)
    @ResponseBody
    public ResponseEntity responseRest(){
        KingResponseObject kingRespOb = new KingResponseObject("Mashkal soya",
                "Mishuth");
        return new ResponseEntity(kingRespOb, HttpStatus.OK);
    }
}
```


