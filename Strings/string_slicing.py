# Topic : String Slicing

'''String slicing in Python allows you to extract a portion of a string by specifying a start and end index'''

name = " H  a  r  r  y"
#        0  1  2  3  4
#        -5 -4 -3 -2 -1


print(name[0:2]) # this goes from 0 to 2-1 = 1 and we get Ha

print(name[2:-1]) # this will equals to 2:4 and the output is rr

# one another method of string slicing.
print(name[0:4:2]) # this will skips one character or one indices


print(name[:4]) # this will same as name[1:4]
print(name[1:]) # this will same as name[1:14] ; here 14 is the length of the string