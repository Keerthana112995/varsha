set1={1,2,3}
set2={3,4,5}
diff=set1.difference(set2)
print(diff)

diff=set2.difference(set1)
print(diff)

set1.update(set2)
print(set1)

set1.update({7})