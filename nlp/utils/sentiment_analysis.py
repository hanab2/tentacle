# coding=utf-8
import paddlehub as hub

senta = hub.Module(name='senta_lstm')


def stone_emotion(text: str) -> str:
    text_list = list()
    text_list.append(text)
    results = senta.sentiment_classify(data={"text": text_list})
    return results[0].get('sentiment_key', '未识别')


if __name__ == '__main__':
    example_text = '''
    【加拿大承认文化衫冒犯中国公众中国外交部：加方应确保此类事件不再发生】加拿大驻华使馆在其网站发表声明称，该使馆人员订制有关文化衫的个人行为冒犯了中国公众情绪，加驻华使馆对此表示由衷遗憾。对此，中国外交部发言人汪文斌8日表示，加方应引以为戒，确保此类事件不再发生。（记者王骁波）
    '''
    emotion_result = stone_emotion(example_text)
    print(emotion_result)
