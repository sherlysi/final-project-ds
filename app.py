import streamlit as st
import streamlit.components.v1 as stc
from about import show_about
import ml_app

# HTML template for the header
html_temp = """
            <div style="background-color:#3872fb;padding:10px;border-radius:10px">
            <h1 style="color:white;text-align:center;">Fake News Prediction App</h1>
            <h4 style="color:white;text-align:center;">Combatting Fake News for a Responsible Society</h4>
            </div>
            """

# Description of the app content
desc_temp = """
            ### Fake News Prediction App
            This app will be used by individuals, organizations, and tech companies to predict whether news is fake or real.
            Combatting fake news is important for maintaining an informed and responsible society.
            #### App Content
            - Prediction 
            - About 
            """

def main():
    # Display the HTML template for the header
    stc.html(html_temp)
    
    # Sidebar menu options
    menu = ['Home', 'Prediction', 'About']
    # Allow user to select from the sidebar menu
    choice = st.sidebar.selectbox('Menu', menu)

    # Depending on the choice, display different content
    if choice == 'Home':
        # Display welcome message and app description
        st.subheader("Welcome to Homepage")
        st.markdown(desc_temp)
    elif choice == "Prediction":
        # Display a section for prediction
        ml_app.run_ml_app()
    elif choice == "About":
        # Display information about the app and dataset
        show_about()

if __name__ == '__main__':
    main()

