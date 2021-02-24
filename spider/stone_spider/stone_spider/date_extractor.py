import re


class DateExtractor:
    # yyyy-MM-dd hh:mm
    pattern = r'[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}'

    @classmethod
    def extract(cls, text):
        return '%s:00' % (re.findall(DateExtractor.pattern, text)[-1])
