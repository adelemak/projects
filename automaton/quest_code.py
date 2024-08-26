import json


# Считываем JSON файл и достаем оттуда данные в виде словаря
def get_data(input_file):
    with open(input_file, "r") as file:
        quest = json.load(file)
    return quest


# Реализация процесса квеста
def play_quest(quest):

    # Создаем переменную текущего состояния
    current_state = "start"

    # Создаем стек, куда будем класть текущее сотсояние,
    # чтобы иметь возможность откатывать выбор назад
    state_stack = []

    # Цикл игры
    while True:
        state = quest[current_state]  # Кладем в переменную текущее состояние (один item словаря)
        print(state["text"])

        # Если состояние конечное (нет опций переходов) -> останавливаем цикл
        if "options" not in state or not state["options"]:
            break

        choice = input("Введите ваш выбор (или введите 'назад' для возврата): ").strip()  # Выбор пользователя

        # Достаем последнее состояние из стека, если ввели 'назад'
        if choice.lower() == "назад" and state_stack:
            current_state = state_stack.pop()
        # Если ввод есть в переходах, добавляем текущее сотсояние в стек и меняем его в соотвествиии с выбором
        elif choice in state["options"]:
            state_stack.append(current_state)
            current_state = state["options"][choice]
        else:
            print("Команда не распознана. Повторите ввод.")


# Основная функция запуска квеста
def main():
    quest_file = "quest.json"
    quest = get_data(quest_file)
    play_quest(quest)

    # Предложение попробовать еще раз после окончания игры
    while True:
        choice = input("Введите 1, если хотите пройти квест еще раз, или 2 для завершения: ").strip()
        if choice == "1":
            play_quest(quest)
        elif choice == "2":
            print("Спасибо за игру! До новых встреч!")
            break
        else:
            print("Команда не распознана. Повторите ввод.")


# Запуск основной функции
main()
