bill_no = 1234567892
un1= 12345
un2 = 12435
cu = un2-un1
total = 0
if cu <= 300:
    total = cu * 3.50
elif 301 >= cu <= 500:
    total = cu * 4.50
else:
    total = cu * 5.50
print(bill_no,"is total used units is",cu,"total bill is",total)
