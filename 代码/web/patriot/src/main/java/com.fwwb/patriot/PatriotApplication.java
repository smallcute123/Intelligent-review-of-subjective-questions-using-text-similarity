package com.fwwb.patriot;

        import org.mybatis.spring.annotation.MapperScan;
        import org.springframework.boot.SpringApplication;
        import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan(value = "com.fwwb.patriot.mapper")
public class PatriotApplication {

    public static void main(String[] args) {
        SpringApplication.run(PatriotApplication.class, args);
    }

}
