# Tone Analyzer

A simple AI-powered tone analysis tool built with LangChain and Azure OpenAI. Analyzes text and determines whether the tone is positive, negative, or neutral with detailed explanations.

## Features

- **Structured Output**: Uses Pydantic models for consistent JSON responses
- **High Accuracy**: Powered by Azure OpenAI GPT-4o model
- **Detailed Analysis**: Provides confidence scores, explanations, and key phrases
- **Simple CLI**: Easy-to-use command line interface
- **Error Handling**: Robust error management and validation

## Project Structure

```
tone_analyzer/
├── .env                 # Azure OpenAI credentials
├── requirements.txt     # Python dependencies
├── models.py           # Pydantic model for structured output
├── config.py           # Azure OpenAI configuration
├── tone_analyzer.py    # Main analyzer logic with LangChain
└── main.py             # Simple CLI interface
```

## Setup

1. **Clone and setup environment:**
   ```bash
   git clone <your-repo>
   cd tone_analyzer
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Azure OpenAI:**
   - Copy `.env` file and fill in your Azure OpenAI credentials:
   ```
   AZURE_OPENAI_API_KEY=your_api_key_here
   AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
   AZURE_OPENAI_API_VERSION=2024-10-21
   AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
   ```

## Usage

**Run the interactive analyzer:**
```bash
python main.py
```

**Example session:**
```
🎯 Simple Tone Analyzer
==============================
Enter text to analyze (or 'quit' to exit)

📝 Enter your text: I absolutely love this new product!

🔍 Analyzing...

📊 Results:
   Tone: POSITIVE
   Confidence: 95.0%
   Explanation: The text conveys enthusiasm and satisfaction with strong positive indicators.
   Key Phrases: absolutely love, new product
```

## Output Format

Each analysis returns:
- **Tone**: positive, negative, or neutral
- **Confidence**: percentage score (0-100%)
- **Explanation**: detailed reasoning for the tone classification
- **Key Phrases**: important words/phrases that influenced the decision

## Technical Stack

- **LangChain**: For structured AI workflows
- **Pydantic**: For data validation and structured outputs
- **Azure OpenAI**: GPT-4o model for tone analysis
- **Python 3.8+**: Core programming language

## Learning Objectives

This project demonstrates:
- LangChain chain composition (prompt → LLM → parser)
- Pydantic models for structured AI outputs
- Azure OpenAI integration
- CLI application development
- Error handling and validation
