lst=[8,2,3,-1,7]
lp=1
def multiply():
    for i in lst:
        global lp
        lp *= i
    print(lp)
multiply()    

list1=[1,2,3,4,5,6,7,8,9]
lst2=[]
for i in list1:
    if i%2==0:
        lst2.append(i)
print(lst2)

def count_number():
    score=0
    def guess_score(points):
       nonlocal score 
       score+=points
    guess_score(20)    
    return score
round_score=count_number()
print("Round Score:",round_score)
