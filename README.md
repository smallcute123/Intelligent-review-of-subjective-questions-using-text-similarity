#  Application and Development Environment

The system's application environment is described as follows: Python 3.6 and above, MySQL 5.6 and above, JDK 1.8 and above, Tomcat 9 and above, Windows 7 and above.

The development technologies and environment for this system are detailed in Table 5.1.

##  Development Technologies and Environment

| Module       | Development Tools               | Technologies, Libraries, and Environment                         |
|--------------|---------------------------------|-----------------------------------------------------------------|
| Algorithm    | Jupyter Notebook; Vscode 1.38.1; | jieba; jiagu; itertools; synonyms; gensim                        |
|              | PyCharm 2019;                   |                                                                 |
| Web Frontend | IntelliJ IDEA 2018;              | JavaScript language; Vue framework                               |
| Server       | MobaXterm; Tomcat 9 (Spring Boot | CentOS 7.7; Windows 10                                           |
|              | built-in)                        |                                                                 |
| Java Backend | IntelliJ IDEA 2019;               | Spring Boot; Maven; MyBatis                                      |
| Database     | Navicat; PhpMyAdmin;              | MySQL                                                           |

#  Running and Usage

First, ensure the correct configuration and installation of the relevant environment and software as described in Section 5.1.

## Algorithm Module

The code for the algorithm module is located in the `\code\python` directory, with the training set contained in the `\code\data` directory. The main algorithm program is `go.py`. The required input format is illustrated in Figure 5.1.


## Web Server Module

The web server module is located in the `\web` directory. It is built using the Vue framework for the frontend, Spring Boot for the backend, and Flask for certain functionalities. To run, configure the relevant frameworks, such as dependencies for running vue.js, the maven environment for the Spring Boot framework, and mybatis for database management. Finally, import the maven project into IntelliJ IDEA, build the project as a JAR file using the `pom.xml` file, and run it using the command `java -jar`.

Please refer to this document for detailed instructions on running and using the system.
