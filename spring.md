# Adding new beans to spring context

you can add beans to spring context via following ways:

- Using @Bean annotation
- Using stereotype annotation
- programmatically


✅ -> At first we define a Parrot class and a spring context ; then we move Parrot instance to spring context.

__*Parrot Class*__

```java
package com.spring.context;

// define a class with private variable parrotName;
public class Parrot {
    private String parrotName;
    public void setParrotName(String parrotName) {
        this.parrotName = parrotName;
    }
     public String getParrotName() {
        return parrotName;
    }
}

```
✅ -> It’s now time to add the needed dependencies to our project.
```pom
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>5.2.6.RELEASE</version>
</dependency>
```

✅ -> Now we can create the instance of the Spring context.
```java
public class Main {
    public static void main(String[] args) {
        // create object of class Parrot
        Parrot p = new Parrot();
        // create a spring context
        var context = new AnnotationConfigApplicationContext();
    }
}
```
✅ -> In our Main.class includes an empty Spring context and a object of Parrot.class

> You created the Spring context instance and a Parrot instance. Now, you want to add the
Parrot instance inside the Spring context to make Spring aware of this instance.

### how to add the instance to the Spring context using the @Bean annotation.

- Define a configuration class with @Configuration annotation (classname: ConfigForProject). 
- Define a method with @Bean annotation , that returns Parrot Object

```java
// ConfigForProject.class
@Configuration
public class ConfigForProject {
    @Bean
    Parrot returnParrot(){
        Parrot p = new Parrot();
        p.setParrotName("Mis Mushku \uD83E\uDD9C");
        return p;
    }
}

```
- Add ConfigForProject.class in spring context.
>  var context = new AnnotationConfigApplicationContext(ConfigForProject.class); Initializing the Spring context based on the defined configuration class

```java
//Main.class
public class Main {
    public static void main(String[] args) {
        // create a spring context
        var context = new AnnotationConfigApplicationContext(ConfigForProject.class);

    }
}
```

>To verify the Parrot instance is indeed part of the context now, you can refer to the
instance and print its name in the console, as presented in the following listing.

```java
Parrot p = context.getBean(Parrot.class);
System.out.println(p.getParrotName());
// output: Mis Mushku 🦜
```

### Adding multiple beans of the same type to the Spring context.

Suppose we define two @Bean returns same Parrot objects (ConfigForProject.class).

```java
// 
@Configuration
public class ConfigForProject {
    @Bean
    Parrot returnParrot(){
        Parrot p = new Parrot();
        p.setParrotName("Mis Mushku \uD83E\uDD9C");
        return p;
    }
    @Bean
    Parrot returnParrot2(){
        Parrot p = new Parrot();
        p.setParrotName("Mis koKo \uD83E\uDD9C");
        return p;
    }
}
```
> After Excution we got following error:
> Exception in thread "main" org.springframework.beans.factory.NoUniqueBeanDefinitionException: No qualifying bean of type 'com.spring.context.Parrot' 
> available: expected single matching bean but found 2: returnParrot,returnParrot2

solution is : provide bean name
> @Bean(name= "koKo")
> @Bean(value="KoKo")
> @Bean("koko")
```java
// in configuration class define bean name
@Bean(name= "koKo")
    Parrot returnParrot2(){
        Parrot p = new Parrot();
        p.setParrotName("Mis koKo \uD83E\uDD9C");
        return p;
}
// getBean by name from context   
Parrot p = context.getBean("koKo",Parrot.class);
// this will solve the above problem
```
### Using stereotype annotations to add beans to the Spring context
We add beans to context by names if we have multiple beans with same type. 

@Primary annotation is a default choice for context, we we have more than one bans with same type,
we can specify using @primary annotation.
```java
@Bean(name= "koKo")
@Primary
Parrot returnParrot2(){
        Parrot p = new Parrot();
        p.setParrotName("Mis koKo \uD83E\uDD9C");
        return p;
    }
```

__@Component__ Annotation

1. Using the @Component annotation, mark the classes for which you want Spring to add
an instance to its context (in our case Parrot ).
2. Using @ComponentScan annotation over the configuration class , instruct Spring on
where to find the classes you marked.


### Using progrmmatically add beans to spring context.

Using registerBean() method, u can write custom logic to add desired instance to spring context.
you just need to call the registerBean() method of the ApplicationContext instance. 
The registerBean() has four parameters, as

1. beanName : Name for the bean , if don't have name pass null.
2. beanClass : It's class that u define bean to add context. (Parrot.class)
3. Supplier
4. BeanDefinitionCustomizer.


# The Spring context: Wiring beans

For implement a relationship between two instance : Suppose we have a instance Person and we need to
establish a relation between Parrot.class.provide a has-A relation betwwen Person and Parrot.
So I'm define a Person class .
```java
public class Person {
    private String personName;
    private String parrotName;

    public void setParrotName(String parrotName) {
        this.parrotName = parrotName;
    }

    public String getParrotName() {
        return parrotName;
    }

    public void setPersonName(String personName) {
        this.personName = personName;
    }

    public String getPersonName() {
        return personName;
    }

}


```   
Here Person.class holdes member variable, we tried to establish a HAS-A relation between Person and Parrot class
> Define Person bean and Parrot bean in Configuration (ConfigForProject.class)

```java
@Configuration
@ComponentScan(basePackages = "main")
public class ConfigForProject {
    @Bean(name = "Mushku")
    Parrot returnParrot(){
        Parrot p = new Parrot();
        p.setParrotName("Mis Mushku \uD83E\uDD9C");
        return p;
    }
    @Bean(name="Chikku")
    Person getPerson(){
        Person chikku = new Person();
        chikku.setPersonName("Mr. Chikku");
        return chikku;
    }
}
```
> Definition in Main.class
```java
public class Main {
    public static void main(String[] args) {
        // create a spring context
        var context = new AnnotationConfigApplicationContext(ConfigForProject.class);
        Parrot p = context.getBean(Parrot.class);
        Person c = context.getBean(Person.class);
        System.out.println(p.getParrotName()); \\ Mis Mushku 🦜
        System.out.println(c.getPersonName()); \\ Mr. Chikku
        System.out.println(c.getParrotName()); \\ null
    }
}
```
From above code u find out that System.out.println(c.getParrotName()); is null, 
The relationship between the person and the parrot isn’t established.

### Wiring the beans using a direct method call between the @Bean methods

We establish the relationship between the beans using direct wiring. This approach implies
calling the method that returns the bean you want to set directly. You need to call this method from the
one that defines the bean for which you set the dependency.

```java

// ConfigForProject.class
    @Bean(name = "Mushku")
    Parrot returnParrot(){
        Parrot p = new Parrot();
        p.setParrotName("Mis Mushku \uD83E\uDD9C");
        return p;
    }

    @Bean(name="Chikku")
    Person getPerson(){
        Person chikku = new Person();
        chikku.setPersonName("Mr. Chikku");
        chikku.setParrotName(returnParrot()); // its return Parrot object , so setParrotname changes
        return chikku;
    }
// Person.class
 public void setParrotName(Parrot parrotName) {
        this.parrotName = parrotName.getParrotName();
    }
//main.class

Parrot p = context.getBean(Parrot.class);
Person c = context.getBean(Person.class);
System.out.println(p.getParrotName()); // Mis Mushku 🦜
System.out.println(c.getPersonName()); // Mr. Chikku
System.out.println(c.getParrotName()); // Mis Mushku 🦜
   
```

### Wiring the beans using the @Bean annotated method’s parameters
