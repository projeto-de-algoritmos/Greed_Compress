#https://www.spoj.com/problems/BUSYMAN/

#The first line consists of an integer T, the number of test cases. For each test case the first line consists of an integer N, the number of activities. 
# Then the next N lines contains two integers m and n, the start and end time of each activity.

def endvalue(arr):
    return int(arr[1])


def AlgoritmoAmbicioso(self,tempoiniciofinal):
    tempoiniciofinal.sort(key = endvalue,reverse = False)
    final = 0
    total = 0


    for i in range(self):

        if (int(tempoiniciofinal[i][0])>=final):
            final = int(tempoiniciofinal[i][1])

            total+=1

    return total

testcase = int(input())
for i in range(testcase):
    self=int(input())
    tempoiniciofinal = [0]*self
    for i in range(self):
        tempoiniciofinal[i] = (input().strip().split(' '))
    print(AlgoritmoAmbicioso(self,tempoiniciofinal))