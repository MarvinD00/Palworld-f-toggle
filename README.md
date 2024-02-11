Description
Toggle GUI is a simple Python program with a graphical user interface (GUI) that allows users to set start and stop keys for toggling a virtual key press. 
It uses the pynput library to detect key presses and simulate holding the 'f' key. The program is designed to be user-friendly, allowing users to set start and stop keys easily.

Installation
First you will have to clone the repo or download the .zip.

You will also need python3 which you can download from here : [python.org](https://www.python.org/downloads/).

After you have downloaded the repo you can run one of the dependency scripts that will automatically install dependencies using pip.

For Linux/macOS: Run install_dependencies.sh
For Windows: Run install_dependencies_win.bat

Running the Program
Open a terminal or command prompt and run the main program:
cd /your/path/to/program-folder/
python3 gui.py

How to Use
The GUI window will appear with fields to set the start and stop keys.
Click on the "Set start key" and "Set stop key" buttons to set the respective keys. Follow the on-screen instructions to press the desired keys.
Once both keys are set, you can click the "Start Toggle" button to begin the toggle functionality.
After pressing the configures start key, the program will continually hold the 'f' key for you until you press the configured stop key.
Click the "Stop Toggle" button to stop the toggle functionality.
Note: Ensure that both start and stop keys are set before starting the toggle.

Troubleshooting
If you encounter any issues during the key setup process, carefully follow the on-screen instructions and error messages.
Make sure the dependencies are installed correctly by running the respective installation script.
If you face difficulties, feel free to create an issue on the GitHub repository for assistance.

Contribution
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or create a pull request.

License
This project is licensed under the MIT License.
