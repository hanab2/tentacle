#
# # coding:utf-8
#
# from flask import Flask
# from flask import jsonify
# # from LAC import LAC
# import paddlehub as hub
#
# app = Flask(__name__)
#
#
# # @app.route('/nlp/segment/<text>', methods=['GET'])
# # def segment(text: str):
# #     lac = LAC(mode='seg')
# #     result = lac.run(text)
# #     data = {
# #         'code': 200,
# #         'msg': result
# #     }
# #     return jsonify(data)
#
#
# @app.route('/nlp/sentiment/<text>', methods=['GET'])
# def sentiment(text: str):
#     classfier = hub.Module(name='senta_lstm')
#     sentiments = classfier.sentiment_classify(data={"text": list(text)})
#     data = {
#         'code': 200,
#         'msg': sentiments[0].get('sentiment_key')
#     }
#     return jsonify(data)
#
#
# # @app.route('/nlp/wordcount/<text>', methods=['GET'])
# # def wordcount(text: str):
# #     wordlist = jieba.lcut(text)
# #     count = {}
# #     for word in wordlist:
# #         if len(word) > 1:
# #             count[word] = count.get(word, 0) + 1
# #     result = {
# #         'code': 200,
# #         'msg': count
# #     }
# #
# #     data = ' '.join(wordlist)
# #     image = imageio.imread('monkey.jpg')
# #     wordcloud = WordCloud(
# #         font_path="C:\\Windows\\Fonts\\HGDGY_CNKI.TTF",
# #         background_color="black",
# #         width=image.shape[0],  # 词云图宽度同原图片宽度
# #         height=image.shape[1],
# #         scale=3
# #     )
# #     wordcloud.generate(data)
# #     wordcloud.to_image().show()
# #     return jsonify(result)
#
#
# if __name__ == '__main__':
#     app.run()
