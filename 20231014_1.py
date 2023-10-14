side = int(input('請輸入對邊:'))
another_side = int(input('請輸入斜邊:'))
#把變數組合在一起,用逗號分開
#display(side, another_side)
import math
radian = math.asin(side/another_side)
degree = math.degrees(radian)
print(round(degree,2))