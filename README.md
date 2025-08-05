
# 📜 YouTube Script Generator using LangChain & Streamlit

This project is a beginner-friendly YouTube script generator powered by **LangChain** and **Google Gemini (via LangChain)**, with a sleek and interactive **Streamlit** frontend.

## 🔧 Backend Highlights
- Utilizes `ChatGoogleGenerativeAI` from `langchain_google_genai` to generate engaging, informative scripts.
- Prompts are dynamically created using `ChatPromptTemplate`.
- Environment variables are securely loaded using `python-dotenv`.

## 🎨 Frontend Features
- Built with **Streamlit** for a fast and responsive UI.
- Users can input a topic and instantly receive a full YouTube video script.
- Ideal for content creators, educators, and marketers.


## 🚀 Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Vinothini-S-1311/LangChain_YouTube_Script_Generator.git
   cd LangChain_YouTube_Script_Generator
   ```
2. Install dependencies:
	pip install -r requirements.txt

3. Set up environment variables: Create a .env file in the root directory and add your Google API key:
	GOOGLE_API_KEY=your_api_key_here

4. Run the Streamlit app:
	streamlit run SG_Frontend.py  
