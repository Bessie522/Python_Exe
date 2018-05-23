# -*- coding:cp936 -*-
print ('M: 预期收益')
print ("a: 每月定投金额")
print ("x: 一年收益率")
print ("n: 定投期数(公式中为n次方)")
a = float(input("计划月定投金额："))
n = int(input("计划投资年限："))
x = float(input("预期年收益率："))
m = x / 100
M = 12 * a * (1 + m) * (-1 + (1 + m)**n) / m
H = M - 12 * a * n
Y = H / (12 * a *n)
print("投资年限到期本金收益和：" + str(M))
print("投资年限到期总收益：" + str(H))
print("资产增加率：" + format(Y,'.5%'))
