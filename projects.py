#all projects url in streamlit deploy as https://rakhamsprojecturls.streamlit.app
import streamlit as st

# Configure Streamlit page
st.set_page_config(
    page_title="Rakhs's Project's Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def main():
    st.title(":rainbow[Welcome to MS Rakha Projects Portfolio]")
    st.header(":blue[🚀 Projects Timeline]")
    
    # Create tabs for different years
    tab1, tab2, tab3, tab4 = st.tabs(["2022", "2023", "2024", "2025"])
    
    # Project data structure
    projects = {
        "2022": [
            {
                "name": "Personal Portfolio",
                "description": "Built a Personal Portfolio platform using React and Node.js",
                "url": "https://rakhashaik.netlify.app",
                "status": "Completed",
                "tech_stack": "React, Node.js,CSS,HTML"
            },
            {
                "name": "Brother Portfolio",
                "description": "Built a Personal Portfolio platform using React and Node.js",
                "url": "https://abbassm.netlify.app",
                "status": "Completed",
                "tech_stack": "React, Node.js"
            },
            {
                "name": "Friends Portfolio",
                "description": "Built a Personal Portfolio platform using React and Node.js",
                "url": "https://deepikakendole.netlify.app",
                "status": "Completed",
                "tech_stack": "React, Node.js"
            }
            
        ],
        "2023": [
            {
                "name": "GenAI App",
                "description": "API keys used to generate the content and analysis",
                "url": "Private",
                "status": "Completed",
                "tech_stack": "Python, TensorFlow, GANs,OpenAI,Gemini"
            },
            {
                "name": "Task Project Management System",
                "description": "Team collaboration and task management platform",
                "url": "Private",
                "status": "Completed",
                "tech_stack": "SQLite,Docker,Streamlit"
            },
            {
                "name":"AWS Supply Chain Management -Smith & Nephew",
                "description": "Supply Chain Management",
                "url": "Private",
                "status": "Completed",
                "tech_stack": "AWS Services"
            },
            {
                "name":"Auto Edge Connect",
                "description": "Automated Edge Connect on AWS",
                "url": "Private",
                "status": "Completed",
                "tech_stack": "AWS Services like EKS,EC2,ECR,S3 and more"
            }
        ],
        "2024": [
            {
                "name":"Mental Health Tracker - Mood Lens App",
                "description": "Mental health monitoring and tracking app",
                "url": "https://rakha-shaik-mental-health-tracker.streamlit.app",
                "status": "Completed",
                "tech_stack": "Python,Streamlit"
            },
                        {
                "name":"GenAI Multimodel App",
                "description": "Image generation ,Analysis,--us-- user1, pw -- password1",
                "url": "https://rakhashaikgenai.streamlit.app/",
                "status": "Completed",
                "tech_stack": "Python,Streamlit,OpenAI,Flux,API Keys"
            },
            {
                "name":"TCS Mental health Tracker -RR- App",
                "description": "Mental health monitoring and tracking app",
                "url": "https://rpl-raipur-rockets.streamlit.app",
                "status": "Completed",
                "tech_stack": "Python,Streamlit"
            },
            {
                "name":"Dr.Soni Bhavani -BFF",
                "description": "Memories to remember",
                "url": "https://se-msr-dr-dsb.streamlit.app/",
                "status": "Completed",
                "tech_stack": "Python,Streamlit"
            },
            {
                "name":"Vercel APP",
                "description": "Image Analysis using Anthropic API key",
                "url": "Private",
                "status": "Completed",
                "tech_stack": "Python,Streamlit"
            },
            {
                "name":"RAG App",
                "description": "Amazon Bedrock LLM ",
                "url": "Private",
                "status": "Completed",
                "tech_stack": "Amazon Bedrock,Python,Streamlit,AWS Services"
            },
            {
                "name":"Automation AWS Pipeline",
                "description": "Scheduled Events to process the workflow feasibly without human interactions",
                "url": "Private",
                "status": "Completed",
                "tech_stack": "AWS Services like AWS EventBridge,AWS Lamda,AWS Stepfunctions,AWS Batch Jobs,Flask App,Streamlit"
            },
            
        ],
        "2025": [
            {
            
                "name":"TCS RPL Coding Challenge Invoicify",
                "description": "Bill extraction in hindi english",
                "url": "https://ms-rakha-invoicify.hf.space",
                "status": "Completed",
                "tech_stack": "Python,gradio,This code represents a sophisticated invoice processing application that leverages several modern technologies and frameworks. Here's a detailed breakdown of the tech stack:
Core Framework and UI
The application is built primarily using Gradio, a Python library that makes it easy to create user-friendly web interfaces for machine learning models. The UI is designed with a clean, modern interface that includes features like image upload, zoom controls, and form inputs.
AI and Machine Learning Components
The application uses Groq's LLM (Large Language Model) service, specifically the "llama-3.2-90b-vision-preview" model, for OCR (Optical Character Recognition) and text processing. LangChain is used to manage the interactions with the LLM and handle prompt engineering.
Data Processing and Validation
Pandas is used for data manipulation and handling Excel operations
Pydantic provides robust data validation through type checking and data modeling
PIL (Python Imaging Library) handles image processing operations
JSON is used for structured data handling
Storage and File Operations
The application uses Excel as its storage solution, with openpyxl handling the Excel file operations. Environment variables are managed using python-dotenv for secure configuration.
Key Features
1. OCR capabilities for extracting text from invoice images
Interactive image manipulation (zoom in/out)
Structured data extraction for invoice details
Excel-based data storage and export
Form validation and error handling
Real-time data processing
This tech stack represents a modern approach to document processing, combining web technologies, AI/ML capabilities, and traditional data processing tools in a single application. The architecture allows for scalable, efficient processing of invoice documents while maintaining a user-friendly interface."
            },



            
            {
                "name":"ISLAMIC Daily Dua App -1",
                "description": "Reminders to read Duas Daily",
                "url": "https://islamic-dua-by-rakha-shaik.streamlit.app",
                "status": "Completed",
                "tech_stack": "Python,Streamlit"
            },
            
            {
                "name":"ISLAMIC Daily Dua App -2 ",
                "description": "Reminders to read Duas Daily",
                "url": "https://msr-ramadan25.streamlit.app",
                "status": "Completed",
                "tech_stack": "Python,Streamlit"
            },
            {
                "name":"TalentFlow",
                "description": "TalentFlow help you to find out the Right Candidates for your Projects and Clients.",
                "url": "https://talentflow.streamlit.app/",
                "status": "Completed",
                "tech_stack": "Python,Streamlit,SQL"
            },
            {
                "name":"Projects Portfolio",
                "description": "All My Project Urls",
                "url": "https://rakhamsprojecturls.streamlit.app/",
                "status": "Completed",
                "tech_stack": "Streamlit"
            },
            {
                "name":"Business Website",
                "description": "Ecom",
                "url": "Private",
                "status": "In Progress",
                "tech_stack": "Python,Streamlit"
            },
            
            {
                "name": "SmartGen Ecom",
                "description": "Upcoming project",
                "url": "Not started yet",
                "status": "Planned",
                "tech_stack": "To be decided"
            },
             {
                "name":"mindfocus",
                "description":"Mind games",
                "url":"https://mindfocus-rakhams.lovable.app/",
                "status":"Completed",
                "tech_stack":"React (v18) - Main UI framework,Vite - Build tool and development server,TypeScript - For type-safe JavaScript development"
            },
            
            {
                "name": "More Projects Coming Up",
                "description": "Health ,IT,Ecommerce,Studies",
                "url": "https://github.com/MSRAKHA",
                "status": "In Progress",
                "tech_stack": "React,Python,AI,CV,GenAI and more"
            }
           
        ]
    }

    # 2022 Projects Tab
    with tab1:
        st.header("2022 Projects")
        for project in projects["2022"]:
            with st.expander(f"🚀 {project['name']} - {project['status']}"):
                st.markdown(f"""
                    **Description:** {project['description']}  
                    **Tech Stack:** {project['tech_stack']}  
                    **Project URL:**
                """)
                st.code(project['url'], language="bash")

    # 2023 Projects Tab
    with tab2:
        st.header("2023 Projects")
        for project in projects["2023"]:
            with st.expander(f"🚀 {project['name']} - {project['status']}"):
                st.markdown(f"""
                    **Description:** {project['description']}  
                    **Tech Stack:** {project['tech_stack']}  
                    **Project URL:**
                """)
                st.code(project['url'], language="bash")

    # 2024 Projects Tab
    with tab3:
        st.header("2024 Projects")
        for project in projects["2024"]:
            with st.expander(f"🚀 {project['name']} - {project['status']}"):
                st.markdown(f"""
                    **Description:** {project['description']}  
                    **Tech Stack:** {project['tech_stack']}  
                    **Project URL:**
                """)
                st.code(project['url'], language="bash")

    # 2025 Projects Tab
    with tab4:
        st.header("2025 Projects")
        for project in projects["2025"]:
            with st.expander(f"🚀 {project['name']} - {project['status']}"):
                st.markdown(f"""
                    **Description:** {project['description']}  
                    **Tech Stack:** {project['tech_stack']}  
                    **Project URL:**
                """)
                st.code(project['url'], language="bash")

# Custom CSS for better styling
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .st-emotion-cache-16idsys p {
        font-size: 16px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0 24px;
        background-color: #f0f2f6;
        border-radius: 4px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1f77b4;
        color: white;
    }
    .project-card {
        padding: 20px;
        border-radius: 5px;
        margin: 10px 0;
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
