math = {"Tom", "John", "Mary", "Jimmy", "Sunny", "Amy"}
eng = {"John", "Mary", "Tony", "Bob", "Pony", "Tom", "Alice"}
# 差集: a - b, 交集: a & b, 聯集: a | b
mpef = math - eng
mfep = eng - math
both = math & eng
total = math | eng

print("數學及格但英文不及格: " + str(mpef))
print("數學不及格但英文及格: " + str(mfep))
print("兩科都及格: " + str(both))
print("全班總共有 " + str(len(total)) + " 個同學\n")

hw = {"Tom": [80, 100, 90, 95], "John": [100, 93, 75, 80]}
tom = hw.get("Tom")
john = hw.get("John")

print("Tom的平均分數: " + str(sum(tom) / len(tom)))
print("John的平均分數: " + str(sum(john) / len(john)))
