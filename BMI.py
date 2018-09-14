weight = input('請輸入體重(kg)')
weight = float(weight)
height = input('請輸入身高(cm)')
height = float(height)
bmi = weight * 10000 / height / height   
if bmi < 18.5:
	print('BMI=', bmi,'體重過輕')
elif bmi >=18.5 and bmi < 24:
	print('BMI=', bmi,'正常範圍')
elif bmi >=24 and bmi <27:
	print('BMI=', bmi,'過重')
elif bmi >=27 and bmi <30:
	print('BMI=', bmi,'輕度肥胖') 
elif bmi >=30 and bmi <35:
	print('BMI=', bmi,'中度肥胖')
else:
	print('BMI=', bmi,'重度肥胖')
