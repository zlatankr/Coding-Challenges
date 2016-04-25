# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 19:14:38 2016

@author: zlatan.kremonic
"""

number_words = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
            7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
            90: 'Ninety', 0: ''}
            
def letters_count(n):
    if n in number_words:
        #print number_words[n]
        return len(number_words[n])
    elif len(str(n)) == 2:
        #print number_words[int(str(n)[0])*10], number_words[int(str(n)[1])]
        return len(number_words[int(str(n)[0])*10])+len(number_words[int(str(n)[1])])
    elif len(str(n)) == 3 and int(str(n)[1:]) > 0 and int(str(n)[1:]) in number_words:
        #print number_words[int(str(n)[0])], 'hundredand', number_words[n]
        return len(number_words[int(str(n)[0])])+len('hundredand')+len(number_words[int(str(n)[1:])])
    elif len(str(n)) == 3 and int(str(n)[1:]) > 0:
        #print number_words[int(str(n)[0])], 'hundredand', number_words[int(str(n)[1])*10], number_words[int(str(n)[2])]
        return len(number_words[int(str(n)[0])])+len('hundredand')+len(number_words[int(str(n)[1])*10])+len(number_words[int(str(n)[2])])
    elif len(str(n)) == 3:
        #print number_words[int(str(n)[0])], 'hundred', number_words[int(str(n)[1])*10], number_words[int(str(n)[2])]
        return len(number_words[int(str(n)[0])])+len('hundred')+len(number_words[int(str(n)[1])*10])+len(number_words[int(str(n)[2])])
    else:
        print 'onethousand'
        return len('onethousand')

def num_seventeen(n):
    counts = []
    for i in range(1, n + 1):
        print i
        counts.append(letters_count(i))
    return sum(counts)