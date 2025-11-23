n=78965
g=0
while n!=0:
    r=n%10
    if r>g:
        g=r
    n=n//10

print(g)

s='sai kumar'
v='aeiou'
for i in range(len(s)-1):
    if s[i] in v:
        print(s.replace(s[i],'*'))
    else:
        print(s[i])

print(s)

res=''
for i in range(len(s)-1):
    if s[i] in v:
        res+='*'
    else:
        res+=s[i]
print(res)