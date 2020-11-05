import sys
file_name, work_hours, money_perhour, money_award = sys.argv
print((float(work_hours) * float(money_perhour)) + float(money_award))