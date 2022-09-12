define e = Character(_('devi'), color="#c8ffc8")

label start:
    python:
        import trivia
        data = trivia.load_questions(
            renpy.loader.transfn,
            "./gcp_devops.json"
        )

    scene bg outside
    show devi happy
    e 'hola'

    while data:
        $ result = data.pop(0)
        $ assessment_type = result['assessment_type']
        $ question = result['question']
        $ explanation = result['explanation']
        $ correct_response = result['correct_response']
        $ answers = result['answers']

        if assessment_type == "multiple-choice":
            $ narrator(question, interact=False)
            $ result = renpy.display_menu(answers)
            if result in correct_response:
                show devi happy
                e 'correct !!!'
            else:
                show devi angry1
                e 'Incorrect !!!!'
            
            show devi happy
            e "[explanation]"

        else:
            $ narrator(question, interact=False)
            $ selected_answers = []
            $ try_conter = 0
            while try_conter < len(correct_response):
                $ result = renpy.display_menu(answers)
                $ try_conter += 1
                if result in correct_response:
                    show devi happy
                    e 'correct !!!'
                else:
                    show devi angry1
                    e 'Incorrect !!!!'
            show devi happy
            e "[explanation]"
