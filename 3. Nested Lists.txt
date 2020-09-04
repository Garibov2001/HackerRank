Link: https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
Difficulty: Easy
Solution: 
if __name__ == '__main__':

    def FindLowest(argArr):
        minNumber = argArr[0][1]
        for eachList in argArr:
            if(eachList[1] < minNumber):
                minNumber = eachList[1]
        return minNumber

    def GetNameAndSort(argArr):
        lowNumber = FindLowest(argArr)
        nameList = []
        for eachList in argArr:
            if(eachList[1] == lowNumber):
                nameList.append(eachList[0])
        nameList.sort()
        return nameList

    def RemoveFirstGrade(argArr):
        minNumber = FindLowest(argArr)
        i = 0
        while(i < len(argArr)):
            if(argArr[i][1] == minNumber):
                argArr.pop(i)
            else:
                i += 1


    studentList = []
    # Arraye yigdigi algorithm
    for _ in range(int(input())):
        name = input()
        score = float(input())
        studentList.append([name, score])
    # 
    RemoveFirstGrade(studentList)

    for element in GetNameAndSort(studentList):
        print(element)