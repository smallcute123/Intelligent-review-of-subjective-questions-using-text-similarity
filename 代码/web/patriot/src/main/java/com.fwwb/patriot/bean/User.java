package com.fwwb.patriot.bean;

import java.io.Serializable;

/**
 * @ClassName: QAexample
 * @Description: TODO
 * @Author: chengxiaoyu
 * @Date: 2023-11-22  23:32
 */
public class User implements Serializable {
    private  int id;
    private String username;
    private String password;
    private String newpassword;
    private String email;
    private String realname;
    private String worknumber;

    public String getNewpassword() {
        return newpassword;
    }

    public void setNewpassword(String newpassword) {
        this.newpassword = newpassword;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getRealname() {
        return realname;
    }

    public void setRealname(String realname) {
        this.realname = realname;
    }

    public String getWorknumber() {
        return worknumber;
    }

    public void setWorknumber(String worknumber) {
        this.worknumber = worknumber;
    }
}
