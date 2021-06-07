# Basic - Print all integers from 0 to 150.
for num in range(151):
    print(num)
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for n in range(5, 1001, 5):
    print(n)
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for dojoNum in range(1,101):
    if dojoNum % 10 == 0:
        print("Coding Dojo")
        continue
    if dojoNum % 5 == 0:
        print("Coding")
        continue
    else:
        print(dojoNum)
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
x = 0
for huge in range(500000):
    if huge % 2 != 0:
        x = x + huge
        continue
print(x)
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for countdown in range(2018, 0, -4):
    print(countdown)
# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9 
mult = 3
for multLowHigh in range(lowNum, highNum + 1):
    if multLowHigh % mult == 0:
        print(multLowHigh)
        continue
