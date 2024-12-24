import os
from pydub import AudioSegment

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Input and output file paths
input_file = os.path.join(script_dir, "hohoho.mp3")
output_file = os.path.join(script_dir, "output_first_second.mp3")

try:
    # Load the MP3 file
    audio = AudioSegment.from_file(input_file, format="mp3")
    
    # Extract the first second
    first_second = audio[:1500]  # Duration in milliseconds
    
    # Save the extracted segment to a new file
    first_second.export(output_file, format="mp3")
    
    print(f"First second extracted and saved to {output_file}")
except FileNotFoundError:
    print(f"Error: {input_file} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
