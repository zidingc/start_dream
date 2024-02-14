import os
"""
import os
os.system('ipconfig')
print('----------------------------------------')
os.open('D:\\czd_script\1.txt','a')

"""
#
# os.system('ipconfig')
# print('----------------------------------------')
# os.open('D:\\czd_script\1.txt', 'a')

# print("hello world")  # print("hello world")
# money = 50
# bing = 10
# kele = 5
# print("当前钱包余额：", money, "元")
# print("购买冰淇淋，花费：", bing, "元")
# print("购买可乐，花费：", kele, "元")
# print("最终，钱包剩余：", money-bing-kele,"元")
# print("黑马", "程序员")
# print("黑马" + "程序员")
# ask_address = "asdha"
# cao_zi_ding = "sas"
# a = 5423526.715212
# print("ahsdka: %5.2f" % a )
# name = "传智播客"
# stock_price = 19.99
# stock_code = "003032"
# stock_price_daily_growth_factor = 1.2
# growth_days = 7
# a = stock_price
# for i in range(0,7):
#     a*=1.2
#
#
# print(f"公司：{name},股票代码：{stock_code},当前股价{stock_price}\n"
#       "每日增长系数是：%.1f,经过%d天的增长后，股票达到了：%.2f" % (stock_price_daily_growth_factor,growth_days,a))
#
# b = 19.99*1.2**7
# print(b)
#
# import const
# print("欢迎来到动物园")
# age = int(input("你多大了 ： "))
# if age  >= 18:
#     print("你成年了票价10元\n祝您游玩愉快")
# else:
#     print("儿童免费")

# num = 10
# guess_num = int(input())
# second_num = None
# last_num = None
# if num != guess_num:
#     print("please input first number:",guess_num )
#     second_num = int(input())
# elif num != second_num:
#
#     print("incorrect please again input",second_num)
#     last_num = int(input())
# else:
#     print("incorrect please again input", last_num)

# if 18 <= int(input("年龄：")) <30:
#     if int(input("入职时间："))>2 or int(input("级别 ： ")) > 3:
#         print("可领取")
#     else:
#         print("不可领取")
# else:
#     print("不可领取")

# import random
#
#
# num = random.randint(1,10)
# if int(input("猜:")) > num:
#     print("你猜大了")
#     if int(input("猜:")) > num:
#         print("你猜大了")
#         if int(input("猜:")) > num:
#             print("你猜大了")
#         elif :
# elif



# import argparse
# parse = argparse.ArgumentParser()
# parse.add_argument("-x",type=int, choices=[1,2,3,])
# parse.add_argument("-b","--b",type=str,default="1")
# parse.add_argument("-a","--age",type=int,default=1)
# parse.add_argument("-w","-weight", type=int, default=60)
#
#
#
# if __name__ == "__main__":
#     args = parse.parse_args()
#     if args.x == 1:
#         args.age = 14
#         args.weight = 65
#         print(args)
#     elif args.x == 2:
#         args.age = 76
#         args.weight = 45
#         print(args)
#     elif args.x == 3:
#         args.age = 36
#         args.weight = 34
#         print(args)
# import requests
#
#
# res = requests.get(url="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html/putty.exe")
#              # headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"})
# file_object = open(r"C:\share\1.exe", mode='wb')
# file_object.write(res.content)
# file_object.close()
#
# import wget
# url = 'https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html/putty.exe'
# path = 'C:/share/1.exe'
# wget.download(url,path)

from selenium import webdriver

opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opt)

driver.get('https://www.baidu.com')
driver.find_element_by_xpath()
print("hahah")


