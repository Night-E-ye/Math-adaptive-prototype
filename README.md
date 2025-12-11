# 🧮 Math Adventures: Adaptive Learning Prototype

Math Adventures is a lightweight, AI-inspired educational prototype designed to help children (ages 5–10) practice arithmetic. It features a rule-based Adaptive Engine that adjusts difficulty dynamically based on immediate performance heuristics.

## 📂 Project Structure

The project follows a modular architecture to separate concerns between logic, data tracking, and user interaction.

```
math-adaptive-prototype/
│
├── README.md               # Project documentation
├── requirements.txt        # Dependencies (uses Python standard library)
└── src/
    ├── main.py             # Entry point (controller)
    ├── puzzle_generator.py # Generates dynamic math problems
    ├── tracker.py          # Logs performance data & metrics
    └── adaptive_engine.py  # Logic for difficulty adjustment
```

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- No external libraries required (uses Python standard library)

### Installation & Execution
1. Clone or download this repository.
2. Open a terminal and change into the src directory:

```bash
cd math-adaptive-prototype/src
```

3. Run the application:

```bash
python main.py
```

## 🧠 How the Adaptive Logic Works

The core of this prototype is a rule-based Adaptive Engine (`adaptive_engine.py`). It addresses the "cold start" problem by relying on immediate heuristics (accuracy and response time) rather than pre-trained data.

### Difficulty Levels
- **Easy**: Single-digit addition and subtraction
- **Medium**: Double-digit operations and multiplication
- **Hard**: Mixed operations including division

### Adaptation Rules
The system evaluates two metrics: **Accuracy** and **Time Taken**.

1. Upgrade Mechanism (Promotion)
   - Trigger: 3 consecutive correct answers promote the user to the next level.
   - Speed Bonus: If an answer is provided in under 8 seconds, it counts as double towards the streak (accelerates promotion for fluent learners).

2. Downgrade Mechanism (Remediation)
   - Trigger: Any incorrect answer.
   - Action: Immediate streak reset. If the current level is Medium or Hard, the difficulty drops one level to rebuild confidence.

## 📊 Features
- **Dynamic Content Generation**: Puzzles are generated algorithmically, allowing for infinite practice.
- **Performance Tracking**: Records time-per-question and session accuracy.
- **Session Summary**: Provides a statistical report at the end of each learning session.

## 🔮 Future Improvements (ML Integration)
The architecture supports easy integration of Machine Learning:
- Data collected by `tracker.py` can be used to train predictive models (e.g., logistic regression) later.
- Future versions could replace if/else rules in `adaptive_engine.py` with a model that predicts user performance or churn risk and adapts questions more precisely.



