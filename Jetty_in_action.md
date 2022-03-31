# Embedded Jetty

1. Simple Embedded Jetty Server
```pom.xml

<dependency>
            <groupId>org.eclipse.jetty</groupId>
            <artifactId>jetty-server</artifactId>
            <version>9.2.15.v20160210</version>
        </dependency>
        <dependency>
            <groupId>org.eclipse.jetty</groupId>
            <artifactId>jetty-servlet</artifactId>
            <version>9.2.15.v20160210</version>
        </dependency>
```
---
```java
public class ServerInit {
    public static void main(String[] args) throws Exception {
        Server jettyServer  = new Server(9001);
        jettyServer.start();
        jettyServer.dumpStdErr();
        jettyServer.join();

    }
}

```
This runs an HTTP server on port 8680. It’s just a simple server, but it won’t do anything useful work as there are no handlers. This will return 404 error for every request.
Jetty requires Handler on the server to create a response. A handler generally examines HTTP request and generates HTTP response.

AbstractHandler class override handle method, which includes following parameters as arguments

1. target – the target of the request, which is either URI or a name from a named dispatcher
2. request – the Jetty mutable request object
3. httpServletRequest – the immutable request object
4. httpServletResponse – the response, which may have been wrapped by a filter or a servlet.
