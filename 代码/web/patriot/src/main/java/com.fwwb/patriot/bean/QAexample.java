package com.fwwb.patriot.bean;

import java.io.Serializable;

/**
 * @ClassName: QAexample
 * @Description: TODO
 * @Author: chengxiaoyu
 * @Date: 2023-11-22  23:32
 */
public class QAexample implements Serializable {
    private String question;
    private String standard_answer;
    private String keywords;
    private String student_answer;
    private String grade;

    public String getQuestion() {
        return question;
    }

    public void setQuestion(String question) {
        this.question = question;
    }

    public String getStandard_answer() {
        return standard_answer;
    }

    public void setStandard_answer(String standard_answer) {
        this.standard_answer = standard_answer;
    }

    public String getKeywords() {
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }

    public String getStudent_answer() {
        return student_answer;
    }

    public void setStudent_answer(String student_answer) {
        this.student_answer = student_answer;
    }

    public String getGrade() {
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }

    @Override
    public String toString() {
        return "QAexample{" +
                "question='" + question + '\'' +
                ", standard_answer='" + standard_answer + '\'' +
                ", keywords='" + keywords + '\'' +
                ", student_answer='" + student_answer + '\'' +
                ", grade='" + grade + '\'' +
                '}';
    }
}
