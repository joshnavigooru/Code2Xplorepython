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
