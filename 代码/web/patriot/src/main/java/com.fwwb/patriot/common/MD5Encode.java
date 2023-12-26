package com.fwwb.patriot.common;
import org.apache.commons.codec.digest.DigestUtils;

public class MD5Encode {
    //有个地方不是英语哦~~~
    private static final String PASSWORD="jiamishujudeqianzhui";
    public static  String encode(String password){
        String str=PASSWORD+password;
        String encode= DigestUtils.md5Hex(str);
        return encode;
    }
}
//  使用： String passwords=MD5Encode.encode(password);