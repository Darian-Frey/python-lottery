import random

lott_num = []
ran_num = 0

# print 6 lottery numbers

for i in range(0, 6):
    ran_num = random.randint(1, 49)
#    print(ran_num)
    while ran_num in lott_num:
        ran_num = random.randint(1, 49)
    lott_num.append(ran_num)

print(lott_num)
#   prints lottery numbers toa text file
#open("./lott.txt", "a").write(f"\n{str(lott_num[0])}, "
#                              f"{str(lott_num[1])}, "
#                              f"{str(lott_num[2])}, "
#                              f"{str(lott_num[3])}, "
#                              f"{str(lott_num[4])}, "
#                              f"{str(lott_num[5])}")

print("The numbers for today are {0}, {1}, {2}, {3}, {4}, {5}".format(str(lott_num[0]), str(lott_num[1]),
                                                                      str(lott_num[2]), str(lott_num[3]),
                                                                      str(lott_num[4]), str(lott_num[5])))

print("The numbers for today are " + str(lott_num[0]) + ", " + str(lott_num[1]) + ", " + str(lott_num[2]) + ", "
      + str(lott_num[3]) + ", " + str(lott_num[4]) + ", " + str(lott_num[5]))

print(f"The numbers for today are {str(lott_num[0])}, {str(lott_num[1])}, {str(lott_num[2])}, "
      f"{str(lott_num[3])}, {str(lott_num[4])}, {str(lott_num[5])}")
