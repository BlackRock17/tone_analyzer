from pydantic import BaseModel, Field
from typing import Literal


class ToneAnalysisResult(BaseModel):
    """
    Structured output model for tone analysis results.
    This model ensures consistent output format from the LLM.
    """

    tone: Literal["positive", "negative", "neutral"] = Field(
        description="The overall tone of the text"
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Confidence score between 0.0 and 1.0"
    )

    explanation: str = Field(
        min_length=10,
        max_length=500,
        description="Detailed explanation of why this tone was detected"
    )

    key_phrases: list[str] = Field(
        description="Important phrases that influenced the tone analysis"
    )


# Example usage and testing
if __name__ == "__main__":
    # Test the model with sample data
    sample_result = ToneAnalysisResult(
        tone="positive",
        confidence=0.85,
        explanation="The text contains optimistic language and positive sentiment indicators.",
        key_phrases=["great job", "excellent work", "very happy"]
    )

    print("Sample model output:")
    print(sample_result.model_dump_json(indent=2))
