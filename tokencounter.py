import time
import os
import markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

class TokenCounter(Preprocessor):
    def run(self, lines):
        token_count = 0
        for line in lines:
            # Split line into tokens (words, punctuation, etc.)
            tokens = line.split()
            token_count += len(tokens)
        return token_count

def estimate_processing_time(token_count, processing_speed):
    # Assuming linear relationship between token count and processing time
    processing_time = token_count / processing_speed
    return processing_time

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()
    return markdown_content

def main():
    folder_path = r'C:\Users\andrew\Desktop\Python Projects\Paper Package Parser\Markdowns'
    # Read Markdown file
    for file_name in os.listdir(folder_path):
        file_path = f"{folder_path}\{file_name}"
        markdown_content = read_markdown_file(file_path)
        
        # Convert Markdown to HTML (optional)
        html_content = markdown.markdown(markdown_content)

        # Initialize token counter
        token_counter = TokenCounter()

        # Process Markdown content
        token_count = token_counter.run(markdown_content.splitlines())

        # Computer specifications
        processing_speed = 1000000  # Tokens processed per second (adjust based on your computer)

        # Estimate processing time
        processing_time = estimate_processing_time(token_count, processing_speed)
        print("Estimated processing time:", processing_time, "seconds   Token: ", token_count)

if __name__ == "__main__":
    main()
