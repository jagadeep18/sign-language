# Indian Sign Language Recognition

## Overview
This project is an **Indian Sign Language (ISL) Recognition System** that translates speech into sign language. The application uses **Tkinter** for the GUI, **SQLite** for storing user data, and **PIL** for handling images. It also integrates various modules for dataset creation, sign prediction, and reverse recognition.

## Features
- **Speech to Sign Language Translation**
- **Animated GIF Support** for better visualization
- **Database Integration** using SQLite
- **Interactive GUI** with Tkinter
- **Indian Flag Themed UI**

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required libraries:
  ```sh
  pip install tkinter pillow sqlite3
  ```

### Clone the Repository
```sh
git clone https://github.com/jagadeep18/sign-language.git
cd sign-language/Code/Predict\ signs
```

## Running the Application
Execute the following command to start the ISL Translator:
```sh
python main.py
```

## Project Structure
```
Indian-Sign-Language-Recognition/
│-- Code/
│   ├── creating_dataset.py    # Handles dataset creation
│   ├── Prediction.py          # Sign language prediction module
│   ├── Reverse_Recognition.py # Speech-to-sign translation
│   ├── main.py                # Main GUI application
│   ├── files/
│   │   ├── users_info.db      # SQLite database
│   │   ├── flag.png           # Background image
│   │   ├── gif2.gif           # Animated sign language GIF
```

## Usage
1. **Translate Speech to Sign Language**
   - Click on the **"Translate Speech"** button.
   - The application will recognize speech and display the corresponding sign language gestures.

2. **Exit Application**
   - Click on the **"Exit"** button to close the application.

## Output
![image](https://github.com/user-attachments/assets/a63db659-50d6-4981-96b4-d76cbf26bb95)


## Author
Developed by **Jagadeep Gorantla**

