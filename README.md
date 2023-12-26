# 应用与开发环境

本系统应用环境描述如下：Python 3.6及以上、MySQL 5.6及以上、JDK 1.8及以上、Tomcat 9及以上、Windows 7及以上。

## 开发技术与环境

| 模块         | 开发工具                        | 开发技术、库与环境                                              |
| ------------ | ------------------------------- | --------------------------------------------------------------- |
| 算法模块     | Jupyter Notebook; Vscode 1.38.1; | jieba; jiagu; itertools; synonyms; gensim                        |
|              | PyCharm 2019;                   |                                                                 |
| 网页端       | IntelliJ IDEA 2018;              | JavaScript语言; Vue框架                                       |
| 服务器       | MobaXterm; Tomcat 9（Spring Boot  | Centos 7.7; Windows 10                                          |
|              | 内置）                          |                                                                 |
| Java后端     | IntelliJ IDEA 2019;               | Spring Boot; Maven; MyBatis                                     |
| 数据库       | Navicat; PhpMyAdmin;             | MySQL                                                           |

# 运行与使用

首先根据上述内容保证相关环境和软件的正确配置和安装。

## 算法模块

算法模块代码位于 ``\代码\python`` 路径下，go.py为算法主程序。所需的输入格式可见视频。


## Web服务端模块

Web服务端模块位于\web路径下，按照前端的Vue框架和后端的Spring Boot框架以及Flask框架搭建而成，运行需要按照相关框架进行相关配置，比如运行vue.js所需的依赖，Spring Boot框架所需的Maven环境，以及管理数据库所需的MyBatis等。最后通过IDEA，导入Maven项目，根据pom.xml文件打成JAR包，直接通过java -jar的方式运行即可。

请参考本文档以获取有关运行和使用系统的详细说明。
