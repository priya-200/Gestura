## Project Name

**Gestura: Hand Gesture Control System** ✋🤖  
A small initiative to learn OpenCV, MediaPipe, and PyAutoGUI to control the mouse, perform scrolling, zooming, clicking, and dragging actions using hand gestures. 🤳💻

## Features

### Use the following gestures to control the system:

- **Cursor Movement**: Move your hand to control the mouse. 🖱️✋
- **Scrolling**: Use your fingers to scroll up or down. ⬆️⬇️
- **Zooming**: Perform pinch gestures to zoom in or out. 🔍👐
- **Clicking**: Perform left-click, right-click, or double-click using specific hand gestures. 🖱️👆👈
- **Dragging**: Hold all fingers down to simulate a drag action. 👇🖱️

## How It Works

1. **Hand Detection**: The system uses the MediaPipe library to detect and track hand landmarks. 👀✋
2. **Gesture Recognition**: Various hand gestures are recognized based on the relative positions of the hand landmarks. 🤲
3. **Action Mapping**: These gestures are mapped to corresponding actions such as moving the cursor, scrolling, zooming, clicking, or dragging using the PyAutoGUI library. 🔄

## Installation

Follow these steps to set up the project:

1. Clone the repository:

    ```bash
    git clone https://github.com/priya-200/gestura.git
    cd gestura
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    Or install the dependencies manually:

    ```bash
    pip install opencv-python mediapipe pyautogui
    ```

## Usage

1. Run the application:

    ```bash
    python app.py
    ```

2. Perform the hand gestures mentioned above to control your system. 🖱️🤳
3. To exit, press the 'q' key. 🚪

## Acknowledgements

- **OpenCV**: Open-source computer vision library. 📸
- **MediaPipe**: Google’s cross-platform framework for building pipelines to process video, audio, and other multimedia types. 🎥
- **PyAutoGUI**: A Python library for GUI automation, including mouse and keyboard control. ⌨️

---

Feel free to contribute and improve the project! ✨🚀
