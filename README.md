# 🔁 Undo-Redo Stack Visualization using Manim

A smooth animation demonstrating the **Undo-Redo stack mechanism** built with Manim library. Visualizes text edits with color-coded stacks and smooth transitions.

---

## ✨ Features
- Visual representation of **Undo** and **Redo** stacks  
- Smooth animations (fade, transform, color effects)  
- Supports operations: `append`, `undo`, `redo`  
- Customizable operation sequences  

---

## 🛠️ Tech Stack
- **Python 3.8+**  
- **Manim Community v0.19.0**  
- **FFmpeg** (for rendering)
- > ⚙️ Built using [Manim](https://github.com/ManimCommunity/manim) — originally developed by [3Blue1Brown](https://www.3blue1brown.com/)


---

## 🚀 Installation

### Prerequisites
1. Install Python 3.8+ from [python.org](https://www.python.org/downloads/)
2. Install FFmpeg:
   ```bash
   # MacOS
   brew install ffmpeg
   
   # Linux (Debian/Ubuntu)
   sudo apt install ffmpeg
   
   # Windows (via Chocolatey)
   choco install ffmpeg

3. Clone the repository:
```bash
git clone https://github.com/Shubham-0-0-7/undo_redo_visualization.git
```

4. Ensure Python 3.10+ is Installed
   Manim works best with Python 3.10 or later.
   Check your Python version:
```bash
   python3 --version #macOS
   python --version  #Windows
```
If it's lower than 3.10, update 

5. Create a virtual environment (Recommended)
   ```bash
   #macOS
   python3 -m venv manim-env
   source manim-env/bin/activate 
   ```
   ```bash
   # Windows
    python -m venv manim-env
    manim-env\Scripts\activate
   ```       
   Now your terminal prompt should change to show (manim-env).

6. Install Manim Community Edition
   ```bash
    pip install manim
   ```
Let it finish — it may take a few minutes based on your internet connection

7. Verify Installation
   ```bash
    manim --version
   ```
You should see something like: `Manim Community v0.19.0`

## ▶️ How to Run

Render the animation by running the following command in your terminal:

```bash
  manim -pql animate_stacks.py UndoRedoStackScene
```
`-pql` = preview, quick, low quality (for faster render while testing)
You can replace it with `-pqh` (high quality) or `-pqm` (medium quality) if needed.
💡 After rendering, a video player window should pop up showing the animation.
The output video file will also be saved inside the media/videos/ directory.

## 🧠 How It Works

- The animation file (`animate_stacks.py`) contains a class called `UndoRedoStackScene` that defines the scene using Manim.
- Text actions (`append`, `undo`, `redo`) are visually represented with stack movements and colored rectangles.
- Undo and Redo stacks grow/shrink as actions are performed, just like in a real editor.

---

## 🤝 Contributing

Feel free to fork this repo, suggest improvements, or add new features. Pull requests are welcome!

---

## ✨ Credits

This project uses the [Manim](https://github.com/ManimCommunity/manim) library, originally created by [Grant Sanderson (3Blue1Brown)](https://www.3blue1brown.com/).  
Huge thanks to the [Manim Community](https://www.manim.community/) for maintaining and evolving the tool!


