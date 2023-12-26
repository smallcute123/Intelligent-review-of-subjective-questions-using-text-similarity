package com.fwwb.patriot.service;

import com.fwwb.patriot.bean.User;

/**
 * @ClassName: UserService
 * @Description: TODO
 * @Author: chengxiaoyu
 * @Date: 2023-11-23  17:35
 */
public interface UserService {
    public User login(String username, String password);
    public int register (User user);
    public User findback(String username,String email,String realname,String worknumber);
    public int updatepassword(User user );
    public int check (User user);
}
