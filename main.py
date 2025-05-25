# قراءة عدد الساعات والأجر لكل ساعة من المستخدم
xh = input('Enter hours: ')
xr = input('Enter rate per hour: ')

# تحويل إلى أعداد عشرية
fh = float(xh)
fr = float(xr)

# حساب الأجر
if fh <= 35:
  pay_total = fh * fr
elif fh <= 50:
  regular_pay = 35 * fr
  overtime_hours = fh - 35
  overtime_pay = overtime_hours * fr * 1.25
  pay_total = regular_pay + overtime_pay
else:
  regular_pay = 35 * fr
  mid_overtime = 15 * fr * 1.25  # من 36 إلى 50
  high_overtime = (fh - 50) * fr * 1.5
  pay_total = regular_pay + mid_overtime + high_overtime

# طباعة الناتج
print("الأجر الإجمالي هو:", pay_total)
