"""Create a Question class with an __init()__ method with two
attributes: text and answer attributes"""

class Question:
    
    def __init__(self, q_text, q_answer):
        self.question = q_text
        self.answer = q_answer

# nrw_q = Question("Naufal", "False")
# print(nrw_q.answer)
