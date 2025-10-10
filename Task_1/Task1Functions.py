

#!!!!!!!!!!!!!!!!!!!!!Addition (3)!!!!!!!!!!!!!!!!!!!

#indices and values are 2d array each row is a seperare signal with its indices/values

def add_signals(num_signals, indices, values): 
    output_indices=[]
    output_samples=[]
    start_index = get_start_index(indices)
    end_index = get_end_index(indices)

    for idx in range(start_index, end_index + 1):
        total = 0
        for s in range(num_signals): #loop through all signals
            if idx in indices[s]:
                pos = indices[s].index(idx) #the index index in the list to get corresponding value
                total += values[s][pos]
        output_indices.append(idx)
        output_samples.append(total)

    return output_indices, output_samples



def get_start_index(indices_list):
    smallest=indices_list[0][0]
    for signal in indices_list:
        if(signal[0]<smallest):
            smallest= signal[0]  
    return smallest

def get_end_index(indices_list):
    largest=indices_list[0][-1]
    for signal in indices_list:
        if(signal[-1]>largest):
            largest= signal[-1]  
    return largest

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!multiplication(4)!!!!!!!!!!!!!!!!!!!!!!

def mul_signal_by_constant(constant, indices, values): 
    output_samples=[]
    for value in values:
        output_samples.append(value*constant)
    return indices,output_samples

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!subtraction(5)!!!!!!!!!!!!!!!!!!!!!!

def sub_signals(indices_s1 ,values_s1 ,indices_s2 ,values_s2):
    indices_s2, values_s2 = mul_signal_by_constant(-1,indices_s2,values_s2)
    output_indices, output_samples = add_signals(2, [indices_s1,indices_s2], [values_s1,values_s2])
    return output_indices, output_samples

#!!!!!!!!!!!!!!!!!!!!!Shifting(6)!!!!!!!!!!!!!!!!!!!

def MyShiftSignal(indices, samples, k):
    shifted_samples = samples.copy()
    shifted_indices =[]
    for i in indices:
        shifted_indices.append(i-k)
    return shifted_indices, shifted_samples
    
#!!!!!!!!!!!!!!!!!!!!!Folding(7)!!!!!!!!!!!!!!!!!!!

def myfolding(indices, samples):
    fsamples = samples.copy()
    findices =[]
    for i in indices:
        findices.append(-i)
    findices.reverse()
    fsamples.reverse()
    return findices, fsamples




