from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from config import AzureOpenAIConfig
from models import ToneAnalysisResult


class ToneAnalyzer:
    """
    Main tone analyzer class that uses LangChain for structured output.
    Combines Azure OpenAI with Pydantic models for consistent results.
    """

    def __init__(self, temperature: float = 0.0):
        """
        Initialize the tone analyzer.

        Args:
            temperature: Controls randomness of AI responses (0.0 = most consistent)
        """
        self.config = AzureOpenAIConfig()
        self.llm = self.config.create_llm(temperature=temperature)

        # Create output parser using our Pydantic model
        self.output_parser = PydanticOutputParser(pydantic_object=ToneAnalysisResult)

        # Create the prompt template
        self.prompt = self._create_prompt_template()

        # Create the chain: prompt -> llm -> parser
        self.chain = self.prompt | self.llm | self.output_parser

    def _create_prompt_template(self) -> ChatPromptTemplate:
        """
        Create the prompt template for tone analysis.
        The prompt includes format instructions from Pydantic model.
        """
        prompt_template = ChatPromptTemplate.from_template(
            """
            You are an expert in tone analysis. Analyze the given text and determine its overall tone.

            Consider the following when analyzing:
            - Word choice and language style
            - Emotional indicators
            - Context and implied meaning
            - Overall sentiment

            Text to analyze: "{text}"

            {format_instructions}

            Important: 
            - Be objective and precise in your analysis
            - Provide specific examples from the text
            - Confidence should reflect how certain you are about the tone
            - Include 2-5 key phrases that influenced your decision
            """
        )

        # Add format instructions from the output parser
        prompt_template = prompt_template.partial(
            format_instructions=self.output_parser.get_format_instructions()
        )

        return prompt_template

    def analyze_tone(self, text: str) -> ToneAnalysisResult:
        """
        Analyze the tone of the given text.

        Args:
            text: The text to analyze

        Returns:
            ToneAnalysisResult: Structured result with tone, confidence, explanation, and key phrases
        """
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")

        try:
            # Invoke the chain with the input text
            result = self.chain.invoke({"text": text})
            return result

        except Exception as e:
            raise RuntimeError(f"Error during tone analysis: {str(e)}")

    def analyze_multiple_texts(self, texts: list[str]) -> list[ToneAnalysisResult]:
        """
        Analyze multiple texts in batch.

        Args:
            texts: List of texts to analyze

        Returns:
            List of ToneAnalysisResult objects
        """
        results = []
        for i, text in enumerate(texts):
            print(f"Analyzing text {i + 1}/{len(texts)}...")
            try:
                result = self.analyze_tone(text)
                results.append(result)
            except Exception as e:
                print(f"Error analyzing text {i + 1}: {e}")
                # Continue with other texts

        return results


# Test the analyzer
if __name__ == "__main__":
    # Create analyzer instance
    analyzer = ToneAnalyzer()

    # Test texts with different tones
    test_texts = [
        "I absolutely love this new product! It's amazing and works perfectly!",
        "This is the worst experience I've ever had. Completely disappointed.",
        "The weather today is cloudy with a chance of rain."
    ]

    print("🔍 Testing Tone Analyzer...")
    print("=" * 50)

    for i, text in enumerate(test_texts, 1):
        print(f"\n📝 Test {i}: {text}")
        print("-" * 30)

        try:
            result = analyzer.analyze_tone(text)
            print(f"Tone: {result.tone}")
            print(f"Confidence: {result.confidence:.2f}")
            print(f"Explanation: {result.explanation}")
            print(f"Key Phrases: {result.key_phrases}")

        except Exception as e:
            print(f"❌ Error: {e}")

    print("\n✅ Testing completed!")
