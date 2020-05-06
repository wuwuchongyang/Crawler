import requests


def sendft():
    SCKEY = 'xxxxxx'  # 方糖给的SCKEY 具体可访问http://sc.ftqq.com/?c=code 获取
    content = '健康打卡因意外而执行错误,请手动执行打卡。待作者更新后可重新拉取代码。[相关代码请点我](https://github.com/JoJoJoinme/Crawler/tree/master/%E5%81%A5%E5%BA%B7%E6%89%93%E5%8D%A1)'
    data = {
        'text': '健康打卡',
        'desp': content,
    }
    requests.get('http://sc.ftqq.com/{0}.send?text={1}&desp={2}'.format(SCKEY, data['text'], data['desp']))


if __name__ == '__main__':
    sendft()


