set_1 = set()
set_2 = set()
for i in range(1,101):
    if i%2 ==1:
        set_1.add(i)
for i in range(1,101):
    if i%5 ==0:
        set_2.add(i)
s3 = set_1 & set_2
s4 = set_1 | set_2
s5 = set_2 - set_1
s6 = set_1 - set_2
print("A與B的交集：",s3)
print("A與B的聯集：",s4)
print("差集A-B:",s6)
print("差集B-A:",s5)

