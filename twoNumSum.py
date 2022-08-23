class TwoNumSum:
    def __init__(self, inputList:list, inputTarget:int):
        self.sumList = inputList
        self.sumTarget = inputTarget

    def twoNumSum_brutalForce(self) -> list:
        if self.sumList is None:
            return []
        if self.sumTarget is None:
            return []
        outputList = []
        for i in range(len(self.sumList)):
            for j in range(i+1, len(self.sumList)):
                item1 = self.sumList[i]
                item2 = self.sumList[j]
                if item1 + item2 == self.sumTarget:
                    #print(str(item1) + "+" + str(item2) + "=" + str(self.sumTarget))
                    outputList.append([]) # Create a new item for the output array
                    outputList[-1] = [item1, item2] # The last item of the array
        return outputList

    # Two num sum using Dictionary of Python
    # input array = [9, 2]
    #      target = 11
    #   key array = [2, 9]
    #  dictionary = [2:9, 9:2]
    # check if input[current] is in dictionary.keys
    def twoSum_dictionary(self) ->list:
        if self.sumList is None:
            return []
        if self.sumTarget is None:
            return []
        outputList = []
        sumDictionary = {}
        for i in range(len(self.sumList)):
            key_temp = self.sumTarget - self.sumList[i]
            if self.sumList[i] in sumDictionary.keys():
                outputList.append([])
                outputList[-1] = [self.sumList[i], sumDictionary[self.sumList[i]]]
            else:
                sumDictionary[key_temp] = self.sumList[i]
        return outputList


inputList_1 = [11, 1, 2, 3, 4, 5, 6, 10, 0, 7, 8, 9]
inputTarget_1 = 11

twoSum1 = TwoNumSum(inputList_1,inputTarget_1)
#print(twoSum1.twoNumSum_brutalForce())
print(twoSum1.twoSum_dictionary())
