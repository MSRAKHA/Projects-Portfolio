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
