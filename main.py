import xlrd
import xlwt
from xlutils.copy import copy

# 输入书单Excel路径
str1 = input("请输入所要购买的书的Excel路径：")
buy = xlrd.open_workbook(str1)

# 读取书名，放入一个元组，初始化价格，位置
buyBookName = []
buyBookPrice = []
buyBookFrom = []
# 对所有标签循环
buyWb = buy.sheet_by_index(0)
# 读取“书名“栏
buyBookName = buyBookName + buyWb.col_values(buyWb.row_values(0).index('书名'))

# 去掉”书名“两个字
for name in buyBookName:
    buyBookFrom = buyBookFrom + [' ']
    buyBookPrice = buyBookPrice + [100000]  # 价格要小于100000
for name in buyBookName:
    try:
        buyBookName.pop(buyBookName.index('书名'))
        buyBookFrom.pop()
        buyBookPrice.pop()
    except:
        break

# 输入所有Excel路径，以over结束
bookExcel = []
while "over" not in bookExcel:
    str2 = input("Please input ")
    bookExcel.append(str2)
bookExcel.pop()

# 遍历每个文件
for url in bookExcel:
    wb = xlrd.open_workbook(url)
    # 遍历每个标签
    for p in range(0,wb.nsheets-1):
        sh=wb.sheet_by_index(p)
        # 找到书名栏和价格栏
        bNumber=sh.row_values(0)
        try:
            bookNameCol = sh.col_values(bNumber.index('书名'))
            bookPriceCol = sh.col_values(bNumber.index('实洋'))
        except:
            continue
        # 对元组中的每个值，找出第一匹配项的索引位置
        for name in buyBookName:
            try:
                bookNameRowNumber = bookNameCol.index(name)
                # print(bookNameRowNumber)
                # print(name)
            except:
                continue
            # 得到价格
            price = sh.cell_value(bookNameRowNumber, bNumber.index('实洋'))
            # 比较价格与上一价格大小，取较小值放入价格列表
            if buyBookPrice[buyBookName.index(name)] > price:
                buyBookPrice[buyBookName.index(name)] = price
                buyBookFrom[buyBookName.index(name)] = "%s,%s" % (url, sh.name)
            # 删除第一匹配项
            # 若没有匹配项（return value error），跳出循环

# 写入Excel
t = 0
buyWb=buy.sheet_by_index(0)
for p in range(0,buy.nsheets):
    buyc=copy(buy)
    buyWbc=buyc.get_sheet(0)
    buyWbc.write(0, 8, '价格')
    buyWbc.write(0, 9, '位置')
    for i in range(1, buyWb.nrows):
        buyWbc.write(i, 8, buyBookPrice[t])
        buyWbc.write(i, 9, buyBookFrom[t])
        t = t + 1
buyc.save("11111.xls")
