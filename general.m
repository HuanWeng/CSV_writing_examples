clear; clc;

% Generate random 3x4 matrix of floats y, 3x1 vector of ints d
y = rand(3, 4);
d = randi([-100, 100], 3, 1);

% Open a file for output
% Overwrite
f = fopen('output.csv', 'w');
% Append
%f = fopen('output.csv', 'a');

% For loop running 3 times to print each csv row
for i = 1: length(d)
    fprintf(f, ' %9.5f, %9.5f, %9.5f, %9.5f, %d\n', y(i, :), d(i));
end

% Close file
fclose(f);