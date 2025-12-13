import Task_1_Test_files.TEST_functions as TEST_functions
import Task_1

indices_s1, samples_s1= TEST_functions.ReadSignalFile("Task_1_Test_files\Signal1.txt")
indices_s2, samples_s2= TEST_functions.ReadSignalFile("Task_1_Test_files\Signal2.txt")

#!!!!!!!!!!!!!!!!!!!!!Addition Test (3)!!!!!!!!!!!!!!!!!!!

add_output_indices, add_output_samples = Task_1.add_signals(2, [indices_s1,indices_s2], [samples_s1,samples_s2])

TEST_functions.AddSignalSamplesAreEqual('Signal1.txt','Signal2.txt',add_output_indices, add_output_samples)

#!!!!!!!!!!!!!!!!!!!!!Multipication Test (4)!!!!!!!!!!!!!!!!!!!

mul_output_indices, mul_output_samples = Task_1.mul_signal_by_constant(5,indices_s1, samples_s1)

TEST_functions.MultiplySignalByConst(5,mul_output_indices, mul_output_samples)# call this function with your computed indicies and samples

#!!!!!!!!!!!!!!!!!!!!!Subtraction Test (5)!!!!!!!!!!!!!!!!!!!

sub_output_indices, sub_output_samples = Task_1.sub_signals(indices_s1 ,samples_s1 ,indices_s2 ,samples_s2)

TEST_functions.SubSignalSamplesAreEqual("Signal1.txt", "Signal2.txt",sub_output_indices,sub_output_samples)

#!!!!!!!!!!!!!!!!!!!!!Shifting Test (6)!!!!!!!!!!!!!!!!!!!

my_indices_shift, my_samples_shift = Task_1.MyShiftSignal(indices_s1 ,samples_s1 , 3) 
TEST_functions.ShiftSignalByConst(3,my_indices_shift, my_samples_shift)

#!!!!!!!!!!!!!!!!!!!!!Folding Test (7)!!!!!!!!!!!!!!!!!!!

my_indices_fold, my_samples_fold = Task_1.myfolding(indices_s1 ,samples_s1) 
TEST_functions.Folding(my_indices_fold, my_samples_fold)  # call this function with your computed indicies and samples

print("len(indices) =", len(my_indices_shift))
print("len(samples) =", len(my_samples_shift))