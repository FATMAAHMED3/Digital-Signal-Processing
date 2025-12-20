import Task_1_test
import Task_1
import Task_2
import Task_1_Test_files.TEST_functions as TEST_functions
import Task_3
import Task_4_moving_average
import task5_Derivative
import Task5_Convolution
import Task_5_DFT
import Task_6_Correlation_P1
import Filters
from Task5_Convolution import compute_convolution



import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu


def creat_plot(x_Label,y_label,x,y,Label="none",title ="none", y_Ticks = "none",y_tick_labels = "none"):
    fig, ax = plt.subplots()

    if Label=="none":
        ax.plot(x, y,marker='o', linestyle='-', markersize=6)
    else:
        ax.plot(x, y, label=Label,marker='o', linestyle='-', markersize=6)

    if y_Ticks !="none":
        ax.set_yticks(y_Ticks)
    
    if y_tick_labels !="none":
        ax.set_yticklabels(y_tick_labels)

    ax.set_xlabel(x_Label)
    ax.set_ylabel(y_label)
    if title != "none":
        ax.set_title(title)
    ax.legend()
    return fig


with st.sidebar:
    selected = option_menu(
        menu_title="Choose Task",
        options=["Task 1","Task 2","Task 3","Task 4","Task 5","Task 6","Task 7"],
    )

if selected == "Task 1":
    st.title("Task 1")
    # Data
    x_s1 = Task_1_test.indices_s1
    y_s1 = Task_1_test.samples_s1

    st.pyplot(creat_plot("Indices","Values",x_s1,y_s1,Label="Signal 1"))

    # Data
    x_s2 = Task_1_test.indices_s2
    y_s2 = Task_1_test.samples_s2


    # Show in Streamlit
    st.pyplot(creat_plot("Indices","Values",x_s2,y_s2,Label="Signal 2"))

    options = ["Add", "Multiply", "Subtract", "Delay/Advance", "Folding/reversing"]

    choice = st.selectbox("Choose operation:", options)

    st.write("You selected:", choice)

    if choice == "Add":

        st.pyplot(creat_plot("Indices","Values",Task_1_test.add_output_indices, Task_1_test.add_output_samples,title="Signal 1 + Signal 2"))

    elif choice == "Subtract":

        st.pyplot(creat_plot("Indices","Values",Task_1_test.sub_output_indices, Task_1_test.sub_output_samples,title="Signal 1 - Signal 2"))

    elif choice == "Multiply":

        st.pyplot(creat_plot("Indices","Values",Task_1_test.mul_output_indices, Task_1_test.mul_output_samples,title="Signal 1 *5 "))

    elif choice == "Delay/Advance":

        st.pyplot(creat_plot("Indices","Values",Task_1_test.my_indices_shift, Task_1_test.my_samples_shift,title="Signal 1 advanced by 3 "))

    elif choice == "Folding/reversing":
        options = ["Signal 1", "Signal 2"]
        choice = st.selectbox("Choose Signal:", options)

        if choice == "Signal 1":

            st.pyplot(creat_plot("Indices","Values",Task_1_test.my_indices_fold, Task_1_test.my_samples_fold,title="Signal 1 after folding"))
        else:
            x_f, y_f = Task_1.myfolding(Task_1_test.indices_s2,Task_1_test.samples_s2)
            st.pyplot(creat_plot("Indices","Values",x_f, y_f,title="Signal 2 after folding"))


elif selected == "Task 2":
    st.title("Task 2")
    signal_type = st.selectbox("Signal Generation:", ["Sin", "Cos"])
    # representation = st.selectbox("Representation:", ["Continuous", "Discrete"])
    A = st.number_input("Enter Amplitude: ")
    phase_degree = st.number_input("Enter Phase Shift in degrees: ")
    analog_freq = st.number_input("Enter Analog Frequency: ")
    fs = None
    # representation == "Discrete"
    fs = st.number_input("Enter Sampling Frequency: ")
    duration = st.number_input("Enter Duration:", value=1.0)
    x, y = Task_2.generate_signal(signal_type, "continuous", A, phase_degree, analog_freq, fs, duration)

    z, n = Task_2.generate_signal(signal_type, "discrete", A, phase_degree, analog_freq, fs, duration)

   
    st.pyplot(creat_plot("Time","Value",x,y))
    st.pyplot(creat_plot("Time","Value",z,n))

    print (x)

elif selected == "Task 3":
    st.title("Task 3")
    choice = st.radio(
    "Choose one to input:",
    ["Number of Levels", "Number of bits available"])




    if choice == "Number of Levels":
        inp = st.number_input("Enter Number of Levels: " ,value=2)
        c="L"
        num_Levels = int(inp)
    elif choice == "Number of bits available":
        inp = st.number_input("Enter Number of bits available: ")
        c="B"
        num_Levels = int(pow(2,inp))

    inp = int(inp)
    options = ["Test 1", "Test 2"]

    T_choice = st.selectbox("Choose Signal to quantize:", options)

    if T_choice == "Test 1":
        i,v = TEST_functions.ReadSignalFile("Task_3_Tests/Test_1/Quan1_input.txt")
    else:
        i,v = TEST_functions.ReadSignalFile("Task_3_Tests/Test_2/Quan2_input.txt")
    
    if c == "L":
        encoded_values , quantized_values , interval_indices , error = Task_3.quantize_signal(v,num_levels=inp)
    else:
        encoded_values , quantized_values , interval_indices , error = Task_3.quantize_signal(v, num_bits=inp)

    y_t = range(1,num_Levels+1)

    y_t_labels = range(0,num_Levels)

    num = num_Levels-1
    bits = num.bit_length()  # minimum bits needed
    binary_values = [format(x, f'0{bits}b') for x in y_t_labels]

    
    total = 0
    for e in error:
        total += pow(e,2)
    
    print("Interval indices ", interval_indices)
    avg_power_error = total/len(error)


    st.pyplot(creat_plot("Samples","Encoded Values",i,interval_indices,Label="none",title =f"Signal after Quantization with {num_Levels} levels",y_Ticks=y_t,y_tick_labels=binary_values))

    st.write("Average error power = " ,avg_power_error)

    st.pyplot(creat_plot("Samples","Values",i,v,title ="Signal before quantization"))
    
elif selected == "Task 4":
    st.title("Task 4")
    with st.expander("Moving Average"):
        i,v = TEST_functions.ReadSignalFile("Task_4_Tests\Moving Average testcases\MovingAvg_input.txt")
        st.pyplot(creat_plot("Indices","Values",i,v,title ="Signal Before Averaging"))
        W_S = st.number_input("Enter Window Size: ", value=3,step=1)
        output_indices,output_values = Task_4_moving_average.moving_avg(W_S,i,v)
        st.pyplot(creat_plot("Indices","Values",output_indices,output_values,title =f"Signal after averaging with window size = {W_S}"))

    with st.expander("Sharpening"):
        i,v = TEST_functions.ReadSignalFile("Task_4_Tests\Derivative testcases\Derivative_input.txt")
        st.pyplot(creat_plot("Indices","Values",i,v,title ="Input Signal"))
        Y_indices_D1, Y_samples_D1 = task5_Derivative.compute_first_derivative(v)
        st.pyplot(creat_plot("Indices","Values",Y_indices_D1,Y_samples_D1,title ="First Derivative of input signal"))

        Y_indices_D2, Y_samples_D2 = task5_Derivative.compute_second_derivative(v)
        st.pyplot(creat_plot("Indices","Values",Y_indices_D2,Y_samples_D2,title ="Second Derivative of input signal"))

    with st.expander("Convolution"):
        i,v = TEST_functions.ReadSignalFile("Task_4_Tests\Convolution testcases\Signal 1.txt")
        i2,v2 = TEST_functions.ReadSignalFile("Task_4_Tests\Convolution testcases\Signal 2.txt")

        st.pyplot(creat_plot("Indices","Values",i,v,title ="Signal 1"))
        st.pyplot(creat_plot("Indices","Values",i2,v2,title ="Signal 2"))

        Y_indices, Y_samples = Task5_Convolution.compute_convolution(i, v, i2, v2)
        st.pyplot(creat_plot("Indices","Values",Y_indices,Y_samples,title ="Convolution of the 2 signals"))

elif selected == "Task 5":
    st.title("Task 5")
    fs = st.number_input("Sampling frequency: ")
    indices, samples =Task_5_DFT.MyReadSignalFile("Task_5_Tests\DFT\input_Signal_DFT.txt")

    As ,phase_shifts, omegas = Task_5_DFT.DFT(indices, samples,fs)

    st.pyplot(creat_plot("Omega","Amplitude",omegas,As,Label="none",title ="Omega Vs Amplitudes", y_Ticks = "none",y_tick_labels = omegas))

    st.pyplot(creat_plot("Omega","Phase Shift",omegas,phase_shifts,Label="none",title ="Omega Vs Phase Shift", y_Ticks = "none",y_tick_labels = omegas))

    Amps,phas = Task_5_DFT.MyReadSignalFile("Task_5_Tests\IDFT\Input_Signal_IDFT_A_Phase.txt")
    values = Task_5_DFT.IDFT(Amps, phas)

    indices = list(range(len(values)))

    st.pyplot(creat_plot("Indices","Values",indices,values,title ="Signal after reconstruction (IDFT)"))

elif selected == "Task 6":
    st.title("Task 6")
    i,v = TEST_functions.ReadSignalFile("Task_6_Tests\Point1 Correlation\Corr_input signal1.txt")
    i2,v2 = TEST_functions.ReadSignalFile("Task_6_Tests\Point1 Correlation\Corr_input signal2.txt")

    st.pyplot(creat_plot("Indices","Values",i,v,title ="Signal 1"))
    st.pyplot(creat_plot("Indices","Values",i2,v2,title ="Signal 2"))

    Y_indices, Y_samples = Task_6_Correlation_P1.compute_r12(i,v,i2,v2)
    norm = Task_6_Correlation_P1.compute_p12(Y_samples, v, v2)

    st.pyplot(creat_plot("Indices","Values",Y_indices,norm,title ="Correlation of both signals after normalization"))

    st.write("time delay---------------------------------------------------")
    i,v = TEST_functions.ReadSignalFile("Task_6_Tests\Point2 Time analysis\TD_input signal1.txt")
    i2,v2 = TEST_functions.ReadSignalFile("Task_6_Tests\Point2 Time analysis\TD_input signal2.txt")

    st.pyplot(creat_plot("Indices","Values",i,v,title ="Signal 1"))
    st.pyplot(creat_plot("Indices","Values",i2,v2,title ="Signal 2"))

    Y_indices, Y_samples = Task_6_Correlation_P1.compute_r12(i,v,i2,v2)
    norm = Task_6_Correlation_P1.compute_p12(Y_samples, v, v2)
    time =Task_6_Correlation_P1.time_delay(100)
    st.write("time delay=",time)

elif selected == "Task 7":
    st.title("Task 7")
    i,v = TEST_functions.ReadSignalFile("Filters_Tests\FIR test cases\Testcase 2\ecg400.txt")

    options = ["low", "high", "bandpass", "bandstop"]

    choice = st.selectbox("Choose type of filter:", options)

    fs = st.number_input("Enter Sampling Frequency: ",value=8000)
    sba = st.number_input("stop attenuation : ",value=50)
    tb = st.number_input("transition band : ",value=500)

    if choice == "low" or choice == "high":
        f1 = st.number_input("Enter cut off frequency: ",value=1500)
        fil = Filters.make_filter(choice, fs, sba , tb , f1)
    elif choice == "bandpass" or choice == "bandstop":
        f1 = st.number_input("Enter f1: ")
        f2 = st.number_input("Enter f2: ")
        fil = Filters.make_filter(choice, fs, sba , tb , f1,f2)
        
    y_indices, y_samples = compute_convolution(i, v,list(fil.keys()), list(fil.values()))

    st.pyplot(creat_plot("Indices","Values",i,v,title ="ecg 400 signal"))
    st.pyplot(creat_plot("Indices","Values",fil.keys(),fil.values(),title ="Filter in time domain"))
    st.pyplot(creat_plot("Indices","Values",y_indices,y_samples,title ="Convolution of signal and filter"))
    

   

















