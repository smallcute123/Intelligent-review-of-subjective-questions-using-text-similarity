package com.fwwb.patriot.interceptor;

import com.fwwb.patriot.bean.UnLoggedException;
import com.fwwb.patriot.bean.User;
import com.sun.net.httpserver.HttpContext;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.rmi.UnexpectedException;

/**
 * @ClassName: UserInterceptor
 * @Description: 检查用户是否登陆的拦截器
 * @Author: chengxiaoyu
 * @Date: 2023-12-09  22:45
 */

public class UserInterceptor implements HandlerInterceptor {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        System.out.println("已执行UserInterceptor。preHandle:"+handler);
        User user = (User) request.getSession().getAttribute("session_user");
        if (user==null){
            //response.sendRedirect(request.getContextPath()+"/unlogged.html");//拦截后跳转到登录页
            //System.out.println("执行拦截并跳转到登录页 "+request.getContextPath());
            throw new UnLoggedException("unlogged","该用户未登录");
            //return false;
        }
        System.out.println("登陆状态，不执行拦截");
        return true;
    }

    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
        System.out.println("已执行UserInterceptor。postHandle");

    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
        System.out.println("已执行UserInterceptor。afterCompletion");
    }
}
