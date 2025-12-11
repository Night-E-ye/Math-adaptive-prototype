import time

class PerformanceTracker:
    def __init__(self):
        self.session_data = []
        self.start_time = None

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        if self.start_time:
            return round(time.time() - self.start_time, 2)
        return 0

    def log_attempt(self, puzzle, user_answer, is_correct, time_taken):
        record = {
            "difficulty": puzzle['difficulty'],
            "question": puzzle['question'],
            "correct_answer": puzzle['answer'],
            "user_answer": user_answer,
            "is_correct": is_correct,
            "time_taken": time_taken
        }
        self.session_data.append(record)
        return record

    def get_summary(self):
        total = len(self.session_data)
        if total == 0:
            return "No data recorded."
        
        correct_count = sum(1 for r in self.session_data if r['is_correct'])
        accuracy = (correct_count / total) * 100
        avg_time = sum(r['time_taken'] for r in self.session_data) / total
        
        return {
            "total_questions": total,
            "accuracy": f"{accuracy:.1f}%",
            "average_time_sec": f"{avg_time:.1f}"
        }