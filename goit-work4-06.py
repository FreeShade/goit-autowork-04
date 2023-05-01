def split_list(lst):
    if not lst:  # Якщо список порожній, повертаємо два порожніх списки
        return [], []

    avg = sum(lst) / len(lst)  # Знаходимо середнє значення

    lower = [
        num for num in lst if num <= avg
    ]  # Створюємо список елементів, менших або дорівнюють середньому
    higher = [
        num for num in lst if num > avg
    ]  # Створюємо список елементів, більших за середнє

    return lower, higher  # Повертаємо кортеж з двома списками
