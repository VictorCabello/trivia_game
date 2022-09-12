import json, xml

def load_questions(fileloader, filename):
    f = open(fileloader(filename), "r")
    data = f.read()
    f.close()
    data = json.loads(data)
    return_value = []
    a_in_ascii = 97

    while data["results"]:
        result = data["results"].pop(0)
        ascii_value = a_in_ascii
        assessment_type = result['assessment_type']
        question = result['question_plain']
        explanation = result['prompt']['explanation']
        correct_response = result['correct_response']
        answers = []

        for x in result['prompt']['answers']:
            answers_prefix = chr(ascii_value)
            answers.append((answers_prefix + "." + x, answers_prefix))
            ascii_value += 1

        return_value.append({
            "assessment_type": assessment_type,
            "question": question,
            "explanation": explanation,
            "correct_response": correct_response,
            "answers": answers
        })

    return return_value
