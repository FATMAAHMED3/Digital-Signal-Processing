from Task_1_Test_files.TEST_functions import ReadSignalFile
from Task5_Convolution import compute_convolution
from Filters_Tests.CompareSignal import Compare_Signals


import numpy as np
import math ,cmath


def choose_window(As):
    if As <= 21:
        return "rectangular"
    elif As <= 44:
        return "hanning"
    elif As <= 53:
        return "hamming"
    else:
        return "blackman"
    
def make_N_odd(N):
    N = math.ceil(N)
    if N % 2 ==0:
        N= N+1
    return N


def window_function(wtype, normalized_transition_band):
    window = {}

    if wtype == "rectangular":
        N = 0.9/normalized_transition_band
        N = make_N_odd(N)
        start_index = int(((N-1)/2)*-1)
        end_index = int(((N-1)/2))
        for i in range(start_index, end_index +1):
            window[i] = 1

    elif wtype == "hanning":
        N = 3.1/normalized_transition_band
        N = make_N_odd(N)
        start_index = int(((N-1)/2)*-1)
        end_index = int(((N-1)/2))
        for i in range(start_index, end_index +1):
            window[i] = 0.5 + 0.5*math.cos((2*math.pi*i)/N)

    elif wtype == "hamming":
        N = 3.3/normalized_transition_band
        N = make_N_odd(N)
        start_index = int(((N-1)/2)*-1)
        end_index = int(((N-1)/2))
        for i in range(start_index, end_index +1):
            window[i] = 0.54 + 0.46*math.cos((2*math.pi*i)/N)

    elif wtype == "blackman": 
        N = 5.5/normalized_transition_band
        N = make_N_odd(N)
        start_index = int(((N-1)/2)*-1)
        end_index = int(((N-1)/2))
        for i in range(start_index, end_index +1):
            window[i] = 0.42 + 0.5*math.cos((2*math.pi*i)/(N-1)) + 0.08*math.cos((4*math.pi*i)/(N-1))
    
    return window , start_index , end_index

def low_pass(fc ,start_index , end_index , normalized_transition_band ): 
    half_N = normalized_transition_band/2
    new_fc = fc + half_N
    low_pass_values = {}
    for i in range(start_index, end_index +1):
        if i == 0:
            low_pass_values[i] = 2*new_fc
        else:
            low_pass_values[i] =  (2 * new_fc * math.sin(i * 2 * math.pi * new_fc)) / (i * 2 * math.pi * new_fc)

    return low_pass_values

def high_pass(fc ,start_index , end_index , normalized_transition_band ): 
    half_N = normalized_transition_band/2
    new_fc = fc - half_N
    high_pass_values = {}
    for i in range(start_index, end_index +1):
        if i == 0:
            high_pass_values[i] = 1 - (2*new_fc)
        else:
            high_pass_values[i] =  (-2 * new_fc * math.sin(i * 2 * math.pi * new_fc)) / (i * 2 * math.pi * new_fc)

    return high_pass_values

def band_pass(f1, f2, start_index, end_index, normalized_transition_band):
    half_N = normalized_transition_band / 2
    new_f1 = f1 - half_N
    new_f2 = f2 + half_N

    band_pass_values = {}

    for i in range(start_index, end_index + 1):
        if i == 0:
            band_pass_values[i] = 2 * (new_f2 - new_f1)
        else:
            term1 = (2 * new_f2 * math.sin(i * 2 * math.pi * new_f2)) / (i * 2 * math.pi * new_f2)
            term2 = (2 * new_f1 * math.sin(i * 2 * math.pi * new_f1)) / (i * 2 * math.pi * new_f1)
            band_pass_values[i] = term1 - term2

    return band_pass_values

def band_stop(f1, f2, start_index, end_index, normalized_transition_band):
    half_N = normalized_transition_band / 2
    new_f1 = f1 + half_N
    new_f2 = f2 - half_N

    band_stop_values = {}

    for i in range(start_index, end_index + 1):
        if i == 0:
            band_stop_values[i] = 1 - 2 * (new_f2 - new_f1)
        else:
            term1 = (2 * new_f1 * math.sin(i * 2 * math.pi * new_f1)) / (i * 2 * math.pi * new_f1)
            term2 = (2 * new_f2 * math.sin(i * 2 * math.pi * new_f2)) / (i * 2 * math.pi * new_f2)
            band_stop_values[i] = term1 - term2

    return band_stop_values




def make_filter(filter_type, fs, stop_band_attenuation , transition_band , fc1,fc2 = None):
    window_type = choose_window(stop_band_attenuation)
    normalized_transition_band = transition_band/fs

    window, start_index , end_index= window_function(window_type, normalized_transition_band)

    if filter_type == "low":
        h = low_pass(fc1/fs ,start_index , end_index , normalized_transition_band )
    elif filter_type == "high":
        h = high_pass(fc1/fs, start_index, end_index, normalized_transition_band)
    elif filter_type == "bandpass":
        h = band_pass(fc1/fs, fc2/fs, start_index, end_index, normalized_transition_band)
    elif filter_type == "bandstop":
        h = band_stop(fc1/fs, fc2/fs, start_index, end_index, normalized_transition_band)
    else:
        raise ValueError("Invalid filter type")
    
    h_windowed = {}
    for i in h:
        h_windowed[i] = h[i] * window[i]

    return h_windowed


##################
def DFT (indices, values):
    N = len(values)

    dft = []
    for k in range (N):
        sum =0.0
        for n in range(N):
            sum += (values[n]* (cmath.exp(-1j * 2 * cmath.pi*k*n/N)))
        sum_rounded = complex(round(sum.real, 2), round(sum.imag, 2))
        dft.append(sum)
    return dft


def IDFT(dft):

    N = len(dft)
    idft = []

    for n in range(N):
        total = 0
        for k in range(N):
            exponent = 1j * 2 * math.pi * k * n / N
            total += dft[k] * cmath.exp(exponent)
        idft.append(total.real / N)

    return idft

def zero_pad_dict(d,N_min,N_max):
    return {n: d.get(n,0) for n in range(N_min,N_max+1)}

def rotate_left(arr, k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]


def fast_method(indices, values,filter_indices, filter_values):

    index_value_dict = dict(zip(indices, values))
    filter_index_value_dict = dict(zip(filter_indices, filter_values))

    start_index = int(min(indices[0],filter_indices[0]))
    end_index = int(indices[-1] + filter_indices[-1])

    index_value_dict = zero_pad_dict(index_value_dict,start_index,end_index)
    filter_index_value_dict = zero_pad_dict(filter_index_value_dict,start_index,end_index)


    signal_dft = DFT (list(index_value_dict.keys()), list(index_value_dict.values()))
    filter_dft = DFT (list(filter_index_value_dict.keys()), list(filter_index_value_dict.values()))

    # print("dft of signal", signal_dft)
    # print("dft of filter", filter_dft)
     
    mult = []
    for i in range(len(filter_dft)):
        mult.append(filter_dft[i] * signal_dft[i])

    # print(mult)
    

    result = IDFT(mult)

    result = rotate_left(result, start_index*-1)

    return result






# print(make_filter("low", 8000,50 , 500 , 1500,fc2 = None))

#################Testing#########################


##Test 1
print("\nTest 1 (low pass)")
h_dict = make_filter("low", 8000, 50, 500, 1500)
Compare_Signals("Filters_Tests\FIR test cases\Testcase 1\LPFCoefficients.txt",list(h_dict.keys()), list(h_dict.values()))



##Test 2
print("\nTest 2 (low pass) using convolution")

x_indices, x_samples = ReadSignalFile('Filters_Tests\FIR test cases\Testcase 2\ecg400.txt')

h_indices = sorted(h_dict.keys())
h_samples = [h_dict[i] for i in h_indices]
y_indices, y_samples = compute_convolution(x_indices, x_samples, h_indices, h_samples)

Compare_Signals("Filters_Tests\FIR test cases\Testcase 2\ecg_low_pass_filtered.txt",y_indices, y_samples)

y_samples_fast = fast_method(x_indices, x_samples, h_indices, h_samples)
# print(y_samples_fast)
# print(len(y_indices_fast))
# print(len(y_indices))
# print(len(h_indices))
print("Test 2 (low pass) using fourir")
Compare_Signals("Filters_Tests\FIR test cases\Testcase 2\ecg_low_pass_filtered.txt",y_indices,y_samples_fast )

##Test 3
print("\nTest 3 (high pass)")
h_dict_highPass = make_filter("high", 8000, 70, 500, 1500)
Compare_Signals("Filters_Tests\FIR test cases\Testcase 3\HPFCoefficients.txt",list(h_dict_highPass.keys()), list(h_dict_highPass.values()))

##Test 4
print("\nTest 4 (high pass) using convolution")
x_indices, x_samples = ReadSignalFile('Filters_Tests\FIR test cases\Testcase 4\ecg400.txt')

h_indices = sorted(h_dict_highPass.keys())
h_samples = [h_dict_highPass[i] for i in h_indices]
y_indices, y_samples = compute_convolution(x_indices, x_samples, h_indices, h_samples)

Compare_Signals("Filters_Tests\FIR test cases\Testcase 4\ecg_high_pass_filtered.txt",y_indices, y_samples)

print("\nTest 4 (high pass) using fourir")
y_samples_fast = fast_method(x_indices, x_samples, h_indices, h_samples)

Compare_Signals("Filters_Tests\FIR test cases\Testcase 4\ecg_high_pass_filtered.txt",y_indices,y_samples_fast )

##Test 5
print("\nTest 5 (band pass)")
h_dict_bandPass = make_filter("bandpass", 1000, 60, 50, 150,250)
Compare_Signals("Filters_Tests\FIR test cases\Testcase 5\BPFCoefficients.txt",list(h_dict_bandPass.keys()), list(h_dict_bandPass.values()))

##Test 6
print("\nTest 6 (band pass) using convolution")
x_indices, x_samples = ReadSignalFile('Filters_Tests\FIR test cases\Testcase 6\ecg400.txt')

y_indices, y_samples = compute_convolution(x_indices, x_samples,list(h_dict_bandPass.keys()), list(h_dict_bandPass.values()))

Compare_Signals("Filters_Tests\FIR test cases\Testcase 6\ecg_band_pass_filtered.txt",y_indices, y_samples)

print("\nTest 6 (band pass) using fourir")
y_samples_fast = fast_method(x_indices, x_samples,list(h_dict_bandPass.keys()), list(h_dict_bandPass.values()))

Compare_Signals("Filters_Tests\FIR test cases\Testcase 6\ecg_band_pass_filtered.txt",y_indices,y_samples_fast )

##Test 7
print("\nTest 7 (band stop)")
h_dict_bandstop = make_filter("bandstop", 1000, 60, 50, 150,250)
Compare_Signals("Filters_Tests\FIR test cases\Testcase 7\BSFCoefficients.txt",list(h_dict_bandstop.keys()), list(h_dict_bandstop.values()))

##Test 8
print("\nTest 8 (band stop) using convolution")
x_indices, x_samples = ReadSignalFile('Filters_Tests\FIR test cases\Testcase 8\ecg400.txt')

y_indices, y_samples = compute_convolution(x_indices, x_samples,list(h_dict_bandstop.keys()), list(h_dict_bandstop.values()))

Compare_Signals("Filters_Tests\FIR test cases\Testcase 8\ecg_band_stop_filtered.txt",y_indices, y_samples)

print("\nTest 8 (band stop) using fourir")
y_samples_fast = fast_method(x_indices, x_samples,list(h_dict_bandstop.keys()), list(h_dict_bandstop.values()))

Compare_Signals("Filters_Tests\FIR test cases\Testcase 8\ecg_band_stop_filtered.txt",y_indices,y_samples_fast )

