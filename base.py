class BaseNum():
    def __init__(self, num, base):
        if type(num) is str:
            self.struct = [int(i) for i in num]
        elif type(num) is list:
            self.struct = num
        self.base = base
    def toBase(self, newbase):
        # First convert to base 10
        sum = 0
        for i, digit in enumerate(reversed(self.struct)):
            sum += digit * (self.base ** i)
            
        # Now convert it to the desired base
        newstruct = []
        while True:
            newstruct.append(sum % newbase)
            sum = sum / newbase
            if(sum < newbase):
               newstruct.append(sum) 
               break
        return BaseNum(newstruct[::-1],newbase)
        
    def getNumStruct(self):
        return self.struct
 
# usage
binNum = BaseNum("1001010101110",2)
print binNum.toBase(16).getNumStruct()
 
# output
# [1, 2, 10, 14]
