# ch31_6.py
import turtle

t = turtle.Pen()

for x in range(1, 37):
    t.forward(100)      # 海龜向前繪線移動100
    t.left(90)          # 海龜方向左轉90度
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(100)         # 海龜方向左轉100度
    
