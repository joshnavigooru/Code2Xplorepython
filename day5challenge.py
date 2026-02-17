n=int(input("enter package weights:"))
weights=[]

for i in range(n):
    w=int(input("enter weight:"))
    weights=weights+[w]

very_light=[]
invalid_entries=[]
normal_load=[]
heavy_load=[]
overload=[]
for w in weights:
    if w<0:
        invalid_entries=invalid_entries+[w]
    elif w<=5:
        very_light=very_light+[w]
    elif w<=25:
        normal_load=normal_load+[w]
    elif w<=60:
        heavy_load=heavy_load+[w]
    else:
        overload=overload+[w]
name=input("enter full name:")
l=0
for i in name:
    if i!=" ":
        l=l+1
PLI=l%3
print("length =",l)
print("pli=",PLI)
affected_items=0
if PLI==0:
    print("Rule A applied:overload moved to invalid entries")
    for item in overload:
        invalid_entries=invalid_entries+[item]
        affected_items=affected_items + 1
    overload=[]
elif PLI==1:
        print("Rule B applied:very light items removed")
        affected_items=len(very_light)
        very_light=[]
else:
     print("Rule c applied:only normal and heavy kept")
     affected_items=len(very_light)+len(overload)
     very_light=[]
overload=[]
valid_count=0
for item in very_light:
    valid_count=valid_count+1
for item in normal_load:
    valid_count=valid_count+1
for item in heavy_load:
    valid_count=valid_count+1
for item in overload:
    valid_count=valid_count+1
print("very light:",very_light)
print("normal load:",normal_load)
print("heavy load:",heavy_load)
print("overload:",overload)
print("invalid entries:",invalid_entries)
print("total valid weights=",valid_count)
print("affected items to pli=",affected_items)

