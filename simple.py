import numpy as np

# Generate random 3x4 matrix of floats y, 3x1 vector of ints d
y = np.random.rand(3, 4)
d = np.random.randint(-100, 100, 3)

# Set number precision
y = np.round(y, 5)

# Overwrite csv file
np.savetxt("output.csv", np.asarray(np.c_[y, d]), delimiter = ",") 

