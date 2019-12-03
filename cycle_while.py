qa = {"Как дела?": "Хорошо", "Что делаешь?": "Программирую", "Где ты живешь?": "В Москве"}

user_question = input("Спроси что-нибудь: ")
prog_answer = qa.get(user_question)

if prog_answer is None:
    print("Пока! Приятно было поболтать")
    exit(0)

print(prog_answer)

while True:
    
    user_question = input('Спроси что-нибудь еще: ')
    prog_answer = qa.get(user_question)
       
    if prog_answer is None:
        print("Пока! Приятно было поболтать")
        break
        
    print(prog_answer)



 
