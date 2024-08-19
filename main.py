# import keyword

# print("Hello world!")
# print(keyword.kwlist)

import turtle

# สร้างหน้าต่างการวาด
screen = turtle.Screen()
screen.bgcolor("#ffffff")

# สร้างวัตถุเต่า
pen = turtle.Turtle()

# วาดสี่เหลี่ยม
for _ in range(4):
    pen.forward(100)  # เคลื่อนที่ไปข้างหน้า 100 หน่วย
    pen.right(90)     # หมุนขวา 90 องศา
    turtle.color("#333333")

    # turtle.penup()
    # pen.backward(100)

# ปิดหน้าต่างเมื่อคลิก
screen.exitonclick()
