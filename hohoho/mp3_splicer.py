import os
from pydub import AudioSegment

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Input and output file paths
input_file = os.path.join(script_dir, "hohoho_v2.mp3")
output_file = os.path.join(script_dir, "output_clipped.mp3")

# Specify the range to keep (in seconds)
start_second = 4  # Start of the range (inclusive)
end_second = 5.36    # End of the range (exclusive)

try:
    # Load the MP3 file
    audio = AudioSegment.from_file(input_file, format="mp3")
    
    # Calculate the range in milliseconds
    start_ms = start_second * 1000
    end_ms = end_second * 1000

    # Extract the specified range
    clipped_audio = audio[start_ms:end_ms]
    
    # Save the clipped segment to a new file
    clipped_audio.export(output_file, format="mp3")
    
    print(f"Audio from {start_second}s to {end_second}s extracted and saved to {output_file}")
except FileNotFoundError:
    print(f"Error: {input_file} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
