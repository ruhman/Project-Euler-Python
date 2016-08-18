results = []
with open('prob67data.txt') as inputfile:
    for line in inputfile:
        lines=line.strip().split(',')
        for i in lines:
            nums=i.strip().split(" ")
            results.append(nums)

for line,row in reversed(list(enumerate(results))):
    for index, item in enumerate(row):
        bottomrow=line+1
        if line !=len(results)-1:
            sum1=int(item) + int(results[bottomrow][index])
            sum2=int(item) + int(results[bottomrow][index+1])
            if sum1>=sum2:
                results[line][index]=sum1
            else:
                results[line][index]=sum2


print(results[0][0])
