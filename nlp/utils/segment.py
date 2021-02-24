# coding=utf-8
from LAC import LAC
from typing import List

lac = LAC(mode='lac')
'''
stopwords_tag_set内容是按照lac的词性选择的
具体请看 https://github.com/baidu/lac
'''
stopwords_tag_set = {'v', 'vd', 'a', 'ad', 'an', 'd', 'm', 'q', 'r', 'p', 'c', 'u', 'xc', 'w'}


def stone_segment(text: str) -> List[str]:
    return lac.run(text)[0]


def stone_segment_without_stopwords(text: str) -> List[str]:
    result = []
    segment = lac.run(text)
    for word, tag in zip(segment[0], segment[1]):
        if tag not in stopwords_tag_set:
            result.append(word)
    return result


if __name__ == '__main__':
    example_text = '''
    【加拿大承认文化衫冒犯中国公众中国外交部：加方应确保此类事件不再发生】加拿大驻华使馆在其网站发表声明称，该使馆人员订制有关文化衫的个人行为冒犯了中国公众情绪，加驻华使馆对此表示由衷遗憾。对此，中国外交部发言人汪文斌8日表示，加方应引以为戒，确保此类事件不再发生。（记者王骁波）
    '''
    segment_result = stone_segment_without_stopwords(example_text)
    print(segment_result)
