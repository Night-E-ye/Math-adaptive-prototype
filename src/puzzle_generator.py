import random

class PuzzleGenerator:
    def __init__(self):
        self.levels = {
            'Easy': {'ops': ['+', '-'], 'range': (1, 10)},
            'Medium': {'ops': ['+', '-', '*'], 'range': (5, 20)},
            'Hard': {'ops': ['+', '-', '*', '/'], 'range': (10, 50)}
        }

    def generate_puzzle(self, difficulty):
        config = self.levels.get(difficulty, self.levels['Easy'])
        operation = random.choice(config['ops'])
        
        # Logic to ensure clean numbers (no negative results for kids, integer division)
        if operation == '/':
            num2 = random.randint(2, 10) # Divisor
            result = random.randint(1, 10) # Quotient
            num1 = num2 * result # Dividend
        else:
            num1 = random.randint(*config['range'])
            num2 = random.randint(*config['range'])
            
            # Ensure no negative results for subtraction
            if operation == '-' and num1 < num2:
                num1, num2 = num2, num1

        question_str = f"{num1} {operation} {num2}"
        answer = eval(question_str) # Safe to use eval here as we control inputs
        
        return {
            "question": question_str,
            "answer": int(answer), # Ensure integer for comparison
            "difficulty": difficulty
        }