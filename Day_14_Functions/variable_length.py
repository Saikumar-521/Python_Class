print([1,2,3,4],'sai',sep=',',end='\n')
'''
1.variable-length positinal argument
1. *args — Non-keyword Variable-length Arguments
✅ Definition:
*args is used when you want to pass multiple positional arguments to a function.
It collects them into a tuple.

✅ Syntax:
def function_name(*args):
    # args is a tuple
'''
def fun(*a):
    print(a)

fun(1,2,3,3,45,6,7,89,10)

def fun(*a):
    for i in a:
        print(i,end=' ')

fun(1,2,3,3,45,6,7,89,10)

# yes here we can declare keyword argument in variable length arguments,
# but the aruguments are placed in the right side
def key_word_with_variable_arg(*a,x,y):
    s=0
    for i in a:
        s=s+i
    return s,x,y

value=key_word_with_variable_arg(1,2,3,4,5,6,7,8,9,10,x=10,y=20)
print(value)  #here the out put in tuple formate


'''
variable length keyword arguments
2. **kwargs — Keyword Variable-length Arguments

✅ Definition:
**kwargs allows you to pass multiple keyword (name=value) arguments.
It collects them into a dictionary.

✅ Syntax:

def function_name(**kwargs):
    # kwargs is a dictionary
'''
def keyword(**kwarg):
    for k,v in kwarg.items():
        print(k,':',v) #a : 1 b : 2 c : 3 d : 4 e : 5

keyword(a=1,b=2,c=3,d=4,e=5)

def keyword(**kwarg):
    for k in kwarg.keys():
        print(k)  # a b c d e

keyword(a=1,b=2,c=3,d=4,e=5)


def keyword(**kwarg):
    for k in kwarg.values():
        print(k)  # 1 2 3 4 5

keyword(a=1,b=2,c=3,d=4,e=5)


def info(**i):
    print(i)

info(name='sai',age=22,ph=100,email='sai@gmail.com')

# yes,here we can use the positinal arguments with keyword-variable-length arguments,
# but positional argumants are placed at lift side

def positinal_with_kw_variable_len_arg(a,b,c,**x):
    d={}
    for k,v in x.items():
        d1={k:v}
        # d.update(d1)
        d |= d1
        # m={**d,**d1} # but it will get only last key-value pair only,it not get all keys and values from dictionary
    return a,b,c,d
val=positinal_with_kw_variable_len_arg(1,2,3,name='sai',age='22',ph=100)
print(val)  #(1, 2, 3, {'name': 'sai', 'age': '22', 'ph': 100})


# both variable length argumants and keyword variable length arguments

def student_info(course, *args,name, **kwargs):
    print("Course:", course)
    print("Subjects:", args)
    print('user name is :',name)
    print("Details:", kwargs)

student_info("B.Tech", "Maths", "Physics", name="Sai", year=4)







