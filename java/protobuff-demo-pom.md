### python
- protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/addressbook.proto

```
"id: \"1\"\n" +\
                "imp {\n" +\
                "  id: \"1\"\n" +\
                "  banner {\n" +\
                "    w: 640\n" +\
                "    h: 480\n" +\
                "    pos: UNKNOWN\n" +\
                "    mimes: \"image/jpg\"\n" +\
                "  }\n" +\
                "  instl: false\n" +\
                "}\n" +\
                "site {\n" +\
                "  id: \"99201\"\n" +\
                "  name: \"rtb4free\"\n" +\
                "  domain: \"rtb4free.com\"\n" +\
                "  cat: \"IAB1\"\n" +\
                "  cat: \"IAB2\"\n" +\
                "  cat: \"IAB3\"\n" +\
                "  keywords: \"radiation\"\n" +\
                "}\n" +\
                "device {\n" +\
                "  ip: \"166.137.138.18\"\n" +\
                "  geo {\n" +\
                "    lat: 42.378\n" +\
                "    lon: -71.227\n" +\
                "    country: \"USA\"\n" +\
                "  }\n" +\
                "  make: \"Apple\"\n" +\
                "  model: \"iPhone\"\n" +\
                "}\n" +\
                "at: SECOND_PRICE";
		
```

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.6.10-SNAPSHOT</version>
		<relativePath/> <!-- lookup parent from repository -->
	</parent>
	<groupId>protobuff.init</groupId>
	<artifactId>protobuff-demo</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>protobuff-demo</name>
	<description>Demo project for Spring Boot - protobuff</description>
	<properties>
		<protobuf.version>3.2.0rc2</protobuf.version>
		<protobuf-java-format.version>1.4</protobuf-java-format.version>
		<java.version>11</java.version>
	</properties>
	<dependencies>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>
		<dependency>
			<groupId>com.google.protobuf</groupId>
			<artifactId>protobuf-java</artifactId>
			<version>${protobuf.version}</version>
		</dependency>

		<dependency>
			<groupId>com.googlecode.protobuf-java-format</groupId>
			<artifactId>protobuf-java-format</artifactId>
			<version>${protobuf-java-format.version}</version>
		</dependency>
		<dependency>
			<groupId>org.projectlombok</groupId>
			<artifactId>lombok</artifactId>
			<optional>true</optional>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>
	</dependencies>

	<build>
		<extensions>
			<extension>
				<groupId>kr.motd.maven</groupId>
				<artifactId>os-maven-plugin</artifactId>
				<version>1.3.0.Final</version>
			</extension>
		</extensions>

		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
			</plugin>

			<plugin>
				<groupId>org.xolstice.maven.plugins</groupId>
				<artifactId>protobuf-maven-plugin</artifactId>
				<version>0.5.0</version>
				<extensions>true</extensions>
				<executions>
					<execution>
						<goals>
							<goal>compile</goal>
							<goal>test-compile</goal>
						</goals>
					</execution>
				</executions>
				<configuration>
					<protocArtifact>com.google.protobuf:protoc:3.0.0:exe:${os.detected.classifier}</protocArtifact>
				</configuration>
			</plugin>

			<plugin>
				<groupId>org.codehaus.mojo</groupId>
				<artifactId>build-helper-maven-plugin</artifactId>
				<executions>
					<execution>
						<id>add-protobuf-generate-sources</id>
						<phase>generate-sources</phase>
						<goals>
							<goal>add-source</goal>
						</goals>
						<configuration>
							<sources>
								<source>target/generated-sources/protobuf/java</source>
							</sources>
						</configuration>
					</execution>

					<execution>
						<id>add-protobuf-generate-test-sources</id>
						<phase>generate-sources</phase>
						<goals>
							<goal>add-test-source</goal>
						</goals>
						<configuration>
							<sources>
								<source>target/generated-test-sources/protobuf/java</source>
							</sources>
						</configuration>
					</execution>
				</executions>
			</plugin>
		</plugins>
	</build>
	
</project>
```
