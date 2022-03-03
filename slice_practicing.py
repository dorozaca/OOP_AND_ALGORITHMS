# a ='python'
# b=[10,20,30,40,50,60]

# print(b[-1])
# print(b[-2:])
# print(b[:-2])
# print(b[::-1])
# print(b[1::-1])
# print(b[-1:-3:-1])
# print(b[-3::-1])

q='Welcome to my blog'

print(q[1::-1]) #1 the first 2 items reversed / The end (:) for STOP is determined by STEP and in this case is at the left
print(q[-1:-3:-1]) #2 the last 2 items reversed
print(q[-3::-1]) #3 everything except the last 2 items reversed
print(q[:-2]) #4 everything except the last 2 items- SPECIAL
print(q[-10:9]) #5 combining index nomenclatures negative and positive - SPECIAL
print(q[:-2:-1]) #6
print(q[:-2:1]) #7

#6-7 START doesn't have value explicitly stated therefore it is equal to None / index [0[] or index [-1] depending on the direction of the STEP 
# Only remember there are 2 ways to call indexes, allindexes have 2 names so to speak and we use each nomenclature depending upon what 
# we want to do # to make the slice generic for all posible sequence arguments (string, list, tuples)
# 4-5 in this same note, we can call START with +index nomenclatures and STOP with -index nomenclature and STEP will apply the direction
# Where it points ":" alone for STOP to indicate "to the end" is defined by the STEP direction. Check #1
# START always need to be greater than STOP, in consistency with direccion (STEP +/-)
#we can use negative index names with direction left to right (STEP +)
#Positive or negative signs for START ans STOP only means that index name system has changed.
# There is no -0, always start with -1 when using negative index names
#STOP is not inclusive, when used with STEP (-) returns value at its right while with STEP (+) returns value at its left
#we can conmbine both index nomenclatures (0,1,3 and -1,-2,-3) as in exercise above (#6 and #7) as long as 
# there is an actual interval and the STEP (direction) is consistent with it which means direction doesn't make the interval to fall out of bounds







# print(a[-1])
# print(a[-2:])
# print(a[:-2])
# print(a[::-1])
# print(a[1::-1])
# print(a[:-3:-1])
# print(a[-3::-1])




# A=list(range(1,10,1))
# B=list(range(9))

# print(A[5:2])
# print(A[-4:-7])
