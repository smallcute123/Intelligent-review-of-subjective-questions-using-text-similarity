package com.fwwb.patriot.service.impl;

import com.fwwb.patriot.bean.User;
import com.fwwb.patriot.mapper.UserMapper;
import com.fwwb.patriot.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

/**
 * @ClassName: UserServiceImpl
 * @Description: TODO
 * @Author: chengxiaoyu
 * @Date: 2023-11-23  17:39
 */
@Service
@Transactional(propagation = Propagation.REQUIRED,rollbackFor = Exception.class)
public class UserServiceImpl implements UserService {
    @Autowired
    private UserMapper userMapper;
    @Override
    public User login(String username, String password) {
        return userMapper.login(username,password);
    }

    @Override
    public int register(User user) {
        return userMapper.register(user);
    }

    @Override
    public User findback(String username, String email, String realname, String worknumber) {
        return userMapper.findback(username,email,realname,worknumber);
    }

    @Override
    public int updatepassword(User user) {
        return userMapper.updatepassword(user);
    }

    @Override
    public int check(User user) {
        return userMapper.check(user);
    }
}
