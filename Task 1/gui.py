import test
import Task1Functions

import streamlit as st
import matplotlib.pyplot as plt


# Data
x = test.indices_s1
y = test.samples_s1

# Create a figure
fig, ax = plt.subplots()
ax.plot(x, y, label="Signal 1")
ax.set_xlabel("Indices")
ax.set_ylabel("Values")
ax.legend()

# Show in Streamlit
st.pyplot(fig)

# Data
x = test.indices_s2
y = test.samples_s2

# Create a figure
fig, ax = plt.subplots()
ax.plot(x, y, label="Signal 2")
ax.set_xlabel("Indices")
ax.set_ylabel("Values")
ax.legend()

# Show in Streamlit
st.pyplot(fig)


options = ["Add", "Multiply", "Subtract", "Delay/Advance", "Folding/reversing"]

choice = st.selectbox("Choose operation:", options)

st.write("You selected:", choice)

if choice == "Add":
    fig, ax = plt.subplots()
    ax.plot(test.add_output_indices, test.add_output_samples)
    ax.set_xlabel("Indices")
    ax.set_ylabel("Values")
    ax.set_title("Signal 1 + Signal 2")
    ax.legend()

    # Show in Streamlit
    st.pyplot(fig)

elif choice == "Subtract":
    fig, ax = plt.subplots()
    ax.plot(test.sub_output_indices, test.sub_output_samples)
    ax.set_xlabel("Indices")
    ax.set_ylabel("Values")
    ax.set_title("Signal 1 - Signal 2")
    ax.legend()

    # Show in Streamlit
    st.pyplot(fig)

elif choice == "Multiply":
    fig, ax = plt.subplots()
    ax.plot(test.mul_output_indices, test.mul_output_samples)
    ax.set_xlabel("Indices")
    ax.set_ylabel("Values")
    ax.set_title("Signal 1 *5 ")
    ax.legend()

    # Show in Streamlit
    st.pyplot(fig)

elif choice == "Delay/Advance":
    fig, ax = plt.subplots()
    ax.plot(test.my_indices_shift, test.my_samples_shift)
    ax.set_xlabel("Indices")
    ax.set_ylabel("Values")
    ax.set_title("Signal 1 advanced by 3 ")
    ax.legend()

    # Show in Streamlit
    st.pyplot(fig)

elif choice == "Folding/reversing":
    options = ["Signal 1", "Signal 2"]
    choice = st.selectbox("Choose Signal:", options)

    if choice == "Signal 1":
        fig, ax = plt.subplots()
        ax.plot(test.my_indices_fold, test.my_samples_fold)
        ax.set_xlabel("Indices")
        ax.set_ylabel("Values")
        ax.set_title("Signal 1 after folding")
        ax.legend()

        # Show in Streamlit
        st.pyplot(fig)
    else:
        x, y = Task1Functions.myfolding(test.indices_s2,test.samples_s2)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel("Indices")
        ax.set_ylabel("Values")
        ax.set_title("Signal 2 after folding")
        ax.legend()

        # Show in Streamlit
        st.pyplot(fig)



