std = [["A", "B", "A", "C", "C", "D", "E", "E", "A", "D"],
       ["D", "B", "A", "B", "C", "A", "E", "E", "A", "D"],
       ["E", "D", "D", "A", "C", "B", "E", "E", "A", "D"],
       ["C", "B", "A", "E", "D", "C", "E", "E", "A", "D"],
       ["A", "B", "D", "C", "C", "D", "E", "E", "A", "D"],
       ["B", "B", "E", "C", "C", "D", "E", "E", "A", "D"],
       ["B", "B", "A", "C", "C", "D", "E", "E", "A", "D"],
       ["E", "B", "E", "C", "C", "D", "E", "E", "A", "D"]]
key = ["D", "B", "D", "C", "C", "D", "A", "E", "A", "D"]

for ans in std:
    tru = 0  # 答對題數歸零
    for i in range(0, 10):  # 用index來比對
        if ans[i] == key[i]:
            tru = tru + 1
    print("學生", std.index(ans), ": 答對", tru, "題")
