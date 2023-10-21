#學生總分為300
#有些學生可以加分5%
#如果加分超過300，就以300分為準

import pyinputplus as pyip

scores = pyip.inputInt("請輸入學生分數:",min=0,max=300)
print(scores)
isYes = pyip.inputMenu(['Yes','No'],prompt="學生是否符合加分條件(請選擇1 Or 2):\n",numbered=True)
if isYes == 'Yes':
    scores *= 1.05
    if scores > 300:
        scores = 300     

print(f"學生分數為{scores}")
