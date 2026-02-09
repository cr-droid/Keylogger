# KeyLogger (Educational Project)

## 📌 Project Description
I built a keylogger that captures and saves keyboard strokes and mouse clicks. For **LEGAL REASONS** and following **GITHUB POLICIES**, I did **NOT** upload any source code nor any pseudocode. Keyloggers can be considered spyware and are not allowed on GitHub per their policies. This repo is just to educate people on keyloggers and how they work. 

This program is an **event-driven Python application** that captures keyboard and mouse input while displaying a graphical user interface (GUI). It logs raw input events with timestamps and also organizes typed keystrokes into readable text output. The project is intended for **educational and learning purposes**, such as understanding event listeners, GUI integration, logging systems, and input handling.

The application runs a Tkinter-based UI and uses global input listeners to monitor keyboard and mouse activity while the program is active. I created a fake Facebook page to demonstrate how a keylogger works in a real setting.

---

## 🛠 Features

- Global keyboard and mouse input monitoring
- Timestamped logging of raw input events
- Organized reconstruction of typed text (handles space, backspace, and enter)
- Graphical user interface built with Tkinter
- Graceful shutdown with safe data flushing

---

## 🧩 Project Structure

- main.py # Application entry point and orchestration
- ... [redacted modules]
- logs.txt # Raw input log output
- organized_keys.txt # Organized keystroke output

---

## 🧠 How It Works (High-Level)

1. The program initializes necessary objects and listeners.
2. Each input event is timestamped and logged.
3. Keyboard input is additionally processed into readable text sequences.
4. Logs are written to disk using buffered appending.
5. On program exit, all remaining data is safely flushed and listeners are stopped.

---

## ⚙️ Usage Notes

- The program only records input **while it is running**.
- Logged data is stored locally in plain text files.
- This project should be used **only in environments where you have permission to monitor input**.
- Do not use keylogger software to capture sensitive data from others without consent.

---

## 🚨🚨🚨🚨 Disclaimer 🚨🚨🚨🚨

This project is intended for **educational and experimental purposes only**. Monitoring keyboard and mouse input can have legal and ethical implications. Always ensure you have proper authorization and follow applicable laws and platform policies.

---

## 🧪 Exhibit

---

## 👤 Author
- **Christian Ruiz**  
  Digital Forensics Student  
  GitHub: https://github.com/cr-droid
