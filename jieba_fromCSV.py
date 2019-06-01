# coding:utf8
import jieba
import jieba.analyse
import csv

jieba.load_userdict("D:/news/tags_set.txt")
jieba.analyse.set_stop_words("D:/news/stopword.txt")

# 讀取CSV取資料
i = 30000

with open('D:/news/csv/setn' + str(i) + ".csv", 'r', encoding='utf8')as csvfile:
    data = csv.reader(csvfile)

    # 增加csv的讀取句數
    csv.field_size_limit(100000000)

    for texts in data:
        text = texts[3]

        # ------------------------------------
        # 一、先用切字看有沒有一定要切出來的新詞，例如專有名詞、人名、地名等
        # 把新詞加進：tags_set.txt
        # 記得存檔，用以下順序多次檢驗：找新詞＞存檔＞再切＞找新詞＞存檔...

        word = jieba.cut(text)
        print('/'.join(word))

        # ------------------------------------
        # 二、把切字部分註解掉，用關鍵字提取看結果有沒有不合理或無意義的關鍵字
        # 不確定的請先不要刪並另外紀錄，應刪除的如：不太敢、不想、改成、發生意外、15歲...等
        # 把停用詞加進：stopword.txt
        # 記得存檔，用以下順序多次檢驗：找停用詞＞存檔＞再找＞找停用詞＞存檔...

        # kw = jieba.analyse.extract_tags(text, topK=20, withWeight=False, allowPOS=())
        # print(kw)

