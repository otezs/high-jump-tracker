# High Jump Training Tracker

A Python terminal application built to help high jump athletes log their training sessions, track progress over time, and see their stats at a glance. No heavy graphics or complex interfaces—just a quick, efficient way to manage your training data right from your command line.

## 🚀 Features

* **Log Management:** Easily add new jump heights (in meters) or delete accidental entries from your log.
* **Training History:** View your entire history of jumps with dates to see how your consistency changes over time.
* **Performance Analytics:** Instantly calculate your career average jump height and display your lifetime Personal Best (PB), including the exact date it was achieved.
* **Goal Tracking:** Set a target height goal and check how close you are to clearing it.
* **Persistent Storage:** Automatically saves your data to a `high-jump-log.json` file when you exit, allowing you to pick up right where you left off next time you train.

## 📦 Data Structure

The app uses an internal dictionary to track data by mapping jump metrics to chronological entries:
* `height`: A list of all recorded jumps in meters.
* `date`: A parallel list marking when each jump was recorded.

## 🛠️ How to Run

1. Make sure you have Python 3 installed on your machine.
2. Clone or download this repository into your project directory.
3. Open your terminal and navigate to the project folder:
   ```bash
   cd path/to/high-jump-tracker

