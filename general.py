import numpy as np

# Generate random 3x4 matrix of floats y, 3x1 vector of ints d
y = np.random.rand(3, 4)
d = np.random.randint(-100, 100, 3)

# Open a file for output
# Overwrite
f = open("output.csv", "w") 
# Append
#f = open("output.csv", "a")

# For loop running 3 times to print each csv row
for i in range(len(d)):
    output = " %9.5f, %9.5f, %9.5f, %9.5f, %d\n" % (y[i,0], y[i,1], y[i,2], y[i,3], d[i])
    f.write(output)
    
# close file
f.close()
