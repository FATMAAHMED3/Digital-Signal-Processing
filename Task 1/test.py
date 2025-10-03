import TEST_functions
import Task1Functions

indices_s1, samples_s1= TEST_functions.ReadSignalFile("Signal1.txt")
indices_s2, samples_s2= TEST_functions.ReadSignalFile("Signal2.txt")

#!!!!!!!!!!!!!!!!!!!!!Addition Test (3)!!!!!!!!!!!!!!!!!!!

add_output_indices, add_output_samples = Task1Functions.add_signals(2, [indices_s1,indices_s2], [samples_s1,samples_s2])

TEST_functions.AddSignalSamplesAreEqual('Signal1.txt','Signal2.txt',add_output_indices, add_output_samples)

#!!!!!!!!!!!!!!!!!!!!!Multipication Test (4)!!!!!!!!!!!!!!!!!!!

mul_output_indices, mul_output_samples = Task1Functions.mul_signal_by_constant(5,indices_s1, samples_s1)

TEST_functions.MultiplySignalByConst(5,mul_output_indices, mul_output_samples)# call this function with your computed indicies and samples

#!!!!!!!!!!!!!!!!!!!!!Subtraction Test (5)!!!!!!!!!!!!!!!!!!!

sub_output_indices, sub_output_samples = Task1Functions.sub_signals(indices_s1 ,samples_s1 ,indices_s2 ,samples_s2)

TEST_functions.SubSignalSamplesAreEqual("Signal1.txt", "Signal2.txt",sub_output_indices,sub_output_samples)

#!!!!!!!!!!!!!!!!!!!!!Shifting Test (6)!!!!!!!!!!!!!!!!!!!

my_indices_shift, my_samples_shift = Task1Functions.MyShiftSignal(indices_s1 ,samples_s1 , 3) 
TEST_functions.ShiftSignalByConst(3,my_indices_shift, my_samples_shift)

#!!!!!!!!!!!!!!!!!!!!!Folding Test (7)!!!!!!!!!!!!!!!!!!!

my_indices_fold, my_samples_fold = Task1Functions.myfolding(indices_s1 ,samples_s1) 
TEST_functions.Folding(my_indices_fold, my_samples_fold)  # call this function with your computed indicies and samples

print("len(indices) =", len(my_indices_shift))
print("len(samples) =", len(my_samples_shift))