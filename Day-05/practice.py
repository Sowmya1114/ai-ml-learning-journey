#marks dictionary
marks={"Maths":90,
       "Physics":80,
       "Chemistry":85}
#print all subjects with marks
for keys,values in marks.items():
  print(keys, ":", values)
#total marks
total=0
for score in marks.values():
  total+=score
print(total)
