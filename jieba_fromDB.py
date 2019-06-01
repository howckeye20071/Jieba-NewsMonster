# coding:utf8
import jieba
import pymysql
import jieba.analyse

jieba.load_userdict("C:/news/tags_set.txt")
jieba.analyse.set_stop_words("C:/news/stopword.txt")
# content = "祈堂老街早期是金瓜石最繁華的商店街，後來雖然比較沒落，不過獨特的懷舊風格，還是吸引不少遊客，但日前就有民眾發現，30公尺長的老街階梯被人漆上七彩油漆，有人認為失去了老街的韻味，不過創作的人出來解釋，這是因為欄杆部分木材腐壞，才會整修，這也意外吸引網美到訪。倚著七彩欄杆，坐在階梯口，新人親密合影，或是拿起自拍棒，遊客快門按不停，不說還不知道，這多彩的階梯竟然就在金瓜石祈堂老街上，有別於以往老街給人的印象，這跳tone風格意外引起論戰。比一比過去的老街階梯，木質把手，色彩比較低調，充滿濃濃懷舊氛圍，新的階梯畫上七彩顏色，雖然少了復古味。不過卻多了活潑感，實際詢問遊客，不少人反應不錯，不過也有人說這變得沒有老街味了。創作者是土生土長在地人，他說當初其實是不捨家附近欄杆年久失修，逐漸腐壞，擔心發生危險，才會和朋友花2千元，重新漆上比較不容易腐鏽的顏料，沒想到引發討論。創作者：「民眾反應都很不錯，也是民眾自己取名叫彩虹梯。」祈堂老街早期是金瓜石最繁華的商店街，不過後來停止產煤礦後逐漸沒落，目前住在這的老人家占大多數，美感定義不同，但無論如何，可以確定的是30公尺長階梯變彩色，確實吸引不少遊客拍照駐足。"

db = pymysql.connect("localhost", "egg", "egg", "news")
cursor = db.cursor()

sql = "SELECT text FROM setn WHERE tags LIKE  '%美國%'"
cursor.execute(sql)
text_tuple = cursor.fetchall()

for texts in text_tuple:
    text = texts[0]

# ------------------------------------
    # 一、先用切字看有沒有一定要切出來的新詞，例如專有名詞、人名、地名等
    # 把新詞加進：tags_set.txt
    # 記得存檔，用以下順序多次檢驗：找新詞＞存檔＞再切＞找新詞＞存檔...

    # word = jieba.cut(text)
    # print('/'.join(word))

# ------------------------------------
    # 二、把切字部分註解掉，用關鍵字提取看結果有沒有不合理或無意義的關鍵字
    # 不確定的請先不要刪並另外紀錄，應刪除的如：不太敢、不想、改成、發生意外、15歲...等
    # 把停用詞加進：stopword.txt
    # 記得存檔，用以下順序多次檢驗：找停用詞＞存檔＞再找＞找停用詞＞存檔...

    kw = jieba.analyse.extract_tags(text, topK=20, withWeight=False, allowPOS=())
    print(kw)
