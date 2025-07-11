import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

# Load environment variables from .env file
load_dotenv()


class AzureOpenAIConfig:
    """
    Configuration class for Azure OpenAI connection.
    Handles all the connection parameters and creates the LLM instance.
    """

    def __init__(self):
        self.api_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
        self.deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

        # Validate that all required environment variables are set
        self._validate_config()

    def _validate_config(self):
        """Validate that all required configuration values are present."""
        required_vars = {
            "AZURE_OPENAI_API_KEY": self.api_key,
            "AZURE_OPENAI_ENDPOINT": self.endpoint,
            "AZURE_OPENAI_API_VERSION": self.api_version,
            "AZURE_OPENAI_DEPLOYMENT_NAME": self.deployment_name
        }

        missing_vars = [var for var, value in required_vars.items() if not value]

        if missing_vars:
            raise ValueError(f"Missing required environment variables: {missing_vars}")

    def create_llm(self, temperature: float = 0.0, max_tokens: int = 1000):
        """
        Create and return AzureChatOpenAI instance.

        Args:
            temperature: Controls randomness (0.0 = deterministic, 1.0 = creative)
            max_tokens: Maximum number of tokens in response

        Returns:
            AzureChatOpenAI: Configured LLM instance
        """
        return AzureChatOpenAI(
            azure_endpoint=self.endpoint,
            api_key=self.api_key,
            api_version=self.api_version,
            azure_deployment=self.deployment_name,
            temperature=temperature,
            max_tokens=max_tokens
        )


# Test the configuration
if __name__ == "__main__":
    try:
        config = AzureOpenAIConfig()
        llm = config.create_llm()
        print("✅ Azure OpenAI configuration successful!")
        print(f"Endpoint: {config.endpoint}")
        print(f"Deployment: {config.deployment_name}")
        print(f"API Version: {config.api_version}")

        # Test a simple call
        response = llm.invoke("Hello! This is a test message.")
        print(f"\n🧪 Test response: {response.content}")

    except Exception as e:
        print(f"❌ Configuration error: {e}")
        print("Please check your .env file and ensure all values are correct.")
