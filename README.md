# 🎯 Interview Coach AI

<div align="center">

**An intelligent, AI-powered interview evaluation system that provides comprehensive candidate assessment with actionable feedback**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

[🚀 Live Demo](#-live-demo) • [✨ Features](#-features) • [🛠️ Installation](#️-installation) • [📖 Usage](#-usage)

</div>

---

## 🌟 Overview

**Interview Coach AI** is a sophisticated evaluation system designed to help interviewers and hiring managers assess candidate responses with precision and consistency. Built with modern web technologies and intelligent rule-based algorithms, it provides instant, comprehensive feedback across multiple competency dimensions.

### 🎯 Key Highlights

- **100% Free & Offline** - No API keys, no costs, no usage limits
- **Intelligent Analysis** - Advanced keyword detection and scoring algorithms
- **Comprehensive Evaluation** - Multi-dimensional competency assessment
- **Actionable Insights** - Detailed explanations, follow-up questions, and coaching tips
- **Modern UI** - Beautiful, responsive interface with gradient design

---

## ✨ Features

### 📊 Multi-Dimensional Scoring
- **Communication** (1-5 scale) - Evaluates clarity, structure, and articulation
- **Technical Depth** (1-5 scale) - Assesses technical knowledge and expertise
- **Problem Solving** (1-5 scale) - Analyzes analytical thinking and solution approach
- **Culture Fit** (1-5 scale) - Evaluates teamwork, collaboration, and alignment

### 🎓 Intelligent Feedback System
- **Detailed Explanations** - Contextual insights for each competency score
- **Targeted Follow-up Questions** - 3 personalized questions based on response analysis
- **Coaching Tips** - Actionable advice to improve interview performance
- **STAR Method Guidance** - Structured approach recommendations

### 🚀 Technical Excellence
- **Rule-Based Intelligence** - No external API dependencies
- **Offline Capability** - Works completely offline after installation
- **Fast Performance** - Instant evaluation with no network delays
- **Scalable Architecture** - Clean, modular codebase

---

## 🚀 Live Demo

**👉 [Try the Live Demo on Streamlit Cloud](https://interview-coach-ai.streamlit.app)**

*Experience the full functionality with sample interview questions and responses*

---

## 🛠️ Installation

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Quick Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Pranamya1833/interview-coach-ai.git
   cd interview-coach-ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the app**
   - Open your browser to `http://localhost:8501`
   - Start evaluating interview responses!

---

## 📖 Usage

### Basic Workflow

1. **Enter Job Role**
   - Specify the position (e.g., "Backend Engineer", "Data Scientist")

2. **Input Interview Question**
   - Paste or type the interview question

3. **Add Candidate Response**
   - Enter the candidate's answer

4. **Get Instant Evaluation**
   - Click "Evaluate Response" to receive:
     - Competency scores (1-5 for each dimension)
     - Detailed explanations
     - Follow-up questions
     - Personalized coaching tips

### Example

```
Job Role: Backend Engineer
Question: "Tell me about a time you handled a production outage."
Response: "I once handled a production outage by identifying a misconfigured database index..."

Result: 
- Communication: 4/5
- Technical Depth: 5/5
- Problem Solving: 4/5
- Culture Fit: 3/5
+ Detailed explanations and follow-up questions
```

---

## 🏗️ Architecture

```
interview-coach-ai/
├── app.py                      # Main Streamlit application
├── agent/
│   ├── coach_agent.py         # Core evaluation logic
│   ├── coach_agent_fallback.py # Rule-based evaluation system
│   └── prompt.py              # Evaluation prompts and templates
├── requirements.txt            # Python dependencies
└── README.md                  # Project documentation
```

### System Design

- **Frontend**: Streamlit with custom CSS styling
- **Backend**: Python-based rule engine
- **Evaluation Engine**: Keyword analysis and scoring algorithms
- **No External Dependencies**: Works completely offline

---

## 🧠 How It Works

The system uses intelligent rule-based algorithms to analyze candidate responses:

1. **Text Analysis** - Parses answer length, structure, and content
2. **Keyword Detection** - Identifies technical terms, problem-solving indicators, and collaboration signals
3. **Scoring Algorithm** - Calculates scores based on multiple factors
4. **Contextual Feedback** - Generates personalized explanations and recommendations

---

## 🆓 Free & Unlimited

- ✅ **No API Keys Required** - Works completely offline
- ✅ **No Costs** - Completely free to use
- ✅ **No Usage Limits** - Evaluate unlimited responses
- ✅ **No Internet Required** - Works offline after installation
- ✅ **Open Source** - Free to modify and distribute

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.11+
- **Evaluation Engine**: Custom rule-based algorithms
- **Styling**: Custom CSS with modern gradient design

---

## 📝 Project Status

✅ **Fully Functional** - All features implemented and tested  
✅ **Production Ready** - Stable and reliable  
✅ **Well Documented** - Comprehensive documentation  
✅ **Actively Maintained** - Regular updates and improvements  

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Pranamya M Rao**

- GitHub: [@Pranamya1833](https://github.com/Pranamya1833)
- Repository: [interview-coach-ai](https://github.com/Pranamya1833/interview-coach-ai)

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Designed for modern interview evaluation workflows
- Inspired by the need for consistent, objective candidate assessment

---

<div align="center">

**⭐ If you find this project helpful, please give it a star! ⭐**

Made with ❤️ for better interview experiences

</div>
