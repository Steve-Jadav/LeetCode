class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()    
        if (len(str) == 0):
            return 0
    
        minimum = ord('0')
        maximum = ord('9')
        result = 0
        
        # If the first character is not a numeric digit or '+' or '-'
        if ( (ord(str[0]) > maximum or ord(str[0]) < minimum) ):
            if ( str[0] != '-' and str[0] != '+' ):
                return 0
        
        # Valid conversion can only take place if the first element of the list is a
        # valid integral number
        number = str.split(' ')[0]
        
        for i in range(1, len(number)):
            if ( (ord(number[i]) < minimum) or (ord(number[i]) > maximum) ):
                number = number[:i]
                break
                
        i = 0
        j = len(number) - 1
        sign = 1
        
        if (number[0] == '-'): 
            sign = -1
            i = 1
            j -= 1
        elif (number[0] == '+'):
            sign = 1
            i = 1
            j -= 1
      
        while (i < len(number)):
            current_int = ord(number[i]) - ord('0')
            result += current_int * pow(10, j)
            i += 1
            j -= 1
            
        result *= sign

        if (result < -(2**31)):
            return -(2**31)
        elif (result > (2**31 - 1)):
            return (2**31 - 1)
        else:
            return result
