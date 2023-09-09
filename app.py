from Perplexity import Perplexity
from Answer import Answer

def main():
    # Create an instance of the Perplexity class
    perplexity_instance = Perplexity()

    try:
        #Perform a search
        query = "What is the capital of France?"
        answer = perplexity_instance.search(query)

        # Display the answer
        print("Answer:")
        print("UUID:", answer.uuid)
        print("Text:", answer.text)
        print("Search Focus:", answer.search_focus)
        print("Related Queries:", answer.related_queries)

        # Ask for more details about the answer
        detailed_answer = perplexity_instance.ask_detailed()

        # Display detailed information
        print("\nDetailed Answer:")
        print("UUID:", detailed_answer.uuid)
        print("Text:", detailed_answer.text)

    finally:
        # Close the WebSocket connection when done
        perplexity_instance.close()

if __name__ == "__main__":
    main()
