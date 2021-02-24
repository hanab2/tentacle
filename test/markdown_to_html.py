# -*- coding: utf-8 -*-
import markdown
from bs4 import BeautifulSoup

md = '''

**淮浦路所：开展[治安](https://news.163.com/news/search?keyword=%E6%B2%BB%E5%AE%89)清查行动**


![淮安突击检查70家旅馆、KTV 发现...](https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2021%2F0216%2Ff32c9300j00qom04b002zc000rs00kug.jpg&thumbnail=660x2147483647&quality=80&type=jpg)


![淮安突击检查70家旅馆、KTV 发现...](https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2021%2F0216%2Fd4c5348aj00qom04b002ac000rs00kug.jpg&thumbnail=660x2147483647&quality=80&type=jpg)


 AD200x300\_2 

为有效打击各类[违法](https://news.163.com/news/search?keyword=%E8%BF%9D%E6%B3%95)[犯罪活动](https://news.163.com/news/search?keyword=%E7%8A%AF%E7%BD%AA%E6%B4%BB%E5%8A%A8)，确保辖区老百姓过一个平安祥和的春节，2月13至14日，涟水县公安局淮浦路派出所在辖区内组织开展[社会面](https://news.163.com/news/search?keyword=%E7%A4%BE%E4%BC%9A%E9%9D%A2)治安清查行动。


通过采取治安清查、安全检查、隐患排查、设卡盘查、社会面巡查等有效手段，在宾馆、网吧、娱乐场所等治安复杂场所、内部单位、重点路段等安全管理重点区域开展地毯式清查，进一步挤压违法犯罪活动空间，有效减少了各类治安危害事故的发生。此次行动，共出动警力45人，检查重点单位、[旅馆](https://news.163.com/news/search?keyword=%E6%97%85%E9%A6%86)、网吧、KTV等70余家，现场督改隐患16处，下发责令整改通知书5份。


![](https://static.ws.126.net/163/f2e/product/post_nodejs/static/logo.png)
'''


html = markdown.markdown(md)
print(html)
print('================')
soup = BeautifulSoup(html, 'html.parser')
print(soup.get_text())
print(type(soup.get_text))

