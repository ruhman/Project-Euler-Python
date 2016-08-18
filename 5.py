# i = 2
# la = True
# mult=True
# while la==True:
#     for j in range (2,21):
#         if i % j !=0:
#             mult=False
#     if mult==True:
#         print("Resultado:")
#         print(i)
#         la=False
#         break
#     print(i)
#     i+=2050
# i = 2
# num = 20
# la=True
# while la ==True:
#     while i <= 20:
#         if num % i !=0:
#             to=True
#             break
#
#         i+=1
#     if to == False:
#         print(num)
#     num+=2

# end = 1
# for i in range (1,20):
#     end = end * i
#
# #end = 1
# print(end)
check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def find_solution(step):
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None
solution = find_solution(2)
if solution is None:
    print ("No answer found")
else:
    print ("found an answer:", solution)
