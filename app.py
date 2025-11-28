import streamlit as st
from agent.coach_agent import evaluate_answer
import json

# Page configuration
st.set_page_config(
    page_title="Interview Coach AI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern, eye-catching design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Global Styles */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 0;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    /* Header Styles */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .main-header h1 {
        color: white;
        font-size: 3rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        background: linear-gradient(45deg, #fff, #f0f0f0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .main-header p {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.2rem;
        margin-top: 0.5rem;
    }
    
    /* Card Styles */
    .evaluation-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .evaluation-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.2);
    }
    
    .input-card {
        background: transparent;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: none;
    }
    
    /* Score Display */
    .score-container {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 1rem;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        margin: 0.5rem 0;
    }
    
    .score-label {
        font-weight: 600;
        color: #2d3748;
        min-width: 150px;
        font-size: 1rem;
    }
    
    .score-value {
        font-size: 2rem;
        font-weight: 700;
        color: #667eea;
    }
    
    .score-bar {
        flex: 1;
        height: 12px;
        background: #e2e8f0;
        border-radius: 10px;
        overflow: hidden;
        position: relative;
    }
    
    .score-fill {
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Badge Styles */
    .badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.25rem;
    }
    
    .badge-free {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
    }
    
    .badge-offline {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Button Styles */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 15px;
        font-size: 1.2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Input Styles */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        padding: 0.75rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Section Headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #2d3748;
        margin: 1.5rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #667eea;
    }
    
    /* Explanation Box */
    .explanation-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    /* Follow-up Questions */
    .question-item {
        background: white;
        padding: 1rem 1.5rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        border-left: 4px solid #38ef7d;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }
    
    /* Coaching Tip */
    .coaching-tip {
        background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border-left: 4px solid #f39c12;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden !important; display: none !important;}
    header {visibility: hidden !important; display: none !important;}
    .stDeployButton {display: none !important;}
    #stDecoration {display: none !important;}
    
    /* Remove any black bars or unwanted elements */
    .stApp > footer {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Ensure no black backgrounds anywhere */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    }
    
    /* Remove default Streamlit spacing issues */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }
    
    /* Remove any bottom bars or dividers */
    hr {
        display: none !important;
    }
    
    /* Ensure consistent background */
    section[data-testid="stSidebar"],
    div[data-testid="stDecoration"] {
        display: none !important;
    }
    
    /* Remove any unwanted borders or bars */
    .element-container {
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Main Header
st.markdown("""
<div class="main-header">
    <h1>🎯 Interview Coach AI</h1>
    <p>Intelligent Evaluation System | 100% Free | Works Offline</p>
    <span class="badge badge-free">FREE</span>
    <span class="badge badge-offline">OFFLINE</span>
    <span class="badge badge-free">UNLIMITED</span>
</div>
""", unsafe_allow_html=True)

# Main Content
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header" style="color: white; border-bottom-color: white;">📝 Interview Details</div>', unsafe_allow_html=True)
    
    job = st.text_input(
        "💼 Job Role",
        placeholder="e.g., Backend Engineer, Data Scientist, Product Manager",
        key="job_input"
    )
    
    question = st.text_area(
        "❓ Interview Question",
        placeholder="Enter the interview question here...",
        height=120,
        key="question_input"
    )
    
    answer = st.text_area(
        "💬 Candidate's Response",
        placeholder="Enter the candidate's answer here...",
        height=200,
        key="answer_input"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Evaluate Button
    evaluate_clicked = st.button("🚀 Evaluate Response", use_container_width=True, type="primary")

with col2:
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header" style="color: white; border-bottom-color: white;">📊 Evaluation Results</div>', unsafe_allow_html=True)
    
    if evaluate_clicked:
        if not job or not question or not answer:
            st.error("⚠️ Please fill in all fields before evaluating.")
        else:
            with st.spinner("🔍 Analyzing response..."):
                try:
                    result = evaluate_answer(job, question, answer)
                    
                    if isinstance(result, dict) and "error" in result:
                        st.error(f"**Error:** {result.get('error', 'Unknown error')}")
                        if "message" in result:
                            st.info(result["message"])
                    else:
                        # Display Scores
                        st.markdown("### 🎯 Competency Scores")
                        
                        scores = result.get("scores", {})
                        score_names = {
                            "communication": "💬 Communication",
                            "technical_depth": "⚙️ Technical Depth",
                            "problem_solving": "🧩 Problem Solving",
                            "culture_fit": "🤝 Culture Fit"
                        }
                        
                        for key, label in score_names.items():
                            score = scores.get(key, 0)
                            score_html = f"""
                            <div class="score-container">
                                <div class="score-label">{label}</div>
                                <div class="score-value">{score}/5</div>
                                <div class="score-bar">
                                    <div class="score-fill" style="width: {score * 20}%"></div>
                                </div>
                            </div>
                            """
                            st.markdown(score_html, unsafe_allow_html=True)
                        
                        # Display Explanations
                        st.markdown("### 📖 Detailed Explanations")
                        explanations = result.get("explanations", {})
                        for key, label in score_names.items():
                            explanation = explanations.get(key, "")
                            if explanation:
                                explanation_html = f"""
                                <div class="explanation-box">
                                    <strong>{label.split(' ', 1)[1]}:</strong><br>
                                    {explanation}
                                </div>
                                """
                                st.markdown(explanation_html, unsafe_allow_html=True)
                        
                        # Follow-up Questions
                        st.markdown("### ❓ Follow-up Questions")
                        follow_ups = result.get("follow_up_questions", [])
                        for i, question in enumerate(follow_ups, 1):
                            question_html = f"""
                            <div class="question-item">
                                <strong>Q{i}:</strong> {question}
                            </div>
                            """
                            st.markdown(question_html, unsafe_allow_html=True)
                        
                        # Coaching Tip
                        coaching_tip = result.get("coaching_tip", "")
                        if coaching_tip:
                            tip_html = f"""
                            <div class="coaching-tip">
                                <strong>💡 Coaching Tip:</strong><br>
                                {coaching_tip}
                            </div>
                            """
                            st.markdown(tip_html, unsafe_allow_html=True)
                            
                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")
                    st.info("💡 This app works completely offline - no API needed!")
    else:
        st.info("👆 Fill in the interview details on the left and click 'Evaluate Response' to get started!")
        st.markdown("""
        <div style="text-align: center; padding: 3rem 0; color: #718096;">
            <h2>🎯 Ready to Evaluate</h2>
            <p>Enter interview details and get instant, intelligent feedback!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer removed - cleaner design
