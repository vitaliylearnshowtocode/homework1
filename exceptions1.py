while True:
    try:
        user_question = input('Спроси что-нибудь: ')
        qa = {"Как дела?": "Хорошо", "Что делаешь?": "Программирую", "Где ты живешь?": "В Москве"}
        prog_answer = qa.get(user_question)
        
        if prog_answer is None:
            print("Пока! Приятно было поболтать")
            break
        print(prog_answer)

    except KeyboardInterrupt:
        print("\nПока")
        break
    