# CareerForge 🚀 Interview Assistant

A professional interviewer chatbot built with Streamlit and LangChain that helps users practice job interviews in their chosen domain.

![CareerForge Logo](logo.png)

## Features

- Interactive chat interface for interview practice
- Personalized interview experience based on user's job role
- Structured interview flow with introduction, questions, and feedback
- Simulates a real interview environment with one question at a time
- Provides feedback on interview performance upon request
- Easy to restart interviews with a single click

## Requirements

- Python 3.7+
- Streamlit
- LangChain
- OpenAI API key
- Python-dotenv
- Pillow (PIL)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/careerforge-interview-assistant.git
   cd careerforge-interview-assistant
   ```

2. Create and activate a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. Make sure you have the `logo.png` file in the project directory
2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
3. Open your browser and navigate to the URL displayed in the terminal (typically http://localhost:8501)
4. Start practicing your interview by following the chatbot's prompts

## How It Works

1. The chatbot begins by asking for a brief introduction
2. It then asks about your target job role
3. Based on your responses, it conducts a structured interview with 5 questions
4. After the interview, it provides feedback on your performance if requested
5. You can restart the interview at any time using the sidebar button

## Project Structure

- `app.py`: Main application file containing the Streamlit interface and LangChain integration
- `logo.png`: Logo image for the application
- `.env`: Environment file for storing API keys (not included in repository)

## Customization

You can customize the interview experience by modifying the prompt template in the `app.py` file. The template controls how the AI interviewer behaves and what types of questions it asks.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Built with ❤️ by [Prince Choudhury](https://www.linkedin.com/in/prince-choudhury26/)

GitHub: [Prince-Choudhury](https://github.com/Prince-Choudhury)
