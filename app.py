import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt

# st.title("My Jupyter Notebook Projects")

# # Sample DataFrame
# df = pd.DataFrame({
#     'x': range(10),
#     'y': range(10)
# })

# st.write("## DataFrame")
# st.dataframe(df)

# # Plot
# fig, ax = plt.subplots()
# ax.plot(df['x'], df['y'])
# ax.set_title('Sample Plot')

# st.write("## Plot")
# st.pyplot(fig)

st.title("Hello, Streamlit!")
st.header("Data Science")
st.subheader("Machine Learning")
st.text("Large Language Models")
st.write("This is a minimalist Streamlit application.")

st.markdown("##### HI") # h5 html tag
st.markdown("# HI")

st.info("Hang in there for a couple of seconds")
st.success("👌 successfully Done!!!")
st.warning("You may have to do it next time")
st.error("It fails")

exp = ZeroDivisionError("Division By Zero is Sin")
st.exception(exp)
st.help(AttributeError)
st.code('x = 10\n'
        'for i in range(x):\n'
            'print(i)'
)
st.write([i for i in range(10)])
st.text_input("Username : ")
st.text_input("Password : ",type="password")
if st.checkbox("Done!"):
    st.success("You have done with the taks congrats! 🤑🤑🤑")
elif st.checkbox("Not yet!"):
    st.warning("Hola Bruv you are running out time🥵🥵🥵")
elif st.checkbox("Not Started"):
    st.error("Who chose you to do this in the first place😡😡😡")


    radioButton = st.radio("Level :",("Intern","Junior","Mid","Senior"))

    if radioButton == "Intern":
        st.write("We are not going to hire you")
    else:
        st.write("You are fired")


selected = st.selectbox("Select your field: ",["web developer","Data Scientist","AI/ML engineer","Data Engineer"])
st.write("You have selected ",selected)

multiselected = st.multiselect("Select your field: ",["web developer","Data Scientist","AI/ML engineer","Data Engineer"])
st.write("You have selected ",*multiselected)

if st.button("Submit"):
    st.success("All the information is submitted!")
else:
    st.warning("You have to submit your information!")

st.slider("slider",1,100,step=1)