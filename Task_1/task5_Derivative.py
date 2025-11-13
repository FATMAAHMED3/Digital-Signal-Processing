
from TEST_functions import ReadSignalFile
from task_5_Derivative_testcases import FirstDerivativeSamplesAreEqual,SecondDerivativeSamplesAreEqual
def compute_first_derivative(input_samples):
    x = input_samples
    
    Y_samples = []
    Y_indices = []
    for i in range(1, len(x)):
        y_val = x[i] - x[i-1]
        Y_samples.append(y_val)
        Y_indices.append(i - 1) 
    return Y_indices, Y_samples
def compute_second_derivative(input_samples):
    x = input_samples
    Y_samples = []
    Y_indices = []
    for i in range(1, len(x) - 1):
  
        y_val = x[i+1] - 2 * x[i] + x[i-1]
        Y_samples.append(y_val)
        Y_indices.append(i - 1)
        
    return Y_indices, Y_samples
input_file = r"Task_4_Tests\Derivative testcases\Derivative_input.txt"
input_indices, input_samples = ReadSignalFile(input_file)
Y1_indices, Y1_samples = compute_first_derivative( input_samples)
FirstDerivativeSamplesAreEqual(Y1_indices, Y1_samples)
Y2_indices, Y2_samples = compute_second_derivative( input_samples)
SecondDerivativeSamplesAreEqual(Y2_indices, Y2_samples)