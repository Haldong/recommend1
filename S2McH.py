# 라이브러리 import
import pandas as pd
import numpy as np
import os
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import regexp_tokenize
from nltk.corpus import stopwords
from collections import Counter
import operator
print("1. library import complete")

# nltk 설치
# nltk.download_gui()

# path 설정
path = "c:/python/S2McH"
if os.path.exists(path):
    os.chdir(path)
else:
    os.makedirs(path)
    os.chdir(path)
print("2. path set complete")

# 사전 불러오기
element_dic = pd.read_excel("Elementary.xlsx", header=None)[0]
middle_dic = pd.read_excel("middle.xlsx", header=None)[0]
high_dic = pd.read_excel("high.xlsx", header=None)[0]
primary_dic = pd.read_excel("primary.xlsx", header=None)[0]
print("3. dic load complete")

# 컨텐츠(책, 영화자막등) 불러오기
path = "Alice's Adventures in Wonderland by Lewis Carroll (339)"
contents = open(path+".txt", "r").read()
print("4. contents open complete")

# tokenize
token = regexp_tokenize(contents, pattern='[a-zA-Z]+') # 영어만 추출
lower_token = [i.lower() for i in token] # 소문자로 변환
word_list = [] # 동사 기본형으로 변형
for word in lower_token:
    word_list.append(WordNetLemmatizer().lemmatize(word, 'v'))
    # word_list.append(WordNetLemmatizer().lemmatize(word, 'n'))
print("5. tokenzie complete")

# word count
unique_words_list = []
stopwords = np.array(stopwords.words("english"))
for i in set(word_list):
    if i not in stopwords:
        unique_words_list.append(i)    # 중복 단어 제거 & 리스트에 단어 추가
unique_words = np.array(unique_words_list)
unique_words_tf = Counter(word_list) # 단어별 tf
sort_tf = sorted(unique_words_tf.items(), key=operator.itemgetter(1), reverse=True)
print("6. extract unique word & compute tf complete")

# matching with dictionary
def dic_count(dic1 = element_dic, dic2 = middle_dic, dic3 = high_dic, dic4 =primary_dic):
    element_dic_counts = 0
    middle_dic_counts = 0
    high_dic_counts = 0
    primary_dic_counts = 0
    for word in unique_words:
        if word in np.array(dic1):
            element_dic_counts += 1
    for word in unique_words:
        if word in np.array(dic2):
            middle_dic_counts += 1
    for word in unique_words:
        if word in np.array(dic3):
            high_dic_counts += 1
    for word in unique_words:
        if word in np.array(dic4):
            primary_dic_counts += 1
    return element_dic_counts, middle_dic_counts, high_dic_counts, primary_dic_counts
dic_count = dic_count()
print("7. matching with dictionary complete","\n","== analysis complete ==","\n")

print(" == result ==")
print("책 :", path)
print("책에 포함된 단어 수 :", len(unique_words))
print("초딩 이해도 :", ((dic_count[0]/len(unique_words))*100).__round__(3), "%")
print("중딩 이해도 :", ((dic_count[1]/len(unique_words))*100).__round__(3), "%")
print("고딩 이해도 :", ((dic_count[2]/len(unique_words))*100).__round__(3), "%")
print("대딩 이해도 :", ((dic_count[3]/len(unique_words))*100).__round__(3), "%")

# # 사전에 없는 단어 표시
# primary_diff_words = []
# for i in unique_words:
#     if i not in np.array(primary_dic): # 사전 설정
#         primary_diff_words.append(i)
# len(primary_diff_words)
# primary_diff_words[0:20] # 사전에 없는 단어 20개 표시