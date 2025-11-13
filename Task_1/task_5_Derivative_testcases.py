
from TEST_functions import ReadSignalFile
def FirstDerivativeSamplesAreEqual(Your_indices, Your_samples):
    
    file_name = r"Task_4_Tests\Derivative testcases\1st_derivative_out.txt"
    expected_indices, expected_samples = ReadSignalFile(file_name)
    if (len(expected_samples) != len(Your_samples)) or (len(expected_indices) != len(Your_indices)):
        print("First Derivative Test case failed, your signal has a different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if(Your_indices[i] != expected_indices[i]):
            print("First Derivative Test case failed, your signal has different indices from the expected one") 
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("First Derivative Test case failed, your signal has different values from the expected one") 
            return
    print("First Derivative Test case passed successfully")
def SecondDerivativeSamplesAreEqual(Your_indices, Your_samples):
    file_name = r"Task_4_Tests\Derivative testcases\2nd_derivative_out.txt" 
    expected_indices, expected_samples = ReadSignalFile(file_name)
    if (len(expected_samples) != len(Your_samples)) or (len(expected_indices) != len(Your_indices)):
        print("Second Derivative Test case failed, your signal has a different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if(Your_indices[i] != expected_indices[i]):
            print("Second Derivative Test case failed, your signal has different indices from the expected one") 
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Second Derivative Test case failed, your signal has different values from the expected one") 
            return
    print("Second Derivative Test case passed successfully")