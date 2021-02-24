# coding=utf-8
from flask import Flask
from flask import jsonify

from nlp.service.location_service import service_location_discovery
from nlp.service.segment_service import service_segment_without_stopwords, service_word_cloud
from nlp.service.sentiment_service import service_sentiment
from nlp.utils.sentiment_analysis import stone_emotion
from nlp.utils.location_discovery import stone_location
from nlp.utils.segment import stone_segment_without_stopwords

app = Flask(__name__)


@app.route('/nlp/sentiment/<text>/', methods=['GET'])
def sentiment(text: str):
    data = {
        'code': 200,
        'msg': '成功',
        'data': service_sentiment(text)
    }
    return jsonify(data)


@app.route('/nlp/location/<text>/', methods=['GET'])
def location(text: str):
    data = {
        'code': 200,
        'msg': '成功',
        'data': service_location_discovery(text)
    }
    print(data)
    return jsonify(data)


@app.route('/nlp/segment/<text>/', methods=['GET'])
def segment(text: str):
    data = {
        'code': 200,
        'msg': '成功',
        'data': service_segment_without_stopwords(text)
    }
    return jsonify(data)


# @app.route('/nlp/wordcloud/<text>/<timestamp>', methods=['GET'])
# def word_count(text: str, timestamp: int):
#     data = {
#         'code': 200,
#         'msg': '成功',
#         'data': service_word_cloud(text, timestamp)
#     }
#     return jsonify(data)


@app.errorhandler(Exception)
def default_error_handler():
    data = {
        'code': 500,
        'msg': '服务器内部错误',
        'data': '服务器内部错误'
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(threaded=True)

