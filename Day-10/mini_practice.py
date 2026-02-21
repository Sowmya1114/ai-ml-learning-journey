import numpy as np
# dataset (marks)
marks = np.array([35, 78, 90, 56, 42, 88, 30])
# pass marks >= 40
passed = marks[marks >= 40]
failed = marks[marks < 40]
print("Passed:", passed)
print("Failed:", failed)
print("Pass percentage:", (len(passed)/len(marks))*100)
