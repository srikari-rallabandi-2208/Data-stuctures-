'''
LeetCode - problem 68
'''

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        def balanceSpaces(string, isLast):
            spacesToAdd = maxWidth - len(string)
            stringAsList = string.split(' ')
            
            if len(stringAsList) == 1 or isLast:
                return string + (' ' * spacesToAdd)
            else:
                while spacesToAdd:
                    for i in range(len(stringAsList) - 1):
                        if spacesToAdd:
                            stringAsList[i] += ' '
                            spacesToAdd -= 1
                        else:
                            break
            return ' '.join(stringAsList)
        
        output = []
        
        currLayer = ""
        for each in words:
            if not currLayer:
                currLayer += each
            elif len(currLayer + ' ' + each) <= maxWidth:
                currLayer += ' ' + each
            else:
                output.append(balanceSpaces(currLayer, False))
                currLayer = each
        
        output.append(balanceSpaces(currLayer, True))
        return output
