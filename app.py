"""
A simple streamlit app demo.
"""

import streamlit as st  # Import the streamlit package to the app.
import pandas as pd  # import the pandas package to handle data.

# Page setting - Set's your application's layout, title and icon.
# "KE" is the shortcode for an emoji of the Kenyan flag
# Check all supported emojis here - https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json
st.set_page_config(
    layout="wide", page_title="Visualising City Population, Kenya", page_icon="🇰🇪"
)


# The code below use the inbuilt streamlit "write" functionality and
# Markdown Language to write formated texts on your app.
# You can learn more about Markdown by Googling it.


st.write(
    """
    ### My First Streamlit Application
    #### This app will display graphs of the populations of several Kenya towns.
    #### Data used for Demo purposes only. Not accurate!

"""
)

# In the following code section, we shall create a new pandas data frame, read data to it and
# do some simple analysis.

df = pd.read_csv(
    "data/kenyan_town_populations.csv"
)  # Creates a dataframe df and loads data to it from the csv file.


# The code below creates and dsiplays a table with an heading.
st.write(
    """
    ##### Table 1: Population of Kenya Towns.

"""
)
st.table(df)  # Using streamlit's table functionality to draw a table of our data


st.markdown("""---""")  # Horizontal seperator

# Calculating the average population in all towns.
average_population = df["Population"].mean()

# Add two new columns to the data frame showing the percentage of population that is male or female
df["Male_Percent"] = [
    55,
    45,
    53,
    52,
    47,
    54,
]  # Say I know Male %. Just attach a new column to df
df["Female_Percent"] = (
    100 - df["Male_Percent"]
)  # Calculate Female % by subtracting Male % from 100

# Add a row of means for all numerical columns

df.loc["Mean_Value"] = df.mean(numeric_only=True)


st.write(
    """
    ##### Table 2: Population of Kenya Towns Male / Female.

"""
)
st.table(df)

# Better textual Visualisation
# Create three Columns in the app and do some visualisation
st.write(
    """
    ##### Key Metrics:

"""
)
a1, a2, a3, a4 = st.columns(4)  # Creat for columns
a1.image("data/kenya.png", width=200)  # Add an image to col 1
a2.metric(
    "Largest City", "Nairobi", +2_000_000
)  # Display highlighted data with stylised text
a3.metric(
    "Smallest City", "Nyeri", -1_000_000
)  # Display another highleted data with stylised text
a4.metric(
    "Average Population", f"{average_population}", "+15.37%"
)  # Note the f-string? Nice solution when using variables.

st.markdown("""---""")  # Horizontal seperator

# Graphical Visualisation of the data
# Create 2 columns in the app
st.write(
    """
    ##### Visualisation: Bar / Line Charts showing Population Per City

"""
)
b1, b2 = st.columns(2)
with b1:
    st.bar_chart(
        df,
        x="City",
        y="Population",
    )  # Barchart visualising the populations of the cities
with b2:
    st.line_chart(
        df, x="City", y="Population"
    )  # Line chart visualising the population of the cities.

st.markdown("""---""")  # Horizontal seperator
