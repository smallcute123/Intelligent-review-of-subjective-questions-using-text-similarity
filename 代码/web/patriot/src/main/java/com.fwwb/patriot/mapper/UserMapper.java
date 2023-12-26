package com.fwwb.patriot.mapper;

import com.fwwb.patriot.bean.User;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Repository;

/**
 * @ClassName: UserMapper
 * @Description: Dao
 * @Author: chengxiaoyu
 * @Date: 2023-12-09  22:45
 */

@Repository
@Mapper
public interface UserMapper {
    //多参数情况下用Param注解实现参数与Mapper中#{变量名}的匹配
    public User login(@Param("username") String username, @Param("password")String password);
    //该插入注册返回的是对数据操作的条数（1）
    public int register (User user);
    public User findback(@Param("username")String username,@Param("email")String email,@Param("realname")String realname,@Param("worknumber")String worknumber);
    //该更新返回的是对数据操作的条数（1）
    public int updatepassword(User user );
    public int check (User user);

}
