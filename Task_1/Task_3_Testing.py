import TEST_functions
import Task_3_Tests.Test_1.QuanTest1 as test1
import Task_3_Tests.Test_2.QuanTest2 as test2
import Task_3

indices, cont_values = TEST_functions.ReadSignalFile("Task_3_Tests/Test_1/Quan1_input.txt")


encoded_values , quantized_values , interval_indices , error = Task_3.quantize_signal(cont_values,num_levels=8)

print (encoded_values)
print(quantized_values)

test1.QuantizationTest1("Task_3_Tests/Test_1/Quan1_Out.txt",encoded_values , quantized_values)

#Test 2

indices, cont_values = TEST_functions.ReadSignalFile("Task_3_Tests/Test_2/Quan2_input.txt")

encoded_values , quantized_values , interval_indices , error = Task_3.quantize_signal(cont_values,num_levels=4)

print(interval_indices)
test2.QuantizationTest2("Task_3_Tests/Test_2/Quan2_Out.txt",interval_indices,encoded_values,quantized_values,error)