package com.fwwb.patriot.bean;
/**
 * @ClassName: QAexample
 * @Description: TODO
 * @Author: chengxiaoyu
 * @Date: 2023-11-22  23:39
 */
public class UnLoggedException extends RuntimeException{

    private String code;
    private String msg;

    public UnLoggedException(String code, String msg) {
        super();
        this.code = code;
        this.msg = msg;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }
}
