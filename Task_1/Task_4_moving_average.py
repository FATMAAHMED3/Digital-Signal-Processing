import math

import TEST_functions


def moving_avg(window_size, indices, values):
    output_values =[]

    half_window = math.floor(window_size/2)
    last_element = len(values) - half_window -1
    start_index = indices[0] + half_window
    

    for i in range(half_window, last_element +1):
        j = i
        sum = 0
        for j in range(j, j-half_window -1, -1):
            sum += values[j]
        j = i
        for j in range(j+1 , j+ half_window + 1):
            sum += values[j]
        avg = sum/window_size
        
        output_values.append(avg)
    
    trim = half_window*2
    output_indices = indices[:-trim]

    return output_indices,output_values


################### TESTING

input_indices,input_samples = TEST_functions.ReadSignalFile("Task_4_Tests\Moving Average testcases\MovingAvg_input.txt")

output_indices,output_values = moving_avg(3, input_indices, input_samples)
output_indices_t2,output_values_t2 = moving_avg(5, input_indices, input_samples)

print(output_indices_t2)
print(output_values_t2)

def SignalSamplesAreEqual(Your_indices,Your_samples,file_name):
    expected_indices,expected_samples=TEST_functions.ReadSignalFile(file_name)          
    if (len(expected_samples)!=len(Your_samples)) and (len(expected_indices)!=len(Your_indices)):
        print("Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if(Your_indices[i]!=expected_indices[i]):
            print("Test case failed, your signal have different indicies from the expected one") 
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Test case failed, your signal have different values from the expected one") 
            return
    print("Test case passed successfully")

SignalSamplesAreEqual(output_indices,output_values,"Task_4_Tests\Moving Average testcases\MovingAvg_out1.txt")

SignalSamplesAreEqual(output_indices_t2,output_values_t2,"Task_4_Tests\Moving Average testcases\MovingAvg_out2.txt")




        




    
