#1
price_list = [3200, 32150, 32000, 32500]
for i, data in enumerate(price_list) : print(i, data)

#2
for i in range(1, 4): print(90 + 10 * i, price_list[i])

#3
for X in range(2002, 2051, 4) : print(X)

#4
for num in range(10) : print(num / 10)

#5
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)

#6
file_name = "보고서.xlsx"
file_name.endswith("xlsx")
print(file_name)

#7
a = "hello world"
a.split()
print(a)

#8
date = "2020-05-01"
date.split("-")
print(date)

#9
상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",","")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))

#10-7번 문제와 같음

#11
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#12
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

#13
리스트 = [3, 100, 23, 44]
for 변수 in 리스트:
    if 변수 % 3 ==0:
        print(변수)
