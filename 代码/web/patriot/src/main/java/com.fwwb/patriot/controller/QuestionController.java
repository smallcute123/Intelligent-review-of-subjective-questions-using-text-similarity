package com.fwwb.patriot.controller;

import com.fwwb.patriot.bean.QAexample;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;

/**
 * @ClassName: QuestionController
 * @Description: TODO
 * @Author: chengxiaoyu
 * @Date: 2023-12-09  22:45
 */

@Controller
public class QuestionController {

    @RequestMapping("/judge")
    @ResponseBody
    public String singleJudge(@RequestBody QAexample example) throws IOException {
        String question= example.getQuestion();
        String standard_answer= example.getStandard_answer();
        String keywords= example.getKeywords();
        String student_answer =example.getStudent_answer();
        String exe = "python";
        String command = "/root/fwwb/go.py";
        String[] cmdArr = new String[]{exe, command, question,standard_answer,keywords,student_answer};
        System.out.println(question);
        System.out.println(standard_answer);
        System.out.println(keywords);
        System.out.println(student_answer);
        Process process = null;
        try {
            process = Runtime.getRuntime().exec(cmdArr);
        } catch (IOException e) {
            e.printStackTrace();
            return "错误";
        }
        InputStream is = process.getInputStream();
        DataInputStream dis = new DataInputStream(is);
        String grade = null;
        try {
            grade = dis.readLine();
        } catch (IOException e) {
            e.printStackTrace();
            return "错误";
        }
        try {
            process.waitFor();
        } catch (InterruptedException e) {
            e.printStackTrace();
            return "错误";
        }
        is.close();
        dis.close();
        System.out.println(grade);
        return grade;
    }
}
