package com.fwwb.patriot.controller;

import com.fwwb.patriot.bean.UnLoggedException;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

/**
 * @ClassName: ExceptionAdvice
 * @Description: TODO
 * @Author: chengxiaoyu
 * @Date: 2023-12-09  22:45
 */
@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(UnLoggedException.class)
    public String UnLoggedAdvice(UnLoggedException e){
        System.out.println("未登录异常已接收");
        return "unlogged";
    }
}
