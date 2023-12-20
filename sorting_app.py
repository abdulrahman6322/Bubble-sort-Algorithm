import streamlit as st

# Sorting algorithm
def bubble_sort(arr):
    n = len(arr)
    steps = []

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                # Save the current step
                steps.append(arr.copy())

    return steps, arr

# Streamlit UI
def main():
    st.title("Bubble Sort Array Sorting App")

    # User input
    array = st.text_input("Enter comma-separated array:", "5,2,8,1,6,3,7,4")
    array = [int(x) for x in array.split(",")]

    if st.button("Sort"):
        steps, sorted_array = bubble_sort(array.copy())
        st.success(f"Sorted array using Bubble Sort:\n{sorted_array}")

        # Display intermediate steps
        st.subheader("Intermediate Steps:")
        for step in steps:
            st.write(step)

if __name__ == "__main__":
    main()
    
