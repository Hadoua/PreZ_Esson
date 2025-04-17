import streamlit as st
import os
from PIL import Image
import base64

## 100% inspired by https://medium.com/data-science/the-portfolio-that-got-me-a-data-scientist-job-513cc821bfe4 
## 100% for fun and code requires optimization

## Functions 
def get_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def display_technologies(images):
    style = "display:flex; align-items:center; border:1px solid #ddd; padding:5px; border-radius:5px;"
    techs = "".join(
        f'<div style="{style}"><img src="data:image/png;base64,{img}" width="20"/>&nbsp;{name}</div>'
        for name, img in images.items()
    )
    st.markdown(f"<div style='display:flex; gap:10px; align-items:center;'>{techs}</div>", unsafe_allow_html=True)
    

def sidebar_summary():
    st.sidebar.title("Pitterson Ibara")
    image = Image.open('img3.jpg')
    st.sidebar.image(image, width=750)
    st.sidebar.markdown("""
    **Data scientist** with 3 years of experience in the insurance industry, focusing on P&C insurance, pricing, and claims. Holds a master's degree in data science from the Institut National des Sciences Appliquées (INSA) Rouen in France, with previous experience in the banking sector.
""")
    st.sidebar.markdown("[View my LinkedIn profile](https://www.linkedin.com/in/pitterson-ibara-7b29995a/)")

def zindi_challenge(icons_path):
    st.subheader("Clinical Reasoning Challenge")
    st.write("""
             The kenya clinical reasoning challenge is a Natural Language Processing predictive challenge commissioned by the Path Living Labs team in collaboration with Moi University. In this challenge, participants are tasked with predicting clinicians' responses to 400 clinical scenarios based on information collected by nurses in direct contact with patients. The vignettes include details such as the nurse's background, patient demographics, presenting symptoms, relevant clinical findings, and a specific clinical question intended for the clinician. These elements enable clinicians to engage in clinical reasoning, develop a differential diagnosis, formulate a management plan, and provide specific answers to the scenario questions, reflecting the constraints and realities of the Kenyan healthcare system.
    
     In this project, I fine-tuned a T5 transformer model.
     """)
    images = {
        "Python": get_image_as_base64(os.path.join(icons_path, "python.png")),
        "HuggingFace Transformers": get_image_as_base64(os.path.join(icons_path, "huggingface-color.png")),
        "Google Colab": get_image_as_base64(os.path.join(icons_path, "colab-color.png")),
    }
    display_technologies(images)
    st.markdown("<br>[View the code on Colab](https://github.com/your-repo/project1)", unsafe_allow_html=True)
    st.markdown("<hr style='margin: 20px 0;'>", unsafe_allow_html=True)

def portfolio_creation(icons_path):
    st.subheader("Creating my portfolio with streamlit")
    st.write("""
    This project involves creating my personal online portfolio using Streamlit. 
    """)
    images = {
        "Vscode": get_image_as_base64(os.path.join(icons_path, "vscode.png")),
        "Git": get_image_as_base64(os.path.join(icons_path, "icons8-git-48.png")),
        "Streamlit": get_image_as_base64(os.path.join(icons_path, "streamlit-mark-color.png")),
        "Python": get_image_as_base64(os.path.join(icons_path, "python.png")),
    }
    display_technologies(images)
    st.markdown("<br>[View the code on GitHub](https://github.com/Hadoua/PreZ_Esson)",  unsafe_allow_html=True)
    st.markdown("<hr style='margin: 20px 0;'>", unsafe_allow_html=True)

def chatbot(icons_path):
    st.subheader("Exploring question-answering with RAG")
    st.write("""
    In this project, I implemented a question-answering system using Retrieval-Augmented Generation (RAG) with Hugging Face. The system is designed to read and interpret information from a PDF file, utilizing natural language processing techniques to extract and answer questions based on the content.
    """)
    images = {
        "OpenAI API": get_image_as_base64(os.path.join(icons_path, "openai.505x512.png")),
        "Langchain": get_image_as_base64(os.path.join(icons_path, "langchain-color.png")),
        "Mistral AI": get_image_as_base64(os.path.join(icons_path, "mistral-color.png")),
        "Google Colab": get_image_as_base64(os.path.join(icons_path, "colab-color.png")),
        "Python": get_image_as_base64(os.path.join(icons_path, "python.png")),
    }
    display_technologies(images)
    st.markdown("<br>[View the code on GitHub](https://github.com/Hadoua?tab=repositories)",  unsafe_allow_html=True)
    st.markdown("<hr style='margin: 20px 0;'>", unsafe_allow_html=True)

def challenge_paris_pompiers(icons_path):
    st.subheader("Predicting response times of the Paris fire brigade vehicles")
    st.write("""
    The Predicting response times of the Paris Fire Brigade vehicles challenge was a predictive modeling competition organized by the Paris Fire Brigade in 2019. Participants had to predict the delay between the selection of a rescue vehicle (the moment a rescue team is alerted) and the moment it arrives at the scene of the rescue request based on information about the emergency vehicle, the intervention, the operational status, and the GPS positions before and during the intervention.

    I participated in this challenge and achieved 3rd place by applying various machine learning techniques. I handled missing values and created new features, using the Google Maps API for route and duration estimates. I utilized models such as LGBM, CatBoost, and XGBoost, and performed Bayesian optimization of hyperparameters. Additionally, I implemented ensemble techniques to enhance model performance.    """)
    images = {
        "Python": get_image_as_base64(os.path.join(icons_path, "python.png")),
        "Jupyter": get_image_as_base64(os.path.join(icons_path, "jupyter_logo_icon_169452.png")),
        "Google maps API": get_image_as_base64(os.path.join(icons_path, "google-maps.png")),
        "Sklearn": get_image_as_base64(os.path.join(icons_path, "scikit-learn.png")),
    }
    display_technologies(images)
    st.markdown('<br><span style="color:blue">Code coming soon</span>', unsafe_allow_html=True)
    st.markdown("<hr style='margin: 20px 0;'>", unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(
        page_title="Pitterson Ibara's Portfolio",
        layout="wide",
        page_icon='👩🏻‍🚀'
    )
    
    st.title("A few projects in data science")
    st.markdown("<hr style='margin: 20px 0;'>", unsafe_allow_html=True)
    
    # Removing the path as Streamlit doesn't handle it well
    icons_path = "."
    
    sidebar_summary()
    zindi_challenge(icons_path)
    chatbot(icons_path)
    portfolio_creation(icons_path)
    challenge_paris_pompiers(icons_path)
