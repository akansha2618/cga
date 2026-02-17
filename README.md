# Space-Escape-Retro-Rocket-Game-CGA-
A 2D retro arcade-style space shooter built using Python and Pygame featuring real-time collision detection and dynamic enemy spawning.
# 🚀 Space Escape – Retro Rocket Game

A 2D arcade-style space shooter built using Python and Pygame.

This project recreates the classic old-school arcade experience where the player controls a rocket and survives waves of falling enemies.

---

## 🎮 Game Overview

In Space Escape, the player pilots a rocket and must dodge or destroy incoming asteroids.

The game features:

- Smooth left-right rocket movement
- Real-time bullet shooting
- Dynamic enemy spawning
- Accurate collision detection
- Live score tracking
- 60 FPS smooth animation loop
- Restart functionality

The goal is simple — survive as long as possible and score maximum points.

---

## 🛠 Technologies Used

- Python (Core Logic)
- Pygame (Graphics & Game Engine)
- Random Library (Enemy Spawning)
- Math Library (Collision Detection)

---

## 🧠 Concepts Applied

- 2D Coordinate System
- Frame-Based Game Loop Architecture
- Event Handling
- Object Management using Lists
- Real-Time Collision Detection using Distance Formula
- FPS Control using Clock

---

## 🔄 Game Loop Architecture

Game Loop →
Input → Update → Collision → Render → Repeat

The game continuously:
1. Captures user input
2. Updates object positions
3. Detects collisions
4. Renders graphics
5. Refreshes the screen at 60 FPS

---

## 💥 Collision Logic

Collision detection is implemented using the distance formula:

distance = √((x1 - x2)² + (y1 - y2)²)

If the distance between objects is less than a defined threshold, a collision is triggered.

---

## 📊 Performance

- Runs at stable 60 FPS using clock control
- Efficient list-based object management
- Simple and optimized logic for smooth gameplay

---

## 🚀 Future Improvements

- Sound effects
- Multiple levels
- Boss enemies
- Power-ups
- Animated backgrounds
- OOP-based scalable architecture

---

## 🎯 Learning Outcome

This project demonstrates how fundamental computer graphics and game logic concepts can be used to build a fully interactive system.

It converts theoretical knowledge into a real-time playable experience.

---

## 🖥️ How to Run

1. Install Python
2. Install Pygame:
   pip install pygame
3. Run the script:
   python main.py

---

## 👨‍💻 Author

Bhavesh Salaskar  
FY BSc IT – Computer Graphics Project

---

⭐ If you like the project, feel free to fork and improve it!
