# -*- coding:cp936 -*-
print ('M: Ԥ������')
print ("a: ÿ�¶�Ͷ���")
print ("x: һ��������")
print ("n: ��Ͷ����(��ʽ��Ϊn�η�)")
a = float(input("�ƻ��¶�Ͷ��"))
n = int(input("�ƻ�Ͷ�����ޣ�"))
x = float(input("Ԥ���������ʣ�"))
m = x / 100
M = 12 * a * (1 + m) * (-1 + (1 + m)**n) / m
H = M - 12 * a * n
Y = H / (12 * a *n)
print("Ͷ�����޵��ڱ�������ͣ�" + str(M))
print("Ͷ�����޵��������棺" + str(H))
print("�ʲ������ʣ�" + format(Y,'.5%'))
