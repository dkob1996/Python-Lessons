# На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
# Первый список ваш лотерейный билет.
# Второй список содержит список чисел, которые выпали в лотерею.
# Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.

# Напишите класс LotteryGame, который будет иметь метод compare_lists,
# который будет сравнивать числа из вашего билета из list1 со списком выпавших чисел list2


import logging
import argparse



class LotteryGame:
    """
    Класс отвечающий за создание экземпляра игры
    """
    def __init__(self, user_list, dropped_nums) -> None:
        self.user_list = user_list
        self.dropped_nums = dropped_nums

    def compare_lists(self):
        """
        Функция для проверки совпадения чисел в выпавших числах и числах пользователя
        """
        result_list = []
        for i in self.dropped_nums:
            if i in self.user_list:
                result_list.append(i)
        return f"Совпадающие числа: {result_list}\nКоличество совпадающих чисел: {len(result_list)}"

def parser():
    """
    Парсер агрумента (список пользовтельских чисел)
    :return:
    """
    parcer = argparse.ArgumentParser()
    parcer.add_argument("-u", "--userlist", default=[1,1,1,1,1,1,1,1,1,1])
    args = parcer.parse_args()

    return args.userlist

FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(level=logging.INFO, filename="lottery_logs.log", filemode="a",
                    format= FORMAT, encoding="utf-8")


dropped_nums = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
droppedlist_len = len(dropped_nums)

try:

    user_list = parser()
    if not isinstance(user_list, list):
        user_list = list(map(int, user_list.split(",")))

    logging.info(f"Получены числа {user_list}")
    userlist_len = len(user_list)
    if userlist_len == droppedlist_len:
        game = LotteryGame(user_list,dropped_nums)
        matching_numbers = game.compare_lists()
        logging.info(f"Совпавшие номера - {matching_numbers}")
    else:
        logging.error(f"Введено невалидное количество чисел {userlist_len} вместо {droppedlist_len}")

except ValueError:
    logging.error(f"Некорректный ввод, пожалуйста введите только цифры! ")
