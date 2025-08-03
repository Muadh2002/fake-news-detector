import streamlit as st
from predict import predict_news

# Page configuration
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .stTextArea textarea {
            min-height: 300px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            width: 100%;
            transition: all 0.3s;
        }
        .stButton button:hover {
            background-color: #45a049;
            transform: scale(1.02);
        }
        .result-box {
            padding: 1.5rem;
            border-radius: 10px;
            margin-top: 1rem;
            font-size: 1.2rem;
            text-align: center;
        }
        .real {
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .fake {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        .header {
            border-bottom: 1px solid #dee2e6;
            padding-bottom: 1rem;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Header section
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/2965/2965878.png", width=80)
with col2:
    st.title("Fake News Detection System")
    st.markdown("""
        <div style='color: #6c757d; margin-bottom: 2rem;'>
            Enter a news article or paragraph to check if it's <strong>Real</strong> or <strong>Fake</strong>.
            Our AI-powered system analyzes the text for authenticity.
        </div>
    """, unsafe_allow_html=True)

# Main content
with st.container():
    user_input = st.text_area(
        "Paste News Article Text Here:",
        placeholder="Enter the news content you want to verify...",
        help="The more text you provide, the more accurate the prediction will be."
    )

    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        if st.button("Check Authenticity", key="predict_button"):
            if user_input.strip() == "":
                st.warning("Please enter some text to analyze.")
            else:
                with st.spinner("Analyzing the content..."):
                    result = predict_news(user_input)
                    
                    # Display result with appropriate styling
                    if result.lower() == "real":
                        st.markdown(f"""
                            <div class='result-box real'>
                                <h3>🔍 Analysis Result</h3>
                                <p>This news is predicted to be: <strong>{result}</strong></p>
                                <p style='font-size: 1rem; margin-top: 0.5rem;'>✅ This content appears to be trustworthy.</p>
                            </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                            <div class='result-box fake'>
                                <h3>🔍 Analysis Result</h3>
                                <p>This news is predicted to be: <strong>{result}</strong></p>
                                <p style='font-size: 1rem; margin-top: 0.5rem;'>⚠️ Be cautious with this content.</p>
                            </div>
                        """, unsafe_allow_html=True)

# Sidebar with additional information
with st.sidebar:
    st.markdown("## About")
    st.info("""
        This Fake News Detection System uses advanced natural language processing 
        to analyze news content and predict its authenticity.
        
        **How it works:**
        - The model examines linguistic patterns
        - Analyzes writing style and content
        - Compares with known fake news characteristics
    """)
    
    st.markdown("## Tips for better results")
    st.write("""
        - Provide complete articles when possible
        - Include at least 3-4 sentences
        - Avoid very short text fragments
    """)
    
    st.markdown("## Examples to try")
    st.code("""
    " Trump Completely SCREWS The Middle East
      Peace Process, Just Another Wednesday For Him"
    """)
    st.code("""
    "The government is secretly implanting 
    microchips in COVID vaccines to track 
    citizens, according to anonymous sources..."
    """)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #6c757d; font-size: 0.9rem;'>
        Fake News Detector • Powered by AI • Use responsibly
    </div>
""", unsafe_allow_html=True)