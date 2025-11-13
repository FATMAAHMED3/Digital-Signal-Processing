from TEST_functions import ReadSignalFile
def ConvolutionSamplesAreEqual(Your_indices, Your_samples):
    file_name = r"Task_4_Tests\Convolution testcases\Conv_output.txt" 
    expected_indices, expected_samples = ReadSignalFile(file_name)
    if (len(expected_samples) != len(Your_samples)) or (len(expected_indices) != len(Your_indices)):
        print("Convolution Test case failed, your signal has a different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if(Your_indices[i] != expected_indices[i]):
            print("Convolution Test case failed, your signal has different indices from the expected one") 
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Convolution Test case failed, your signal has different values from the expected one") 
            return
    print("Convolution Test case passed successfully")