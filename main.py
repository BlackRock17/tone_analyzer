from tone_analyzer import ToneAnalyzer


def main():
    """Simple tone analyzer - just enter text and get results."""
    print("🎯 Simple Tone Analyzer")
    print("=" * 30)
    print("Enter text to analyze (or 'quit' to exit)")

    # Create analyzer instance once
    analyzer = ToneAnalyzer()

    while True:
        print("\n" + "-" * 30)

        # Get text input from user
        user_text = input("📝 Enter your text: ").strip()

        # Check if user wants to quit
        if user_text.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break

        # Check if text is empty
        if not user_text:
            print("⚠️  Please enter some text to analyze.")
            continue

        # Analyze the text
        try:
            print("\n🔍 Analyzing...")
            result = analyzer.analyze_tone(user_text)

            # Display results
            print(f"\n📊 Results:")
            print(f"   Tone: {result.tone.upper()}")
            print(f"   Confidence: {result.confidence:.1%}")
            print(f"   Explanation: {result.explanation}")
            print(f"   Key Phrases: {', '.join(result.key_phrases)}")

        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try again with different text.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Interrupted by user. Goodbye!")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
