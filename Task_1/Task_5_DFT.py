import cmath
import math
import Task_1_Test_files.TEST_functions as TEST_functions
import Task_5_Tests.signalcompare as compare_test


def DFT (indices, values,fs):
    N = len(indices)
    index_value_dict = dict(zip(indices, values))
    dft = []
    As= []
    phase_shifts =[]
    omegas = []

    for k in range (N):
        sum =0.0
        for n in range(N):
            sum += (index_value_dict[n]* (cmath.exp(-1j * 2 * cmath.pi*k*n/N)))
        dft.append(sum)
    
    for i in dft:
        real = i.real
        imag = i.imag
        amp = cmath.sqrt(real**2 + imag**2).real
        As.append(amp)
        phase_shifts.append(math.atan2(imag,real))
    
    omega = 2 * cmath.pi * fs /N
    for o in range(1,N+1):
        omegas.append(o*omega)

    return As ,phase_shifts, omegas

################TEST#######################

def float_total_digits(x, total_digits=15):
    digits_before = len(str(int(abs(x))))     
    decimal_digits = max(total_digits - digits_before, 0)
    return round(x, decimal_digits)

def MyReadSignalFile(file_name):
    expected_indices = []
    expected_samples = []
    
    with open(file_name, 'r') as f:
       
        for _ in range(3):
            f.readline()
        
        line = f.readline()
        
        while line:
            L = line.strip().split()

            if len(L) == 2:
               
                v1_str = L[0].rstrip('f')
                v2_str = L[1].rstrip('f')

               
                V1 = float(v1_str)
                V2 = float(v2_str)

                expected_indices.append(V1)
                expected_samples.append(V2)

                line = f.readline()
            else:
                break

    return expected_indices, expected_samples


indices,values = TEST_functions.ReadSignalFile("Task_5_Tests\DFT\input_Signal_DFT.txt")

expected_Amplitudes,expected_phases = MyReadSignalFile("Task_5_Tests\DFT\Output_Signal_DFT_A_Phase.txt")

As ,phase_shifts,o = DFT (indices, values,0)

As = [float_total_digits(x) for x in As]

# print(As)
# print("jjjjjjjjjjj")
# print(expected_Amplitudes)


print(compare_test.SignalComapreAmplitude(As,expected_Amplitudes))

# print(phase_shifts)
# print("jjjjjjjjjjj")
# print(expected_phases)

print(compare_test.SignalComapreAmplitude(phase_shifts,expected_phases))

#########################################IDF####################3


def IDFT(amplitude_list, phase_list):
    X = []
    for amp, rad in zip(amplitude_list, phase_list):
        real = amp * math.cos(rad)
        imag = amp * math.sin(rad)
        X.append(complex(real, imag))

    N = len(X)
    idft = []

    for n in range(N):
        total = 0
        for k in range(N):
            exponent = 1j * 2 * math.pi * k * n / N
            total += X[k] * cmath.exp(exponent)
        idft.append(round(total.real / N))

    return idft

##########Test############

Amps,phas = MyReadSignalFile("Task_5_Tests\IDFT\Input_Signal_IDFT_A_Phase.txt")

values = IDFT(Amps, phas)

print(values)











        


