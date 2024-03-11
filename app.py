import streamlit as st
import numpy as np
from main import gauss_elem, getAug, isValid


st.title('Gaussian Elimination method')

st.header('AX = B')
num = st.selectbox('Select the number of equations', [
                   2, 3, 4])


def resetvalues(num):
    A = np.ones((num, num))
    B = np.ones((num, 1))

    majorX = ["x", "y", "z", "w"]
    X = [[majorX[i]] for i in range(num)]

    return A, B, X


A, B, X = resetvalues(num)


col1, col2, col3 = st.columns(3)

with col1:
    st.header('A')
    st.data_editor(A, hide_index=True)

with col2:
    st.header('X')
    st.dataframe(X)

with col3:
    st.header('B')
    st.data_editor(B)


if isValid(A) and isValid(B):
    augmented = getAug(A, B)
    solutions = gauss_elem(augmented)
    if solutions == "No Solution":
        st.subheader("No Solution, please update the matrix")

    else:
        st.subheader("Solution:")

        for i in range(num):
            st.success(f"{X[i][0]} = {solutions[i]}")


else:
    st.error("Invalid input, please enter valid numbers")


st.write(" ")
st.write(" ")
st.write("Developed by")
st.dataframe({
    "Name": ["Sarfaraj Ansari", "Kshitij Dalvi", "Yash Nema", "Rajeev Ranjan Prata Singh", "Shubham gupta", "Vadik Mane", "Rishabh Sharma", "Vansh Dudeja"],
    "Registration Number":["22BAI10129","22BAI10285","22BAI10011","22BAI10344","22BAI10187","22BAI10280","22BAI10367","22BAI10257"]
})
