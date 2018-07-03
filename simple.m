clear; clc;

% Generate random 3x4 matrix of floats y, 3x1 vector of ints d
y = rand(3, 4);
d = randi([-100, 100], 3, 1);

% Set number precision
y = round(y, 5);

% Overwrite csv file
csvwrite('output.csv', [y, d]);