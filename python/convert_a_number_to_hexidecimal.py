import math

class Solution:
    def toHex(self, num: int) -> str:
        letter_map = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        num_map = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
        neg = num < 0
        if neg: num = num * -1
        
        def decToHex(num):
            hex = ""
            while(num > 15):
                div = int(math.floor(num/16))
                rem = num-(16*div)
                if rem > 9: let = letter_map[rem]
                else: let = str(rem)
                hex = let + hex
                num = div
            if num > 9: hex = letter_map[num] + hex
            else: hex = str(num) + hex
            return hex
        
        def hexToDec(hex):
            dec = 0
            length_hex = len(hex)
            for i in range(length_hex):
                digit = 1
                if(hex[i].isalpha()): digit = num_map[hex[i]]
                else: digit = hex[i]
                dec = int(dec) + ( int(digit) * (16**(length_hex-1-i)) )
            return dec
        
        def getTwosComp(hex):
            neg_hex = ""
            comp = ""
            for i in hex:
                if i.isalpha(): comp = str(15 - num_map[i])
                else: comp = str(15 - int(i))
                if int(comp) > 9: comp = letter_map[int(comp)]
                neg_hex = neg_hex + comp

            dec = hexToDec(neg_hex) + 1
            comp_hex = decToHex(dec)
            return comp_hex
        
        hex = decToHex(num) 
        expected_length = len(hex)
        
        if(neg):
            comp_hex = getTwosComp(hex)
            while(len(comp_hex) < expected_length):
                comp_hex = '0' + comp_hex
            while(len(comp_hex) < 8):
                comp_hex = 'f' + comp_hex
                
            return comp_hex
        
        return hex