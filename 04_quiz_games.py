#https://youtu.be/4TZ1K8EHT2M?t=107

questions=[

 {'prompt': 'What is 7 + 5?' ,
 'options': ['A. 10', 'B. 12', 'C. 13', 'D. 14' ],
  'Answer': 'B',
    },

{ 'prompt': 'Which part of a plant makes food?' ,
 'options': ['A. Root', 'B. Stem', 'C. Leaf', 'D. Flower' ],
 'Answer': 'C' },

{ 'prompt': 'Which of these is a continent?' ,
 'options': ['A. Sahara', 'B. Europe', 'C. Amazon', 'D. Pacific'],
   'Answer': 'B' },

{ 'prompt': 'Who was the first President of the United States?',
  'options': ['A. Abraham Lincoln', 'B. George Washington', 'C. Thomas Jefferson', 'D. Benjamin Franklin' ],
  'Answer': 'B' },

{ 'prompt': 'Which word is a noun?',
  'options': ['A. Run', 'B. Quickly', 'C. Happiness', 'D. Blue'],
    'Answer': 'C' },

    
]

def run_quiz(questions):
    score=0
    for question in questions:
        print(question['prompt'])
        for option in question['options']:
            print(option)
        answer= input('Enter your answer (A, B, C, or D): ').upper()
        
        #answerUp=answer.upper()
        print(answer)
        if answer== question['Answer']:
            print('Correct!')
            score+=1
        else:
            print('Incorrect, the correct answer is, ', question['Answer'])
    print(f'You got {score} out of {len(questions)} questions correct')

run_quiz(questions)