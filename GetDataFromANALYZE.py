from urllib.request import urlopen
from sqlalchemy import create_engine
from lxml.html import parse
from pandas.io.parsers import TextParser
from lxml.html import clean
cleaner = clean.Cleaner(style=True,scripts=True,page_structure=False,safe_attrs_only=False)
engine = create_engine('oracle://lb:lb@192.168.1.30:1521/tsbi')
fxsCODE =['11000175582',
'11000174501',
'11000257460',
'11000232926',
'11000178359',
'11000177243',
'11000239867',
'11000249133',
'11000176377',
'11000219723',
'11000172765',
'11000239134',
'11000233940',
'11000234146',
'11000215424',
'11000175485',
'11000217632',
'11000252225',
'11000173983',
'11000222044',
'11000216625',
'11000171850',
'11000174500',
'11000178639',
'11000182535',
'11000188823',
'11000176793',
'11000172896',
'11000176929',
'11000254533',
'11000236246',
'11000233937',
'11000179701',
'11000179273',
'11000236946',
'11000228928',
'11000234665',
'11000173878',
'11000175139',
'11000240738',
'11000198932',
'11000176448',
'11000239626',
'11000250425',
'11000175333',
'11000258138',
'11000174669',
'11000247832',
'11000240739',
# '11000241246',
'11000172794',
'11000177104',
'11000193723',
'11000245836',
'11000178742',
'11000176484',
'11000172938',
'11000172336',
'11000249525',
'11000247732',
'11000172724',
'11000180941',
'11000179414',
'11000220968',
'11000177053',
'11000176431',
'11000176187',
'11000173155',
'11000172566',
'11000179246',
'11000235924',
'11000172198',
'11000174967',
'11000249626',
'11000172218',
'11000220425',
'11000224429',
'11000172913',
'11000234330',
'11000202543',
'11000229430',
'11000251727',
'11000176352',
'11000174852',
'11000250130',
'11000177362',
'11000249027',
'11000178729',
'11000219167',
'11000201326',
'11000173462',
'11000176016',
'11000177235',
'11000173008',
'11000178161',
'11000177199',
'11000173469',
'11000251846',
'11000210666',
'11000200262',
]

def _unpack(row, kind='td'):
    elts = row.xpath('.//%s' %kind)
    # 根据标签的类型获取数据
    return [val.text_content() for val in elts]
    # 使用列表推导式返回一个列表
def parse_options_data(table):
    rows = table.xpath('.//tr')
    # 以table为当前路径，查找tr标签
    header = _unpack(rows[0], kind='td')
    # 查找th标签作为header
    data = [_unpack(r) for r in rows[1:]]
    # 剩下的行作为data
    return TextParser(data, names=header).get_chunk()
    # 返回一个DataFrame

def getNewDataAnalyze(uid):
    doc = parse(urlopen('http://data.eastmoney.com/invest/invest/'+uid+'.html'))
    print(doc)
    # doc2 =cleaner.clean_html(doc)
    # tables =doc2.xpath('//table')
    # print(len(tables))
    tables = doc.xpath('//table')
    # print(len(tables))
    df = parse_options_data(tables[0])
    df['FXSCODE']=uid
    # print(df)
    if str(df[0][0])!='暂无最新跟踪成分股...':
        df.to_sql('fxs_stcode', engine, if_exists='append', index=None)

    # df2 = parse_options_data(tables[1])
    # df.to_sql('fxs_stcode',engine,if_exists='append',index=None)
    # print(df2)

if __name__ == '__main__':
    for i in fxsCODE:
      print(i)
      getNewDataAnalyze(i)