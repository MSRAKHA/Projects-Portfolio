# #all projects url in streamlit deploy as https://rakhamsprojecturls.streamlit.app



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
    tab1, tab2, tab3, tab4,tab5 = st.tabs(["2022", "2023", "2024", "2025","Certificates"])
    
    # Project data structure
    projects = {
        "2022": [
            {
                "name": "Personal Portfolio",
                "description": "Developed a modern, responsive personal portfolio website showcasing professional experience, skills, and projects. Implemented smooth animations, dark/light mode, and contact form functionality.",
                "url": "https://rakhashaik.netlify.app",
                "status": "Completed",
                "tech_stack": "React.js, Node.js, Express.js, CSS3, HTML5, JavaScript ES6+, Material-UI, Netlify CI/CD"
            },
            {
                "name": "Brother Portfolio",
                "description": "Designed and developed a professional portfolio website with dynamic content loading, responsive design, and optimized performance. Integrated blog section and project showcase with filtering capabilities.",
                "url": "https://abbassm.netlify.app",
                "status": "Completed",
                "tech_stack": "React.js, Node.js, Express.js, MongoDB, Bootstrap 5, AWS S3, Netlify"
            },
            {
                "name": "Friends Portfolio",
                "description": "Created a customized portfolio platform with interactive UI elements, portfolio gallery, and integrated CMS for easy content updates. Implemented SEO best practices and performance optimization.",
                "url": "https://deepikakendole.netlify.app",
                "status": "Completed",
                "tech_stack": "React.js, Node.js, Express.js, Redux, SASS, Webpack, Git, Netlify"
            }
            
        ],
        "2023": [
            {
                "name": "GenAI App",
                "description": "Developed an advanced AI content generation platform utilizing multiple AI models for text, image, and analysis generation. Implemented rate limiting, error handling, and user authentication for secure API access.",
                "url": "Private",
                "status": "Completed",
                "tech_stack": "Python, TensorFlow 2.x, PyTorch, OpenAI GPT-4, Google Gemini, Hugging Face Transformers, FastAPI, Redis, Docker"
            },
            {
                "name": "Task Project Management System",
                "description": "Built a comprehensive project management solution with real-time collaboration features, task tracking, timeline management, and automated reporting. Implemented role-based access control and activity logging.",
                "url": "Private",
                "status": "Completed",
                "tech_stack": "Python, SQLite, Docker, Streamlit, Redis, JWT Authentication, REST APIs, Celery, PostgreSQL"
            },
            {
                "name": "AWS Supply Chain Management - Smith & Nephew",
                "description": "Architected and implemented an end-to-end supply chain management solution on AWS, featuring inventory tracking, demand forecasting, and automated order processing. Reduced operational costs by 30%.",
                "url": "Private",
                "status": "Completed",
                "tech_stack": "AWS (Lambda, DynamoDB, SQS, SNS, CloudWatch), Python, Terraform, Docker, Kubernetes"
            },
            {
                "name": "Auto Edge Connect",
                "description": "Developed an automated edge computing solution on AWS, enabling seamless deployment and management of edge applications. Implemented auto-scaling, monitoring, and disaster recovery features.",
                "url": "Private",
                "status": "Completed",
                "tech_stack": "AWS EKS, EC2, ECR, S3, CloudFront, Route53, VPC, IAM, Python, Terraform, Docker, Kubernetes"
            }
        ],
        "2024": [
            {
                "name": "Mental Health Tracker - Mood Lens App",
                "description": "Created an innovative mental health monitoring application with mood tracking, analysis, and personalized recommendations. Features include journal entries, mood patterns visualization, and progress tracking with AI-powered insights.",
                "url": "https://rakha-shaik-mental-health-tracker.streamlit.app",
                "status": "Completed",
                "tech_stack": "Python 3.9+, Streamlit, Pandas, Plotly, SQLAlchemy, scikit-learn, Firebase Auth, REST APIs, TensorFlow for sentiment analysis"
            },
            {
                "name": "GenAI Multimodel App",
                "description": "Built a sophisticated multi-modal AI platform capable of image generation, analysis, and text processing. Implemented secure user authentication, rate limiting, and usage analytics. Features include batch processing, custom model fine-tuning, and API integration dashboard.",
                "url": "https://rakhashaikgenai.streamlit.app/",
                "status": "Completed",
                "tech_stack": "Python, Streamlit, OpenAI API (GPT-4, DALL-E), Flux, FastAPI, Redis, PostgreSQL, Docker, JWT Authentication"
            },
            {
                "name": "TCS Mental Health Tracker -RR- App",
                "description": "Enterprise-level mental health monitoring solution for TCS employees. Includes anonymous reporting, crisis intervention alerts, wellness resource directory, and integration with employee assistance programs. Features real-time analytics and trend analysis.",
                "url": "https://rpl-raipur-rockets.streamlit.app",
                "status": "Completed",
                "tech_stack": "Python, Streamlit, MongoDB, Redis, Pandas, Plotly, Machine Learning (scikit-learn), REST APIs, OAuth2"
            },
            {
                "name": "Dr.Soni Bhavani -BFF",
                "description": "Digital memory preservation platform with advanced media management capabilities. Features include AI-powered photo organization, facial recognition, timeline generation, and secure sharing mechanisms. Implemented cloud storage integration and backup systems.",
                "url": "https://se-msr-dr-dsb.streamlit.app/",
                "status": "Completed",
                "tech_stack": "Python, Streamlit, AWS S3, OpenCV, TensorFlow, Face Recognition, SQLAlchemy, Redis Cache"
            },
            {
                "name": "Vercel APP",
                "description": "Advanced image analysis platform leveraging Anthropic's Claude API for detailed visual understanding and processing. Implemented features for batch processing, custom analysis pipelines, and automated reporting with comprehensive API documentation.",
                "url": "Private",
                "status": "Completed",
                "tech_stack": "Python, Streamlit, Anthropic Claude API, FastAPI, Redis, PostgreSQL, Docker, Vercel deployment"
            },
            {
                "name": "RAG App",
                "description": "Developed a sophisticated Retrieval-Augmented Generation system using Amazon Bedrock LLM. Features include document processing, semantic search, dynamic knowledge base updates, and context-aware responses with citation support.",
                "url": "Private",
                "status": "Completed",
                "tech_stack": "Amazon Bedrock, Python, Streamlit, AWS Services (S3, Lambda, DynamoDB), LangChain, FAISS, Hugging Face Embeddings"
            },
            {
                "name": "Automation AWS Pipeline",
                "description": "Enterprise-grade automation pipeline for complex workflow orchestration. Implemented event-driven architecture with scheduled triggers, error handling, retry mechanisms, and comprehensive monitoring. Reduced manual intervention by 90% and improved process reliability.",
                "url": "Private",
                "status": "Completed",
                "tech_stack": "AWS (EventBridge, Lambda, Step Functions, Batch), Flask, Streamlit, Docker, Terraform, CloudWatch, SNS"
            }
        ],
        "2025": [
            {
                "name": "TCS RPL Coding Challenge Invoicify 📄",
                "description": "Enterprise-grade invoice processing system with multi-language support and advanced OCR capabilities. Features include automated data extraction, signature verification, fraud detection, and integration with major accounting systems. Reduced processing time by 75% and improved accuracy to 99.9%.",
                "url": "https://ms-rakha-invoicify.hf.space",
                "status": "Completed",
                "tech_stack": "Python, Gradio, LangChain, Groq LLM, Pandas, Pydantic, PIL, OpenCV, Tesseract OCR, MongoDB, Redis, Docker, REST APIs"
            },
            {
                "name": "ISLAMIC Daily Dua App -1",
                "description": "Comprehensive Islamic daily prayer and dua application with personalized reminders and scheduling. Features include Qibla direction, prayer times, transliteration, audio recitations, and progress tracking. Supports multiple languages and madhabs.",
                "url": "https://islamic-dua-by-rakha-shaik.streamlit.app",
                "status": "Completed",
                "tech_stack": "Python, Streamlit, MongoDB, Redis Cache, GeoPy, Prayer Times API, AWS Lambda, CloudFront"
            },
            {
                "name": "ISLAMIC Daily Dua App -2",
                "description": "Enhanced version of the Islamic app with additional features for Ramadan planning, tafseer integration, and community engagement. Includes smart notifications, custom dua collections, and habit tracking with gamification elements.",
                "url": "https://msr-ramadan25.streamlit.app",
                "status": "Completed",
                "tech_stack": "Python, Streamlit, PostgreSQL, Redis, Celery, REST APIs, Firebase, PWA capabilities"
            },
            {
                "name": "TalentFlow",
                "description": "Advanced talent management and recruitment platform with AI-powered candidate matching. Features include skill assessment, automated screening, interview scheduling, and analytics dashboard. Integrates with major job boards and ATS systems.",
                "url": "https://talentflow.streamlit.app/",
                "status": "Completed",
                "tech_stack": "Python, Streamlit, SQL, Redis, Machine Learning (scikit-learn), NLP, REST APIs, OAuth2"
            },
            {
                "name": "Projects Portfolio",
                "description": "Centralized portfolio platform showcasing professional projects with detailed analytics and interactive demonstrations. Features include live project previews, technology stack visualization, and integrated contact system.",
                "url": "https://rakhamsprojecturls.streamlit.app/",
                "status": "Completed",
                "tech_stack": "Streamlit, Python, PostgreSQL, AWS S3, CloudFront, Analytics APIs, Custom CSS/HTML"
            },
            {
                "name": "Business Website",
                "description": "Full-featured e-commerce platform with advanced inventory management, payment processing, and customer relationship management. Implementing AI-powered product recommendations and personalized shopping experience.",
                "url": "Private",
                "status": "In Progress",
                "tech_stack": "Python, Streamlit, PostgreSQL, Stripe API, Redis, ElasticSearch, Docker, Kubernetes"
            },
            {
                "name": "SmartGen Ecom",
                "description": "Next-generation e-commerce platform with AI-driven personalization, real-time inventory optimization, and advanced analytics. Planning features include AR product visualization and voice commerce integration.",
                "url": "Not started yet",
                "status": "Planned",
                "tech_stack": "React, Node.js, MongoDB, GraphQL, AWS, AI/ML, AR/VR technologies"
            },
            {
                "name": "mindfocus",
                "description": "Cognitive training platform featuring adaptive brain games and mental exercises. Includes progress tracking, personalized difficulty scaling, and detailed performance analytics with scientific backing.",
                "url": "https://mindfocus-rakhams.lovable.app/",
                "status": "Completed",
                "tech_stack": "React 18, TypeScript, Vite, Redux Toolkit, TailwindCSS, Jest, React Testing Library, PWA features"
            },
            {
                "name": "More Projects Coming Up",
                "description": "Portfolio of upcoming projects focusing on healthcare innovation, IT infrastructure modernization, e-commerce solutions, and educational technology. Emphasis on AI/ML integration and cloud-native architectures.",
                "url": "https://github.com/MSRAKHA",
                "status": "In Progress",
                "tech_stack": "React, Python, TensorFlow, PyTorch, AWS, Azure, Kubernetes, GraphQL, Web3, Computer Vision"
            }
        ],
         "Certificates" :[
             {
                 "name":"Credly Certificate Badges Account",
                 "description": "https://www.credly.com/users/rakha-shaik",
                 "url" :"https://www.credly.com/users/rakha-shaik",
                 "status": "Certificates InProgress",
                 "tech_stack":""
             },
         {
             "name" : "Azure Fundamentals",
             "description": "",
             "url": "https://www.credly.com/badges/c737c405-f772-4ada-99a3-3e6750e60a81/public_url",
             "status": "completed",
             "tech_stack": "Azure Cloud"
         },
             {
             "name" : "AWS Cloud Practitioner",
             "description": "",
             "url": "https://www.credly.com/badges/329dcc5e-4b12-49e9-b740-da45ac7b3846/public_url",
             "status": "completed",
             "tech_stack": "AWS Cloud"
                 
             },
             {
              "name" : "AWS Solution Architect ",
             "description": "",
             "url": "https://www.credly.com/badges/eeded8cd-9f73-4faa-b9c1-b1a59e165924/public_url",
             "status": "completed",
             "tech_stack": "AWS Cloud"   
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
    with tab5:
        st.header("Rakha's Certificates So Far")
        for project in projects["Certificates"]:
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
# import streamlit as st

# # Configure Streamlit page
# st.set_page_config(
#     page_title="Rakhs's Project's Portfolio",
#     page_icon="🚀",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# def main():
#     st.title(":rainbow[Welcome to MS Rakha Projects Portfolio]")
#     st.header(":blue[🚀 Projects Timeline]")
    
#     # Create tabs for different years
#     tab1, tab2, tab3, tab4 = st.tabs(["2022", "2023", "2024", "2025"])
    
#     # Project data structure
#     projects = {
#         "2022": [
#             {
#                 "name": "Personal Portfolio",
#                 "description": "Built a Personal Portfolio platform using React and Node.js",
#                 "url": "https://rakhashaik.netlify.app",
#                 "status": "Completed",
#                 "tech_stack": "React, Node.js,CSS,HTML"
#             },
#             {
#                 "name": "Brother Portfolio",
#                 "description": "Built a Personal Portfolio platform using React and Node.js",
#                 "url": "https://abbassm.netlify.app",
#                 "status": "Completed",
#                 "tech_stack": "React, Node.js"
#             },
#             {
#                 "name": "Friends Portfolio",
#                 "description": "Built a Personal Portfolio platform using React and Node.js",
#                 "url": "https://deepikakendole.netlify.app",
#                 "status": "Completed",
#                 "tech_stack": "React, Node.js"
#             }
            
#         ],
#         "2023": [
#             {
#                 "name": "GenAI App",
#                 "description": "API keys used to generate the content and analysis",
#                 "url": "Private",
#                 "status": "Completed",
#                 "tech_stack": "Python, TensorFlow, GANs,OpenAI,Gemini"
#             },
#             {
#                 "name": "Task Project Management System",
#                 "description": "Team collaboration and task management platform",
#                 "url": "Private",
#                 "status": "Completed",
#                 "tech_stack": "SQLite,Docker,Streamlit"
#             },
#             {
#                 "name":"AWS Supply Chain Management -Smith & Nephew",
#                 "description": "Supply Chain Management",
#                 "url": "Private",
#                 "status": "Completed",
#                 "tech_stack": "AWS Services"
#             },
#             {
#                 "name":"Auto Edge Connect",
#                 "description": "Automated Edge Connect on AWS",
#                 "url": "Private",
#                 "status": "Completed",
#                 "tech_stack": "AWS Services like EKS,EC2,ECR,S3 and more"
#             }
#         ],
#         "2024": [
#             {
#                 "name":"Mental Health Tracker - Mood Lens App",
#                 "description": "Mental health monitoring and tracking app",
#                 "url": "https://rakha-shaik-mental-health-tracker.streamlit.app",
#                 "status": "Completed",
#                 "tech_stack": "Python,Streamlit"
#             },
#                         {
#                 "name":"GenAI Multimodel App",
#                 "description": "Image generation ,Analysis,--us-- user1, pw -- password1",
#                 "url": "https://rakhashaikgenai.streamlit.app/",
#                 "status": "Completed",
#                 "tech_stack": "Python,Streamlit,OpenAI,Flux,API Keys"
#             },
#             {
#                 "name":"TCS Mental health Tracker -RR- App",
#                 "description": "Mental health monitoring and tracking app",
#                 "url": "https://rpl-raipur-rockets.streamlit.app",
#                 "status": "Completed",
#                 "tech_stack": "Python,Streamlit"
#             },
#             {
#                 "name":"Dr.Soni Bhavani -BFF",
#                 "description": "Memories to remember",
#                 "url": "https://se-msr-dr-dsb.streamlit.app/",
#                 "status": "Completed",
#                 "tech_stack": "Python,Streamlit"
#             },
#             {
#                 "name":"Vercel APP",
#                 "description": "Image Analysis using Anthropic API key",
#                 "url": "Private",
#                 "status": "Completed",
#                 "tech_stack": "Python,Streamlit"
#             },
#             {
#                 "name":"RAG App",
#                 "description": "Amazon Bedrock LLM ",
#                 "url": "Private",
#                 "status": "Completed",
#                 "tech_stack": "Amazon Bedrock,Python,Streamlit,AWS Services"
#             },
#             {
#                 "name":"Automation AWS Pipeline",
#                 "description": "Scheduled Events to process the workflow feasibly without human interactions",
#                 "url": "Private",
#                 "status": "Completed",
#                 "tech_stack": "AWS Services like AWS EventBridge,AWS Lamda,AWS Stepfunctions,AWS Batch Jobs,Flask App,Streamlit"
#             },
            
#         ],
#         "2025": [
#             {
            
#                 "name":"TCS RPL Coding Challenge Invoicify 📄",
#                 "description": "Invoicify can be integrated into different aspects of an organization's operations, making it a versatile tool for businesses of various sizes and industries. The application's ability to handle multiple languages, verify signatures, and maintain accurate records makes it particularly valuable for organizations with complex invoice processing needs.",
#                 "url": "https://ms-rakha-invoicify.hf.space",
#                 "status": "Completed",
#                 "tech_stack": "Python, Gradio, LangChain, Groq LLM, Pandas, Pydantic, PIL (Python Imaging Library), openpyxl, python-dotenv, JSON, base64, llama-3.2-90b-vision-preview, HTML/CSS, REST APIs"
#             },



            
#             {
#                 "name":"ISLAMIC Daily Dua App -1",
#                 "description": "Reminders to read Duas Daily",
#                 "url": "https://islamic-dua-by-rakha-shaik.streamlit.app",
#                 "status": "Completed",
#                 "tech_stack": "Python,Streamlit"
#             },
            
#             {
#                 "name":"ISLAMIC Daily Dua App -2 ",
#                 "description": "Reminders to read Duas Daily",
#                 "url": "https://msr-ramadan25.streamlit.app",
#                 "status": "Completed",
#                 "tech_stack": "Python,Streamlit"
#             },
#             {
#                 "name":"TalentFlow",
#                 "description": "TalentFlow help you to find out the Right Candidates for your Projects and Clients.",
#                 "url": "https://talentflow.streamlit.app/",
#                 "status": "Completed",
#                 "tech_stack": "Python,Streamlit,SQL"
#             },
#             {
#                 "name":"Projects Portfolio",
#                 "description": "All My Project Urls",
#                 "url": "https://rakhamsprojecturls.streamlit.app/",
#                 "status": "Completed",
#                 "tech_stack": "Streamlit"
#             },
#             {
#                 "name":"Business Website",
#                 "description": "Ecom",
#                 "url": "Private",
#                 "status": "In Progress",
#                 "tech_stack": "Python,Streamlit"
#             },
            
#             {
#                 "name": "SmartGen Ecom",
#                 "description": "Upcoming project",
#                 "url": "Not started yet",
#                 "status": "Planned",
#                 "tech_stack": "To be decided"
#             },
#              {
#                 "name":"mindfocus",
#                 "description":"Mind games",
#                 "url":"https://mindfocus-rakhams.lovable.app/",
#                 "status":"Completed",
#                 "tech_stack":"React (v18) - Main UI framework,Vite - Build tool and development server,TypeScript - For type-safe JavaScript development"
#             },
            
#             {
#                 "name": "More Projects Coming Up",
#                 "description": "Health ,IT,Ecommerce,Studies",
#                 "url": "https://github.com/MSRAKHA",
#                 "status": "In Progress",
#                 "tech_stack": "React,Python,AI,CV,GenAI and more"
#             }
           
#         ]
#     }

#     # 2022 Projects Tab
#     with tab1:
#         st.header("2022 Projects")
#         for project in projects["2022"]:
#             with st.expander(f"🚀 {project['name']} - {project['status']}"):
#                 st.markdown(f"""
#                     **Description:** {project['description']}  
#                     **Tech Stack:** {project['tech_stack']}  
#                     **Project URL:**
#                 """)
#                 st.code(project['url'], language="bash")

#     # 2023 Projects Tab
#     with tab2:
#         st.header("2023 Projects")
#         for project in projects["2023"]:
#             with st.expander(f"🚀 {project['name']} - {project['status']}"):
#                 st.markdown(f"""
#                     **Description:** {project['description']}  
#                     **Tech Stack:** {project['tech_stack']}  
#                     **Project URL:**
#                 """)
#                 st.code(project['url'], language="bash")

#     # 2024 Projects Tab
#     with tab3:
#         st.header("2024 Projects")
#         for project in projects["2024"]:
#             with st.expander(f"🚀 {project['name']} - {project['status']}"):
#                 st.markdown(f"""
#                     **Description:** {project['description']}  
#                     **Tech Stack:** {project['tech_stack']}  
#                     **Project URL:**
#                 """)
#                 st.code(project['url'], language="bash")

#     # 2025 Projects Tab
#     with tab4:
#         st.header("2025 Projects")
#         for project in projects["2025"]:
#             with st.expander(f"🚀 {project['name']} - {project['status']}"):
#                 st.markdown(f"""
#                     **Description:** {project['description']}  
#                     **Tech Stack:** {project['tech_stack']}  
#                     **Project URL:**
#                 """)
#                 st.code(project['url'], language="bash")

# # Custom CSS for better styling
# st.markdown("""
#     <style>
#     .stApp {
#         max-width: 1200px;
#         margin: 0 auto;
#     }
#     .st-emotion-cache-16idsys p {
#         font-size: 16px;
#     }
#     .stTabs [data-baseweb="tab-list"] {
#         gap: 24px;
#     }
#     .stTabs [data-baseweb="tab"] {
#         height: 50px;
#         padding: 0 24px;
#         background-color: #f0f2f6;
#         border-radius: 4px;
#     }
#     .stTabs [aria-selected="true"] {
#         background-color: #1f77b4;
#         color: white;
#     }
#     .project-card {
#         padding: 20px;
#         border-radius: 5px;
#         margin: 10px 0;
#         background-color: #ffffff;
#         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
#     }
#     </style>
# """, unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()
