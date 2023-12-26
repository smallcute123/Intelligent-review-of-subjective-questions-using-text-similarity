import re
import jieba
import jiagu
import math
import jieba.analyse
from itertools import product
jieba.load_userdict('data/jiebawordlist.txt') #加载jieba自定义词典

#################    自定义函数：   ####################################
# 生成各类词表list以及学生回答list
# 参数说明，filepath：相对路径
def generate_list(filepath):
    list1 = []
    with open(filepath,'r',encoding='UTF-8') as f :
        for line1 in f:
            list1.append(line1.strip())
    return list1

# 创建同义词反义词词典
def creat_tong_fan(filepath):
    keyword = []
    tongyici = []
    dict1 = dict()
    with open(filepath, 'r', encoding = 'utf-8') as f1:
        for i in f1:
            list1 = i.strip().split(':')
            key = list1[0]
            value = list1[1]
            dict1[key] = value
    return dict1

# 去停用词得列表
# 参数说明，list1：学生回答分词list，list2：停用词列表
# 返回值：去停用词的分词list
def delete_stopwords(list1, list2):
    list3 = []
    for i in list1:
        if i not in list2:
            list3.append(i)
    return list3

# jieba对句子/得分点进行分词并去停用词
# 参数说明，sentence：学生回答，stopwords：停用词list
# 返回值：去停用词的学生回答分词list
def jieba_seg_sentence(sentence, stopwords):
    sentence_seged = jieba.lcut(sentence) # 使用jieba对学生回答进行分词
    list1 = delete_stopwords(sentence_seged,  stopwords) #去停用词
    return ''.join(list1)

# jieba对句子进行分词并去停用词
# 参数说明，sentence：学生回答，stopwords：停用词list
# 返回值：去停用词的学生回答分词list
def jieba_seg_sentence(sentence, stopwords):
    sentence_seged = jieba.lcut(sentence) # 使用jieba对学生回答进行分词
    list1 = delete_stopwords(sentence_seged,  stopwords) #去停用词
    return ''.join(list1)

# jiagu对句子进行分词并去停用词
# 参数说明，sentence：学生回答，stopwords：停用词list
# 返回值：去停用词的学生回答分词list
def jiagu_seg_sentence(sentence, stopwords):
    sentence_seged = jiagu.seg(sentence) # 使用jieba对学生回答进行分词
    list1 = delete_stopwords(sentence_seged,  stopwords) #去停用词
    return ''.join(list1)

# 提出学生回答中长度小于等于1或大于等于3，且在wordlist_1 、wordlist_3中的词语
# 参数说明，str1：去停用词的学生回答，list1：wordlist_1 + wordlist_3，长度小于等于1和大于等于3的标准答案关键词list
# 返回值：长度小于等于1或大于等于3的学生回答关键词list
def extractwords_1_3(str1, list1):
    temp_list1 = set(jieba.lcut(str1) + jiagu.seg(str1)) # jieba和jiagu同时进行分词，并去重
    temp_list2 = []
    for i in temp_list1:
        if len(i)==1 or len(i)>=3:
            if i in list1:
                temp_list2.append(i)
    return temp_list2

# tfidf和textrank结合提取关键词
# 参数说明，str1：剩余两字词语的回答，n: 提取关键词的字数
# 返回值：学生答案关键词list
def tfidf_textrank(n, str1):
    a= jieba.analyse.extract_tags(str1,withWeight=True)  # tfidf(关键词, 得分)
    b = jieba.analyse.textrank(str1,withWeight=True)  # textrank(关键词, 得分)
    if a != []: # 如果a不为空
        a_value = []
        for i in range(len(a)):
            a_value.append(a[i][1])
        a_keymax = max(a_value) # 得a_keymax为归一化做准备
        a_dict = dict()
        b_dict = dict()
        for i in range(len(a)):
            a_dict[a[i][0]] = a[i][1] / a_keymax # 归一化
        for i in range(len(b)):
            b_dict[b[i][0]] = b[i][1]
        temp_list = [] # 用于储存即在a又在b中的词语
        for i in b_dict.keys():
            if i in a_dict:
                a_dict[i] += b_dict[i]
                temp_list.append(i)
        for i in b_dict.keys():
            if i not in temp_list:
                a_dict[i] = b_dict[i]  # a_dict[i]为所有词语和其得分
        all_keywords = sorted(a_dict.items(), key = lambda x:x[1], reverse = True) # 所有关键词排序
        keywords = []
        if len(all_keywords)>= n:
            for i in range(n):
                keywords.append(all_keywords[i][0])
            return keywords
        else:
            for i in range(len(all_keywords)):
                keywords.append(all_keywords[i][0])
            return keywords
    else: # 如果a为空，直接返回[]
        return []

# 提取学生回答关键词
# 参数说明，str1：去停用词的学生回答，list1：学生回答中长度小于等于1或大于等于3的词语list，list2：标准答案关键词
# 返回值：学生答案所有关键词list
def student_all_keywords(str1, list1, list2):
    temp_list1 = set(jieba.lcut(str1) + jiagu.seg(str1)) # jieba和jiagu同时进行分词，并去重
    temp_set2 =  [] 
    for i in temp_list1 - set(list1): # 得到所有的2字词语
        if len(i) == 2:
            temp_set2.append(i)
    temp_set2 = set(temp_set2) # 所有的2字词语set
    str2 = ' '.join(temp_set2) # 剩下长度为 2 的词语组成间隔为‘ ’的句子
    # topK = len(list2)+1-len(list1) # jieba提取关键词的个数=标答关键词数+5-list1词数
    # if topK <= 0: # 防止topK为0
    #     topK = 1
    topK = 4
    if set(list2) <= set(list1): # 如果标准答案关键词集合属于长度小于等于1或大于等于3的词语list
        keywords_std = list1
    else:  # 否则 jieba提取topK个关键词 + list1 + jiagu提取2个关键词 后去重
        keywords_std =  tfidf_textrank(topK, str2) + list1
    return keywords_std

def extract_keywords(str1, list1):
    temp_list1 = jieba.lcut(str1) # jieba进行分词
    temp_list2 = []
    for i in range(len(temp_list1)-1 , -1 ,-1):
        if (len(temp_list1[i])==1 or len(temp_list1[i])>=3) and temp_list1[i] in list1:
            temp_list2.append(temp_list1[i])
            temp_list1.pop(i)
    rest_str = ''.join(set(temp_list1)) # 剩余词语组成的str
    temp_list2 = temp_list2 + tfidf_textrank(5,rest_str)
    return temp_list2

# 得去双重否定词后的句子str1和双重否定词list2
# 参数说明：str1：未作处理的学生回答，list1：双重否定词list
# 返回值：去双重否定词后的句子str1和双重否定词list
def delete_double_neg(str1, list1): 
    list2 = []
    for i in list1:
        temp = str1.find(i)
        if temp != -1:
            str1 = str1[0:temp] + str1[temp+len(i):]
            list2.append(i)
    return str1, list2

def panduan(boolean1, int1):
    if int1 == 1:
        return boolean1
    elif int1 == 2:
        return True

# 判断的否定词为前一项
def singal_word_before(word, index1, index2, allwords, func_flag):
    for i in range(len(allwords)):
        if len(word)==1 : # 如果这个词语长度为1
            # 如果这个词是学生回答中某词或者某词的子集并且这个词不为否定词
            if word in allwords[i]  and abs(len(allwords[i])-len(word))<=1 and panduan(student_answer_flag[i]==0, func_flag) :
                if allwords[i] not in neg_list:
                    flag1 = 1
                    if allwords[i-1] in neg_list:
                        flag1 *= -1
                    student_answer_flag[i]=1
                    return (weight[index1][index2], flag1)
        else:
            # 如果这个词是学生回答中某词或者某词的子集
            if word in allwords[i]  and abs(len(allwords[i])-len(word))<=2 and panduan(student_answer_flag[i]==0, func_flag) :
                flag1 = 1
                if allwords[i-1] in neg_list:
                    flag1 *= -1
                student_answer_flag[i]=1
                return (weight[index1][index2], flag1)
    return (0,1)

    # if word in allwords:
    #     index_temp1 = allwords.index(word)
    #     flag1= meaning_flag[index1]
    #     if allwords[index_temp1-1] in neg_list:
    #         flag1 *= -1
    #     if flag1 == meaning_flag[index1]:
    #         return weight[index1][index2]
    #     else:
    #         return 0
    # else:
    #     return 0

##################################################################
wordlist_1 = generate_list('data/wordlist_1.txt') # 长度等于1的答案关键词list
wordlist_3 = generate_list('data/wordlist_3.txt')   # 长度大于等于3的答案关键词list
stopwords = generate_list('data/Hstopwords.txt') # 停用词
neg_list = generate_list('data/negative.txt') # 否定词list
double_neg_list = generate_list('data/double_negative.txt') # 双重否定词list
tongyici = creat_tong_fan("data/tongyici.txt") # 创建同义词字典
fanyici = creat_tong_fan("data/fanyici.txt") # 创建反义词字典

question = input("输入问题：")
keywords_str =  input("输入关键词：")
answer = input("输入标准答案：")
student_answer = input("输入学生回答：")

# question = duyiwuer[0]
question_seg_allpattern=[] # 问题jieba分词全模式，未使用自定义词典
for item in jieba.cut(question, cut_all=True):
    if item not in stopwords:
        question_seg_allpattern.append(item)
# print(question)

# keywords_str = duyiwuer[2]
sco_point_keywords_list = [] # ['活动范围', '功能', '存在', '差异', '运输方式', '运输工具']
sco_point_keywords = [] # [['活动范围'], ['功能', '存在', '差异'], ['运输方式', '运输工具']]
scoring_points = keywords_str.split('，') # eg: ['数据易搜集', '计算简单', '容易理解', '单一设施选址时常采用']
for j in scoring_points:
    # 如果这个词语不可再分
    if len(jieba.lcut(j))==1:
        sco_point_keywords_list.append(jieba.lcut(j)[0])
        sco_point_keywords.append(jieba.lcut(j))
    # elif len(jieba.lcut(j))==2:
    #     sco_point_keywords_list.append(jieba.lcut(j))
    #     sco_point_keywords.append(jieba.lcut(j))
    else: # 如果这个词可分为多个
        temp_list0 = jieba_seg_sentence(j, stopwords)  # jiagu去除得分点的停用词得str
        temp_list1 = delete_stopwords(jieba.lcut(temp_list0), [" ","","和","与","受","上"]+stopwords+question_seg_allpattern) # 去除题干中的词语
        if temp_list1 != []:
            sco_point_keywords_list += temp_list1
            sco_point_keywords.append(temp_list1)
# print(sco_point_keywords)

# answer = duyiwuer[1]
sentence1 = jieba_seg_sentence(answer, stopwords) # jieba对标准答案去停用词后的句子
words_1_3 = extractwords_1_3(sentence1, wordlist_1+ wordlist_3) # 提取出标准答案中出长度小于等于1或大于等于3的词语list
keywords_ans = list(student_all_keywords(sentence1, words_1_3, scoring_points)) # 得到标准答案的部分关键词list
weight = [] # 记录词语权重
meaning_flag=[] # 记录该词在标答中肯否定
per = 10 / len(sco_point_keywords)
for i in range(len(sco_point_keywords)-1,-1,-1):
    if len(sco_point_keywords[i]) == 1:
        weight.insert(0,[per])
        meaning_flag.insert(0,1)
    else:
        flag = 1
        list1 = sco_point_keywords[i]
        init_weight = [1]*len(list1)
        for j in range(len(list1)-1,-1,-1):
            if list1[j] in neg_list:
                # print(list1[j])
                list1.pop(j)
                init_weight.pop(j)
                flag = -1
            else:
                if list1[j] in keywords_ans and len(list1[j]) != 2:
                    init_weight[j] = 1.3
        meaning_flag.insert(0,flag)
        sum1 =  sum(init_weight ) # 记录权重总和为归一化做准备
        temp_list2 = [x*per/sum1 for x in init_weight ] # 和为10的各关键词权重
        weight.insert(0,temp_list2)
# print(weight)
student_answer = "回答，"+student_answer+"，回答"
sentence1, double_neg_list1 = delete_double_neg(student_answer, double_neg_list)# 得去双重否定词后的学生回答sentence1和双重否定词list1
student_answer_words = jieba.lcut(jieba_seg_sentence(sentence1, stopwords)) # 得去停用词、去双重否定词得学生回答list
# student_answer_words = jieba.lcut(sentence1)# 得去停用词、去双重否定词得学生回答list
for index4 in range(len(student_answer_words) - 2, 0, -1):
    if student_answer_words[index4] in neg_list and student_answer_words[index4 + 1] in ["，", "。", "：", "、","；"]: # 如果这个词为否定词且后一个词为标点符号
        student_answer_words[index4], student_answer_words[index4-1] = student_answer_words[index4-1], student_answer_words[index4] # 则交换位置，使否定词前移
for item0 in range(len(student_answer_words)-2, 0, -1):
    if student_answer_words[item0] in fanyici and fanyici[student_answer_words[item0]] in sco_point_keywords_list: # 如果这个词语出现在反义词典，并且其反义词出现在关键词中
        if student_answer_words[item0-1] in neg_list: # 并且这个词前一个词为否定词
            student_answer_words.pop(item0)
            student_answer_words[item0- 1] = fanyici[student_answer_words[item0]]
    elif student_answer_words[item0] in tongyici and tongyici[student_answer_words[item0]] in sco_point_keywords_list: # 如果这个词语出现在同义词典，并且其同义词出现在关键词中
        student_answer_words[item0] = tongyici[student_answer_words[item0]]
student_answer_flag = [0] * len(student_answer_words) # 用于标记已找到过的词语
# sentence2 = ''.join(student_answer_words) # 去停用词、去双重否定词得学生回答str
# print(sentence2)
point=[]
for i in range(len(sco_point_keywords)):
    if len(sco_point_keywords[i]) == 1: # 如果只有一个词语
        temp_tuple = singal_word_before(sco_point_keywords[i][0], i, 0, student_answer_words,1)
        if temp_tuple[1] == meaning_flag[i]: # 如果句意相同
            point.append(temp_tuple[0])
        else:
            point.append(0)
    elif len(sco_point_keywords[i]) == 2: # 如果有两个词
        if weight[i][0] == weight[i][1]: # 如果两个词权重相同
            temp_tuple1 = singal_word_before(sco_point_keywords[i][0], i, 0, student_answer_words,1)
            temp_tuple2 = singal_word_before(sco_point_keywords[i][1], i, 1, student_answer_words,1)
            if temp_tuple1[1]*temp_tuple2[1] == meaning_flag[i]: # 如果这个得分点句意相符
                point.append(temp_tuple1[0] + temp_tuple2[0])
            else: # 如果这个得分点句意不相符
                point.append(0)
        else: # 如果两个词权重不相同
            if sco_point_keywords[i][0] not in student_answer_words or sco_point_keywords[i][1] not in student_answer_words: # 如果两个词不同时在allwords中
                point.append(0)
            else:  # 如果两个词同时在allwords中
                temp_tuple1 = singal_word_before(sco_point_keywords[i][0], i, 0, student_answer_words,1)
                temp_tuple2 = singal_word_before(sco_point_keywords[i][1], i, 1, student_answer_words,1)
                if temp_tuple1[1]*temp_tuple2[1] == meaning_flag[i] and temp_tuple1[0] * temp_tuple2[0] != 0: # 如果这个得分点句意相符，并且得分相乘不为0
                    point.append(temp_tuple1[0] + temp_tuple2[0])
                else:
                    point.append(0)
    else: # 如果有多个词
        index_list1 = [] # 记录多个词在回答中的索引
        distance = 100 # 记录所有词之间的距离
        temp_list3 = [] # 记录所有词最短距离下的index
        temp_point4 = 0 # 记录得分
        neg_num = meaning_flag[i] # 设置初始句意  
        # print(sco_point_keywords[i])
        for item in sco_point_keywords[i]:
            index_temp1 = [item0 for item0,x in enumerate(student_answer_words) if x == item] # 得到所有词出现的位置【【12，15，20】 【17】【18，27】】
            index_list1.append(index_temp1)
        if len(index_list1) == len(sco_point_keywords[i]) and [] not in index_list1: # 如果全部找到
            for item1 in product(*index_list1):
                n = 0
                for k in range(len(index_list1))[0:-1]:
                    n += abs(item1[k+1] - item1[k] - 1)
                if n <= distance:
                    distance = n
                    temp_list3 = item1 # 得到所有词最短距离情况时的index
            if distance <=3: # 如果这些词相隔不远
                for num in range(len(temp_list3)):
                    if student_answer_words[num-1] in neg_list:
                        neg_num *= -1
                if neg_num == meaning_flag[i]:
                    point.append(sum(weight[i]))
                    for index3 in temp_list3:
                        student_answer_flag[index3] = 1
                else:
                    point.append(0)
            else:
                point.append(0)
        elif len(index_list1) == len(sco_point_keywords[i])-1: # 如果少找1个
            for item1 in product(*index_list1):
                n = 0
                for k in range(len(index_list1))[0:-1]:
                    n += abs(item1[k+1] - item1[k] - len(sco_point_keywords[i][k]))
                if n <= distance:
                    distance = n
                    temp_list3 = item1
            for num in range(len(temp_list3)):
                if student_answer_words[num-1] in neg_list:
                    neg_num *= -1
            if neg_num == meaning_flag[i]:
                point.append(sum(weight[i])/3)
                for index3 in temp_list3:
                    student_answer_flag[index3] = 1
            else:
                point.append(0)
        else: # 如果少找2个或以上，直接给0分
            point.append(0)
 # 再次打分   
if len(sco_point_keywords) == len(point): # 先判断词的个数是否与分数个数相一致
    for index5 in range(len(sco_point_keywords)):
        # 如果是一个词
        if len(sco_point_keywords[index5])==1 and point[index5]==0: 
            # 剔除题干中的词得到str
            temp_word = ''.join(list(set(jiagu.seg(sco_point_keywords[index5][0]))- set(question_seg_allpattern)))
            temp_list4 = jieba.lcut(temp_word)
            # 如果分成一个词
            if len(temp_list4)==1:
                if temp_word != "":
                    temp_tuple3 = singal_word_before(temp_word, index5, 0, student_answer_words,1)
                if temp_tuple3[1] == meaning_flag[i]: # 如果句意相同
                    point[index5] = temp_tuple3[0]
            # 如果分成两个词
            elif len(temp_list4)==2:
                temp_tuple4 = singal_word_before(temp_list4[0], i, 0, student_answer_words,1)
                temp_tuple5 = singal_word_before(temp_list4[1], i, 0, student_answer_words,1)
                # 如果这个得分点句意相符，并且得分相乘不为0，表示找到了
                if temp_tuple4[1]*temp_tuple5[1] == meaning_flag[i] and temp_tuple4[0] * temp_tuple5[0] != 0:
                    point[index5] = weight[index5][0]
        # # 如果是两个词
        elif len(sco_point_keywords[index5])==2 and point[index5]==0: 
            # 不管这个词是否被找到过
            # print(sco_point_keywords[index5][0])
            # print(sco_point_keywords[index5][1])
            temp_tuple6 = singal_word_before(sco_point_keywords[index5][0], index5, 0, student_answer_words,2)
            temp_tuple7 = singal_word_before(sco_point_keywords[index5][1], index5, 0, student_answer_words,2)
            # print(temp_tuple6)
            # print(temp_tuple7)
            # 如果这个得分点句意相符，并且得分相乘不为0，表示找到了
            if temp_tuple6[1]*temp_tuple7[1] == meaning_flag[i] and temp_tuple6[0] * temp_tuple7[0] != 0:
                point[index5] = sum(weight[index5])

int_temp = math.floor(sum(point))  # 分数的整数部分
float_temp = sum(point) - int_temp # 分数的小数部分 
if  float_temp >= 0.7: # 如果小数部分大于0.7
    print(int_temp+1)
else:
    print(int_temp)