import streamlit as st
import time

def main():
    st.title("Digital Clock")
    st.markdown("## A simple digital clock using Streamlit")
    
    clock_placeholder = st.empty()
    
    while True:
        current_time = time.strftime("%H:%M:%S %p")
        clock_placeholder.markdown(f"# {current_time}")
        time.sleep(1)

if __name__ == "__main__":
    main()

