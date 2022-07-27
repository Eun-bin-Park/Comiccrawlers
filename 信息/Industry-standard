import xlwt
import requests
from lxml import etree
import time

def getOnePage(url):
    headers = {
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    data = {
        'current': '1',
        'size': '15',
        'status': '现行'
    }
    html = requests.get(url=url,headers = headers,data=data)
    a = html.text
    selector = etree.HTML(html.text)
    infos = selector.xpath('//table[@class="table table-striped"]/tr')
    print(infos)
    for info in infos:
        try:
            yield {
                'standard_number': info.xpath('td[1]/text()')[0],
                'standard_name': info.xpath('td[2]/div/a/text()')[0],
                'industry_sectors': info.xpath('td[3]/text()')[0],
                'filing_date': info.xpath('td[4]/text()')[0].split(),
            }
        except IndexError:
            pass
header = ['标准号','标准名称','行业领域','备案日期']
encode = xlwt.Workbook(encoding='utf-8')
sheet = encode.add_sheet('Informations')
for h in range(len(header)):
    sheet.write(0, h, header[h])
urls = [r'https://hbba.sacinfo.org.cn/'.format(str(i)) for i in range(1,2)]
print(urls)
i = 1
for url in urls:
    Informations = getOnePage(url)
    for Information in Informations:
        time.sleep(0.1)
        sheet.write(i, 0, Information['standard_number'])
        sheet.write(i, 1, Information['standard_name'])
        sheet.write(i, 2, Information['industry_sectors'])
        sheet.write(i, 3, Information['filing_date'])
        i += 1
        print(i)
encode.save('信息平台.xls')


