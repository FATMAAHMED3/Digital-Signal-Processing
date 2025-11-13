from TEST_functions import ReadSignalFile
from Task5_ConvolutionTestCase import ConvolutionSamplesAreEqual
def compute_convolution(x_indices, x_samples, h_indices, h_samples):
    x_map = dict(zip(x_indices, x_samples))
    h_map = dict(zip(h_indices, h_samples))
    n_start = x_indices[0] + h_indices[0] 
    n_end = x_indices[-1] + h_indices[-1] 
    Y_samples = []
    Y_indices = []
    for n in range(n_start, n_end + 1):
        y_n = 0
        for m in x_indices:
            x_m = x_map[m]
            h_n_minus_m = h_map.get(n - m, 0.0)
            y_n += x_m * h_n_minus_m
        Y_samples.append(y_n)
        Y_indices.append(n)
    return Y_indices, Y_samples
x_indices, x_samples = ReadSignalFile(r"Task_4_Tests\Convolution testcases\Signal 1.txt")
h_indices, h_samples = ReadSignalFile(r"Task_4_Tests\Convolution testcases\Signal 2.txt")
Y_indices, Y_samples = compute_convolution(
    x_indices, x_samples, 
    h_indices, h_samples)
ConvolutionSamplesAreEqual(Y_indices, Y_samples)