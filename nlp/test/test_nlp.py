# from snownlp import SnowNLP
# text = '你站在桥上看风景，看风景的人在楼上看你。明月装饰了你的窗子，你装饰了别人的梦'
# snow = SnowNLP(text)
# print(snow.sentiments)

# from ltp import LTP
# text = '你站在桥上看风景，看风景的人在楼上看你。明月装饰了你的窗子，你装饰了别人的梦'
# ltp = LTP()
#
# print(ltp.tokenizer(text))

# from snownlp import SnowNLP
#
# text = '你站在桥上看风景，看风景的人在楼上看你。明月装饰了你的窗子，你装饰了别人的梦'
# snow = SnowNLP(text)
# print(snow.words)
#
# print(snow.tags)


# import jiagu
#
# print(jiagu.seg('你站在桥上看风景，看风景的人在楼上看你。明月装饰了你的窗子，你装饰了别人的梦'))
# print(jiagu.sentiment('你站在桥上看风景，看风景的人在楼上看你。明月装饰了你的窗子，你装饰了别人的梦'))

# from LAC import LAC
#
# lac = LAC(mode='seg')
#
# # 单个样本输入，输入为Unicode编码的字符串
# text = u"LAC是个优秀的分词工具"
# seg_result = lac.run(text)
# print(seg_result)
# # 批量样本输入, 输入为多个句子组成的list，平均速率会更快
# texts = [u"LAC是个优秀的分词工具", u"百度是一家高科技公司"]
# seg_result = lac.run(texts)
# print(seg_result)

# import jieba
#
# s = 'NLPIR分词系统前身为2000年发布的ICTCLAS词法分析系统，从2009年开始，为了和以前工作进行大的区隔，并推广NLPIR自然语言处理与信息检索共享平台，调整命名为NLPIR分词系统。'
# wordList = jieba.lcut(s)
# wordCount = {}
# for word in wordList:
#     if len(word) > 1:
#         wordCount[word] = wordCount.get(word, 0) + 1
#
# print(wordCount)


# from wordcloud import WordCloud
# import imageio
#
# data = ' '.join(wordList)
#
# print(type(data))
# image = imageio.imread('monkey.jpg')
# wordCloud = WordCloud(
#     font_path="C:\\Windows\\Fonts\\HGDGY_CNKI.TTF",
#     background_color="black",
#     width=image.shape[0],  # 词云图宽度同原图片宽度
#     height=image.shape[1],
#     scale=3
# )
# wordCloud.generate(data)
# wordCloud.to_file("monkey2.jpg")
# wordCloud.to_image().show()

# import paddlehub as hub
#
# senta = hub.Module(name='senta_lstm')
#
# # text
# test_text = [
#     "不错呦",
#     "哎，一般"
# ]
#
# # classify
# results = senta.sentiment_classify(data={"text": test_text})
#
# # result
# for result in results:
#     print(result)
# print(type(results))
