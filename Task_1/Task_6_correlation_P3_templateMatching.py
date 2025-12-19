
import os
import Task_6_Correlation_P1 as corrP1


#######helper func to read the files#########

def ReadSignalFile_OneColumn(file_name):
    samples = []

    with open(file_name, 'r') as f:
        line = f.readline()   # start from first line

        while line:
            L = line.strip()

            if L != "":       # ignore empty lines
                value = float(L)
                samples.append(value)

            line = f.readline()

    return samples

######### Reading the Tests #############

t1_samples = ReadSignalFile_OneColumn("Task_6_Tests/point3 Files/Test Signals/Test1.txt")
t2_samples = ReadSignalFile_OneColumn("Task_6_Tests/point3 Files/Test Signals/Test2.txt")

# print(t1_samples)

################# Reading the classes #################

folder_path = "Task_6_Tests\point3 Files\Class 1"
C1_values = []   

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    c1_samples = ReadSignalFile_OneColumn(file_path)
    C1_values.append(c1_samples) #2d array each row represents samples in each file, has 5 rows for each files

# print(len(C1_values))
#print(C1_values[0])

folder_path = "Task_6_Tests\point3 Files\Class 2"
C2_values = []   

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    c2_samples = ReadSignalFile_OneColumn(file_path)
    C2_values.append(c2_samples)

################ Func ##############     

def template_matching(signal_samples, C1_values , C2_values): #C1_values w C2_values are 2d arrays
    test_indices = list(range(len(signal_samples)))
    C1_maxes =[]
    C2_maxes =[]

    for i in range(len(C1_values)):
        C1_sample_indices = list(range(len(C1_values[i])))
        Y_indices, Y_samples = corrP1.compute_r12(test_indices,signal_samples,C1_sample_indices,C1_values[i])
        P = corrP1.compute_p12(Y_samples, signal_samples, C1_values[i])
        max_corr = max(P)
        C1_maxes.append(max_corr)

    for i in range(len(C2_values)):
        C2_sample_indices = list(range(len(C2_values[i])))
        Y_indices, Y_samples = corrP1.compute_r12(test_indices,signal_samples,C2_sample_indices,C2_values[i])
        P = corrP1.compute_p12(Y_samples, signal_samples, C2_values[i])
        max_corr = max(P)
        C2_maxes.append(max_corr)
    
    C1_avg = sum(C1_maxes) / len(C1_maxes)
    C2_avg = sum(C2_maxes) / len(C2_maxes)

    print("C1 Average " , C1_avg)
    print("C2 Average " , C2_avg)

    if C1_avg >= C2_avg:
        return "Class 1"
    else:
        return "Class 2"



print("Test 1: " , template_matching(t1_samples, C1_values , C2_values))
print("Test 2: " ,template_matching(t2_samples, C1_values , C2_values))


