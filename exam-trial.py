# - [Core Concepts - 13%](a.core_concepts.md)
# - [Multi-container pods - 10%](b.multi_container_pods.md)
# - [Pod design - 20%](c.pod_design.md)
# - [Configuration - 18%](d.configuration.md)
# - [Observability - 18%](e.observability.md)
# - [Services and networking - 13%](f.services.md)
# - [State persistence - 8%](g.state.md)
import os
import random
import ast

def read_questions(file:str):
    return os.popen(f"cat {file} | grep '### '").readlines()
exam_composition = [{
        "name": 'a.core_concepts.md',
        "percentage": 13
    },{
        "name": 'b.multi_container_pods.md',
        "percentage": 10
    },{
        "name": 'c.pod_design.md',
        "percentage": 20
    },{
        "name": 'd.configuration.md',
        "percentage": 18
    },{
        "name": 'e.observability.md',
        "percentage": 18
    },{
        "name": 'f.services.md',
        "percentage": 13
    },{
        "name": 'g.state.md',
        "percentage": 8
    }
]

def choose_random_questions(exam_composition, total, random_questions=set()):
    for concept in exam_composition:
        name = concept['name']
        questions = read_questions(name)
        size_questions = int((concept['percentage']/100)*total)
        # The ammount that will be tried on each concepts
        x_times = 3

        while size_questions != 0 and len(random_questions) < total and x_times != 0:
            size_before = len(random_questions)
            selected_question = random.sample(questions, 1)[0]
            random_questions.add(f"{name} {selected_question}")
            size_after = len(random_questions)
            # when select a question that is not selected it decrease by one.
            size_questions = size_questions - (len(random_questions) - size_before)
            # when the question is equals that a one already selected
            if (size_after == size_before):
                x_times = x_times - 1

        if len(random_questions) >= total:
            return random_questions

    return choose_random_questions(exam_composition, total, random_questions)

def create_exam():
    total = int(input("how many questions (20-30): "))

    return choose_random_questions(exam_composition, total)

questions = create_exam()

print()
for index, question in enumerate(questions, start=1):
    fp, q = question.split(" ### ")
    print(f"{index} - {fp}")
    print(q)


# TO RUN ON COMMAND LINE AND CREATE A FILE:
# $ echo 20 | /usr/bin/python3.8 ./exam-trial.py > exam-1.txt
