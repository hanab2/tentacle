import paddlehub as hub

senta = hub.Module(name='senta_lstm')

# text
test_text = [
    "不错呦",
    "哎，一般",
    "我爱你，我讨厌你"
]

# classify
results = senta.sentiment_classify(data={"text": test_text})

# result
for result in results:
    print(result)
print(type(results))
