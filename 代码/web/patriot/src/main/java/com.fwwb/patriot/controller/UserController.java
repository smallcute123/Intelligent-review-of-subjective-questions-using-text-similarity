package com.fwwb.patriot.controller;

import com.fwwb.patriot.bean.User;
import com.fwwb.patriot.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletRequest;

/**
 * @ClassName: userController
 * @Description: TODO
 * @Author: chengxiaoyu
 * @Date: 2023-12-09  22:45
 */
@Controller
public class UserController {
    @Autowired
    private UserService userService;

    @RequestMapping("/login")
    @ResponseBody
    public String login(@RequestBody User user, HttpServletRequest request) {   //RequestBody指定传递json型数据，不可以 @RequestBody str
        String username = user.getUsername();
        String password = user.getPassword();
        User newuser = userService.login(username, password);
        if (newuser == null) {
            return "0";   //用户名或密码错误
        } else {
            request.getSession().setAttribute("session_user", newuser);
            return "1";   //登陆成功
        }
    }

    @RequestMapping("/register")
    @ResponseBody
    public String register(@RequestBody User user) {
        int count = userService.check(user);
        if (count != 0) {
            return "0";//该用户名已存在
        } else {
            count=0;
            count = userService.register(user);
            if (count != 0)
                return "1";//注册成功
            else
                return "2";//数据库操作失败
        }
    }

    @ResponseBody
    @RequestMapping("/updatepassword")
    public String updatepassword(@RequestBody User user, HttpServletRequest request) {
        User nowuser = (User) request.getSession().getAttribute("session_user");
        String password= user.getPassword();
        String newpassword= user.getNewpassword();
        if (nowuser.getPassword() .equals(password) ) {
            nowuser.setPassword(newpassword);
            int count= 0;
            count = userService.updatepassword(nowuser);
            if (count != 0) {
                System.out.println("111");
                return "1";//修改密码成功
            }
            else {
                return "2";//数据库操作失败
            }
        }
        else {
            System.out.println(nowuser.getPassword());
            return "0";//输入的旧密码错误
        }
    }

    @ResponseBody
    @RequestMapping("/findback")
    public String findback(@RequestBody User user,HttpServletRequest request){
        String username = user.getUsername();
        String email = user.getEmail();
        String realname=user.getRealname();
        String worknumber=user.getWorknumber();
        String newpassword= user.getNewpassword();
        User myuser=userService.findback(username,email,realname,worknumber);
        if(myuser==null){
            return "0";//信息错误
        }
        else {
            myuser.setPassword(newpassword);
            int count=0;
            count=userService.updatepassword(myuser);
            if (count != 0) {
                request.getSession().setAttribute("session_user", myuser);
                return "1";//修改(找回)密码成功
            }
            else
                return "2";//数据库操作失败
        }
    }
}