# 🤖 AI Agent by Sachin

A powerful AI chatbot built with **LangChain**, **Google Gemini**, and **Streamlit**.

## ✨ Features

- 💬 Natural conversation with AI
- 🧠 Powered by Google Gemini 2.0 Flash
- 🎨 Clean, responsive web interface
- 📱 Mobile-friendly design
- ⚙️ Adjustable temperature settings
- 🔄 Conversation memory within sessions

## 🚀 Live Demo

**Coming Soon** - Will be deployed on Vercel

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.0 Flash
- **Framework**: LangChain
- **Deployment**: Vercel
- **Package Manager**: UV
- **Language**: Python 3.9+

## 🏃‍♂️ Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ai-agent
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   ```bash
   # Create .env file with:
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Run the application**
   ```bash
   # Web interface
   uv run streamlit run streamlit_app.py
   
   # Command line
   uv run python main.py "Your question here"
   
   # Interactive mode
   uv run python main.py
   ```

## 🌐 GitHub to Vercel Deployment Steps

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Deploy AI Agent to Vercel"
git push origin main
```

### Step 2: Connect to Vercel
1. Go to [vercel.com/dashboard](https://vercel.com/dashboard)
2. Click **"Import Project"**
3. Connect your GitHub repository
4. Select your AI agent repository

### Step 3: Configure Environment Variables
1. In Vercel dashboard, go to **Settings > Environment Variables**
2. Add new variable:
   - **Name**: `GOOGLE_API_KEY`
   - **Value**: `AIzaSyAg04tHud7gxErOdGSZNodbFdtmvHbz-iw`
   - **Environment**: Production, Preview, Development

### Step 4: Deploy
1. Click **"Deploy"** button
2. Wait for deployment to complete
3. Your AI agent will be live at: `https://your-project-name.vercel.app`

## 📁 Project Structure

```
ai-agent/
├── main.py              # Core AI agent logic
├── streamlit_app.py     # Streamlit web interface
├── api/
│   └── index.py         # Vercel API endpoint
├── requirements.txt     # Python dependencies
├── vercel.json         # Vercel deployment config
└── README.md          # This file
```

## 💡 Usage Examples

### Command Line
```bash
uv run python main.py "What is artificial intelligence?"
```

### Web Interface
1. Run `uv run streamlit run streamlit_app.py`
2. Open http://localhost:8501
3. Type your message and chat with AI!

## ⚙️ Configuration

- **Model**: `models/gemini-2.0-flash`
- **Temperature**: 0.7 (adjustable in web UI)
- **Max History**: 40 messages (20 exchanges)

## 👨‍💻 Created By

**Sachin**
- LinkedIn: [sachin-pradhan-ba82a927a](https://www.linkedin.com/in/sachin-pradhan-ba82a927a)
- Created with ❤️ using LangChain and Google Gemini

---

⭐ **Star this repository if you found it helpful!**