import test
import Task1Functions
import Task_2

import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu


def creat_plot(x_Label,y_label,x,y,Label="none",title ="none"):
    fig, ax = plt.subplots()

    if Label=="none":
        ax.plot(x, y)
    else:
        ax.plot(x, y, label=Label)

    ax.set_xlabel(x_Label)
    ax.set_ylabel(y_label)
    if title != "none":
        ax.set_title(title)
    ax.legend()
    return fig


with st.sidebar:
    selected = option_menu(
        menu_title="Choose Task",
        options=["Task 1","Task 2"],
    )

if selected == "Task 1":
    st.title("Task 1")
    # Data
    x_s1 = test.indices_s1
    y_s1 = test.samples_s1

    st.pyplot(creat_plot("Indices","Values",x_s1,y_s1,Label="Signal 1"))

    # Data
    x_s2 = test.indices_s2
    y_s2 = test.samples_s2


    # Show in Streamlit
    st.pyplot(creat_plot("Indices","Values",x_s2,y_s2,Label="Signal 2"))

    options = ["Add", "Multiply", "Subtract", "Delay/Advance", "Folding/reversing"]

    choice = st.selectbox("Choose operation:", options)

    st.write("You selected:", choice)

    if choice == "Add":

        st.pyplot(creat_plot("Indices","Values",test.add_output_indices, test.add_output_samples,title="Signal 1 + Signal 2"))

    elif choice == "Subtract":

        st.pyplot(creat_plot("Indices","Values",test.sub_output_indices, test.sub_output_samples,title="Signal 1 - Signal 2"))

    elif choice == "Multiply":

        st.pyplot(creat_plot("Indices","Values",test.mul_output_indices, test.mul_output_samples,title="Signal 1 *5 "))

    elif choice == "Delay/Advance":

        st.pyplot(creat_plot("Indices","Values",test.my_indices_shift, test.my_samples_shift,title="Signal 1 advanced by 3 "))

    elif choice == "Folding/reversing":
        options = ["Signal 1", "Signal 2"]
        choice = st.selectbox("Choose Signal:", options)

        if choice == "Signal 1":

            st.pyplot(creat_plot("Indices","Values",test.my_indices_fold, test.my_samples_fold,title="Signal 1 after folding"))
        else:
            x_f, y_f = Task1Functions.myfolding(test.indices_s2,test.samples_s2)
            st.pyplot(creat_plot("Indices","Values",x_f, y_f,title="Signal 2 after folding"))


elif selected == "Task 2":
    st.title("Task 2")
    signal_type = st.selectbox("Signal Generation:", ["Sin", "Cos"])
    representation = st.selectbox("Representation:", ["Continuous", "Discrete"])
    A = st.number_input("Enter Amplitude: ")
    phase_degree = st.number_input("Enter Phase Shift in degrees: ")
    analog_freq = st.number_input("Enter Analog Frequency: ")
    fs = None
    if representation == "Discrete":
        fs = st.number_input("Enter Sampling Frequency: ")
    duration = st.number_input("Enter Duration:", value=1.0)
    x, y = Task_2.generate_signal(signal_type, representation.lower(), A, phase_degree, analog_freq, fs, duration)

   
    st.pyplot(creat_plot("Time","Value",x,y))




