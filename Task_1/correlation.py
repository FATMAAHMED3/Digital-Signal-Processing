def Compare_Signals(file_name,Your_indices,Your_samples):      
    expected_indices=[]
    expected_samples=[]
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L=line.strip()
            if len(L.split(' '))==2:
                L=line.split(' ')
                V1=int(L[0])
                V2=float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break
    print("Current Output Test file is: ")
    print(file_name)
    print("\n")
    if (len(expected_samples)!=len(Your_samples)) and (len(expected_indices)!=len(Your_indices)):
        print("Shift_Fold_Signal Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if(Your_indices[i]!=expected_indices[i]):
            print("Shift_Fold_Signal Test case failed, your signal have different indicies from the expected one") 
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Correlation Test case failed, your signal have different values from the expected one") 
            return
    print("Correlation Test case passed successfully")

def ReadSignalFile(file_name):
    expected_indices=[]
    expected_samples=[]
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L=line.strip()
            if len(L.split(' '))==2:
                L=line.split(' ')
                V1=int(L[0])
                V2=float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break
    return expected_indices,expected_samples


import numpy as np
def compute_r12(x_indices, x_samples, h_indices, h_samples):
    x_map = dict(zip(x_indices, x_samples))
    h_map = dict(zip(h_indices, h_samples))
    Y_samples = []
    Y_indices = x_indices  # output indices
    for n in x_indices:
        y_n = 0.0
        for m in x_indices:
            x_m = x_map[m]
            h_val = h_map[(n + m) % len(h_indices)]  # direct correlation assumes second signal is periodic
            y_n += x_m * h_val
        y_n /= len(x_indices)  
        Y_samples.append(y_n)
        
    return Y_indices, Y_samples


def compute_p12(R, x_samples, h_samples):
    N = len(x_samples)
    sum_x2 = np.sum(np.square(x_samples)) 
    sum_h2 = np.sum(np.square(h_samples))  
    denominator = np.sqrt(sum_x2 * sum_h2) * (1/N)
    P = []

    for n in (R):
        p_n = n/denominator
        P.append(p_n)

    return P

x_indices, x_samples = ReadSignalFile(r"Correlation Task_Tests\Point1 Correlation\Corr_input signal1.txt")
h_indices, h_samples = ReadSignalFile(r"Correlation Task_Tests\Point1 Correlation\Corr_input signal2.txt")

Y_indices, R = compute_r12(x_indices, x_samples, h_indices, h_samples)

print ("result before normalization" , R)
P = compute_p12(R, x_samples, h_samples)


indices = Y_indices


print("Indices:", indices)
print("R12:", R)
print("P12:", P)

print("Length of your output:", len(P))
for idx, val in zip(indices, P):
    print(f"Index: {idx}, Value: {val:.8f}")


Compare_Signals(r"Correlation Task_Tests\Point1 Correlation\CorrOutput.txt", indices, P)
