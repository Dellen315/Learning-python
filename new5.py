# -*- coding:utf-8 -*-

height = float(input('你的身高:'))
weight = float(input('你的体重：'))
bmi = weight/(height*height)
if bmi < 18.5:
	print('你的体重过轻！')
elif bmi <= 25:
	print('你的体重正常!')
elif bmi <= 28:
	print('你的体重过重！')
elif bmi <= 32:
	print('你属于肥胖！')
else:   #bmi > 32
	print('你属于严重肥胖！')
	
