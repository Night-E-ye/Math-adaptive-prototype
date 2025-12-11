class AdaptiveEngine:
    def __init__(self):
        self.levels = ['Easy', 'Medium', 'Hard']
        self.current_level_index = 0  # Start at Easy (index 0)
        self.consecutive_correct = 0
        self.consecutive_slow = 0

    def update_difficulty(self, is_correct, time_taken):
        """
        Decides the next difficulty based on the last attempt.
        Returns: The new difficulty string (e.g., 'Medium')
        """
        
        # Rule 1: Incorrect answer immediately resets streak and may lower difficulty
        if not is_correct:
            self.consecutive_correct = 0
            # If user fails at Hard or Medium, downgrade
            if self.current_level_index > 0:
                self.current_level_index -= 1
                return f"⬇️  Too hard? Let's try {self.levels[self.current_level_index]}."
            return "Keep trying at Easy!"

        # Rule 2: Correct answer checks for speed and consistency
        if is_correct:
            self.consecutive_correct += 1
            
            # Fast response bonus
            if time_taken < 8: 
                self.consecutive_correct += 1 # Bonus point for speed

            # Check for Upgrade
            if self.consecutive_correct >= 3:
                if self.current_level_index < len(self.levels) - 1:
                    self.current_level_index += 1
                    self.consecutive_correct = 0 # Reset streak after promotion
                    return f"⬆️  Great job! Moving up to {self.levels[self.current_level_index]}!"
        
        return "Steady progress..."

    def get_current_difficulty(self):
        return self.levels[self.current_level_index]