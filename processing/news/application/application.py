import time

import schedule

from processing.news.worker.nlp_worker import location_process, sentiment_process, segment_process, status_process

schedule.every(1).seconds.do(location_process)
schedule.every(1).seconds.do(sentiment_process)
schedule.every(1).seconds.do(segment_process)
schedule.every(1).seconds.do(status_process)

if __name__ == '__main__':
    while True:
        schedule.run_pending()  # 运行所有可以运行的任务
        # time.sleep(1)
