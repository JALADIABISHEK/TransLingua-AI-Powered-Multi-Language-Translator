# TransLingua-AI-Powered-Multi-Language-Translator
This project delivers a lightweight web interface for translating sentences between languages with the help of Google’s Gemini models, accessed through LangChain. Users can supply their own API key directly in the app sidebar, choose any text, and get instant translations.

Table of Contents
Features
Architecture
Prerequisites
Local Development
Running the App
Supplying the API Key
Deployment (Streamlit Community Cloud)
Repository Structure
Troubleshooting
License
Features
Streamlit UI for quick, browser-based interaction.
Sidebar input field for securely providing the Google API key each session.
Prompt template with system/human roles that LangChain uses to construct requests.
Uses langchain-google-genai to reach Gemini (gemini-2.0-flash-001) with a configurable temperature.
Graceful feedback for missing API keys, empty text input, and run-time errors.
Architecture
Layer	Description
UI (Streamlit)	Handles text input, button rendering, and displays translations / error states.
Prompt Engineering	ChatPromptTemplate defines the translator persona and format of user prompts.
LLM Connector	ChatGoogleGenerativeAI from langchain_google_genai communicates with Gemini.
Output Parsing	StrOutputParser converts model responses into plain strings.
Runtime Configuration	Environment variables or sidebar input capture the Google API key.
Prerequisites
Python 3.13 or newer (earlier 3.x versions should work, but 3.13 is verified).
Google Gemini API access (obtainable via Google AI Studio / MakerSuite).
Git (optional, for deployments and collaboration).
Local Development
Clone the repository:

git clone https://github.com/Subramaniya-pillai/language-translator-streamlit.git
cd language-translator-streamlit
Set up a virtual environment (recommended):

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
Install the required packages:

pip install -r requirements.txt
Running the App
Start Streamlit:

streamlit run app.py
Streamlit opens the app in your default browser (or provides a local URL to click).

Supplying the API Key
Locate the sidebar on the left side of the app.
Paste your Gemini API key into the “Enter your Google API key” field.
The field is masked as a password and stored only for the current session.
If you prefer environment variables, set GOOGLE_API_KEY before starting Streamlit—the sidebar will auto-fill it.
Enter the text you want translated in the main input box.
Click “Translate” to run the request.
The translated text appears below the button, or warnings/errors appear if something needs attention.
Deployment (Streamlit Community Cloud)
Push the repository to GitHub (already done for Subramaniya-pillai/language-translator-streamlit).
Sign in to Streamlit Community Cloud.
Click Deploy an app, choose the repository, branch, and set app.py as the entry point.
No secrets are required because the API key is entered in the sidebar at runtime.
Deploy. Streamlit builds the environment using requirements.txt.
Share the generated URL. Each user must enter their own key when they access the app.
Live deployment: https://language-translator-subramani.streamlit.app/
Repository Structure
├── app.py            # Streamlit application source
├── requirements.txt  # Python dependencies
├── .gitignore        # Specifies files Git should ignore (e.g., .env, __pycache__)
└── README.md         # This documentation
Optional: You can create a .env file locally for development convenience, but keep it out of version control.

Troubleshooting
Cannot import langchain_google_genai
Run pip install -r requirements.txt to ensure dependencies are installed.

Streamlit raises “GOOGLE_API_KEY not found”
Enter your key in the sidebar or set GOOGLE_API_KEY before starting the app.

“Failed to fetch translation” or generic errors
The error box displays the exception. Common causes are invalid keys, exceeded quotas, or network issues.

Blank page after deployment
Check Streamlit Cloud logs via the deployment dashboard to see installation or runtime errors.
