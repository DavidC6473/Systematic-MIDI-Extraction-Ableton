# Systematic MIDI Extraction for Ableton Live

This project aims to automate the process of extracting MIDI files from multiple Ableton Live projects and converting audio files to MIDI. It provides a Python script that utilizes the `pylive` library to interact with Ableton Live and perform the MIDI extraction.

## Prerequisites

- Python 3.7 or higher
- Ableton Live installed on your system
- `pylive` library (included as a submodule in this repository)

## Installation

1. Clone this repository to your local machine: 
git clone https://github.com/DavidC6473/Systematic-MIDI-Extraction-Ableton.git

2. Navigate to the cloned repository: 
cd Systematic-MIDI-Extraction-Ableton

3. Install the required dependencies: 
pip install -r requirements.txt

4. Set up the `pylive` library as a submodule:
git submodule init
git submodule update

## Usage

1. Change "Path/To/Projects/Folder" in ableton_data_extraction.py to the path of the folder containing you projects.

2. Change "Path/To/Output/Folder" in ableton_data_extraction.py to the path to your desired output folder.

3. Run the script:
python ableton_data_extraction.py

The script will cycle through each project file, convert audio files to MIDI, and extract MIDI files from the projects. The resulting MIDI files will be saved in the `output` directory.

## Credits

- This project utilizes the `pylive` library (https://github.com/ideoforms/pylive) for interacting with Ableton Live programmatically. Many thanks to the contributors of `pylive`.
