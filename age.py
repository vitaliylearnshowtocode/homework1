user_age = int(input ("Сколько Вам лет?: "))

def activity(user_age):
    if user_age <= 6: 
        return "Вы учитесь в детском саду"
    elif 7 <= user_age <= 18:
        return "Вы учитесь в школе"
    elif 19 <= user_age <= 22:
        return "Вы учитесь в институте"
    else: 
        return "Вы работаете или на пенсии"
print(activity(user_age))