import numpy as np
a=np.array([0,1,2,3,4,5,6,7,8])
b=np.matrix([0,1,2,3,4,5,6,7,8])
b=b.reshape(3,3)
print(b)
element_mean=a.mean()
element_var=a.var()
element_max=float(a.max())
element_min=float(a.min())
element_sum=float(a.sum())
element_std=float(a.std())
row_mean=[]
row_var=[]
row_max=[]
row_min=[]
row_sum=[]
row_std=[]
for i in range(3):
   row_mean.append(float(b[i].mean()))
   row_var.append(float(b[i].var()))
   row_max.append(float(b[i].max()))
   row_min.append(float(b[i].min())) 
   row_sum.append(float(b[i].sum())) 
   row_std.append(float(b[i].std()))
col_mean=[]
col_var=[]
col_max=[]
col_min=[]
col_sum=[]
col_std=[]
for i in range(3):
   col_mean.append(float(b[:,i].mean()))
   col_var.append(float(b[:,i].var()))
   col_max.append(float(b[:,i].max()))
   col_min.append(float(b[:,i].min()))
   col_sum.append(float(b[:,i].sum()))
   col_std.append(float(b[:,i].std()))
mean=[]
mean.append(col_mean)
mean.append(row_mean)
mean.append(float(element_mean))
var=[]
var.append(col_var)
var.append(row_var)
var.append(float(element_var))
max=[]
max.append(col_max)
max.append(row_max)
max.append(element_max)
min=[]
min.append(col_min)
min.append(row_min)
min.append(element_min)
sum=[]
sum.append(col_sum)
sum.append(row_sum)
sum.append(element_sum)
std=[]
std.append(col_std)
std.append(row_std)
std.append(element_std)

if len(a) < 9:
    raise ValueError("List must contain at least 9 elements.")
else:
 result={
    'mean':mean,
    'variance':var,
  'standard deviation':std,
  'max': max,
  'min': min,
  'sum': sum
 }
print(result)


