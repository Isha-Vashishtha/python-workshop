dictionaries={
     'x':'10',
     'y':'20',
     'z':'30'
     }
for x in dictionaries.items():
    print(x)

num=int(input("Enter the number:"))
squared_dict={i:i**2 for i in range(1,num+1)}
print(squared_dict)

squared_dict1={num:num**2 for num in range(1,16)}
print(squared_dict1)
      
my_dict={
    'data1':100,
    'data2':-54,
    'data3':247
    }
s_um=0
a=my_dict.values()
for i in a:
    s_um=s_um+i
print(s_um)
def fun():
    
    my_dict2={'red':'#ff00000','green':'#000000','black':'#2345'}
    mykeys=list(my_dict2.keys())
    mykeys.sort()
    sorted_dict={i:my_dict2[i] for i in mykeys}
    print(sorted_dict)
    dict_={1:10,2:20,3:30,4:40,5:50,6:60}
    if  1 in dict_:
     print("Yes,the key is in the dictionary.")
fun()
