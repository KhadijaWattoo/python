import array
y = array.array('i',[15,7,10,1,3])
 
for x in y:
     if x <  y[0] :
      y[0]=x
print("the smallest number", y[0])
