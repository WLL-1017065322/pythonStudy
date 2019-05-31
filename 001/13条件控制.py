# if语句

# if condition_1:
# #     statement_block_1
# # elif condition_2:
# #     statement_block_2
# # else:
# #     statement_block_3

# var1 = 100
# if var1:
#     print("if表达条件true")
#     print(var1)
#
# var2 = 0
# if var2:
#     print("2-if true")
#     print(var2)
#
# print("bye")


# age = int(input("你狗的年龄"))
#
# if age < 0:
#     print("口住！")
#
# elif age==1:
#     print("相当于14")
# else:
#     print("what?")
#
# input("enter退出")



# print(5 == 6)
# x,y = 5,6
# print(x == y)


number = 10
guess = 3
while number!=guess:
    guess = int(input("guess"))

    if number>guess:
        print("xiaole")
    elif number<guess:
        print("dale")
    else:
        print("greate")

