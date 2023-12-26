package com.fwwb.patriot.config;

import com.fwwb.patriot.interceptor.UserInterceptor;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurationSupport;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

/**
 * @ClassName: CustomMVCConfig
 * @Description: 1、扩展默认的SpringMVC功能
 *  *              2、根据需求实现接口的功能，不强制全部实现（default）
 *  *              3、声明为配置类
 */
//@Configuration
//public class CustomMVCConfig implements WebMvcConfigurer {
//    //添加拦截器
//    @Override
//    public void addInterceptors(InterceptorRegistry registry) {
//        registry.addInterceptor(new UserInterceptor())
//                .addPathPatterns("/judge/**")
//                .addPathPatterns("/updatepassword/**");
//    }
//
//}
