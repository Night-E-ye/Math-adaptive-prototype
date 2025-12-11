from puzzle_generator import PuzzleGenerator
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine

def main():
    print("Welcome to Math Adventures! 🧮")
    print("---------------------------------")
    
    # Initialize components
    generator = PuzzleGenerator()
    tracker = PerformanceTracker()
    engine = AdaptiveEngine()
    
    # Session Loop (e.g., 5 questions for the demo)
    total_questions = 5
    
    for i in range(total_questions):
        current_diff = engine.get_current_difficulty()
        print(f"\nQuestion {i+1} [{current_diff} Level]")
        
        # 1. Generate
        puzzle = generator.generate_puzzle(current_diff)
        print(f"Solve: {puzzle['question']} = ?")
        
        # 2. Input & Timing
        tracker.start_timer()
        try:
            user_input = int(input("Your Answer: "))
        except ValueError:
            print("Please enter a number.")
            user_input = 0 # Treat invalid input as incorrect
            
        time_taken = tracker.stop_timer()
        
        # 3. Check Correctness
        is_correct = (user_input == puzzle['answer'])
        if is_correct:
            print(f"✅ Correct! ({time_taken}s)")
        else:
            print(f"❌ Incorrect. The answer was {puzzle['answer']}.")
            
        # 4. Log Data
        tracker.log_attempt(puzzle, user_input, is_correct, time_taken)
        
        # 5. Adapt
        feedback = engine.update_difficulty(is_correct, time_taken)
        print(f"System: {feedback}")

    # End Session
    print("\n--- Session Summary ---")
    summary = tracker.get_summary()
    for key, value in summary.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()