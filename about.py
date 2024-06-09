import streamlit as st
import plotly.graph_objects as go

def show_about():
    """
    Function to display information about the dataset.
    """
       
    st.subheader("About Dataset")
    st.write("This file is having news data. Fake news or hoax news is false or misleading information presented as news. Fake news often has the aim of damaging the reputation of a person or entity, or making money through advertising revenue. This dataset is having Both Fake and Real news.")
    st.write("The columns present in the dataset are:-")
    st.write("1) Title: Title of the News")
    st.write("2) Text: Text or Content of the News")
    st.write("3) Label: Labelling the news as Fake or Real")

    st.subheader("Real and Fake News Comparison")
    st.write("Real: 3171")
    st.write("Fake: 3164")
    st.write("Output: 50.06% Real and 49.94% Fake")

    # Visualization
    labels = ['Real', 'Fake']
    counts = [3171, 3164]
    colors = ['#ff9999', '#66b3ff']

    fig = go.Figure(data=[go.Pie(labels=labels, values=counts, hole=.3, textinfo='percent+label')])
    fig.update_traces(marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    fig.update_layout(title_text="Real and Fake News Comparison", title_font_color="white", font=dict(color="white"))
    st.plotly_chart(fig)

    st.write("Source: [Fake News Dataset](https://www.kaggle.com/datasets/rajatkumar30/fake-news)")

    # Display team information
    st.write("Final Project: [Digital Skola](https://digitalskola.com/)")
    st.write("By: Team 1-Membara")

    # Display logo in the top-right corner
    st.image("Logo_Digital_Skola.png", width=80)

show_about()

