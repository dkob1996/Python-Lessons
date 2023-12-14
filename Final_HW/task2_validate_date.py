"""
Программа проверяющая валидность даты
"""
import datetime
import logging
import argparse

FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(level=logging.INFO, filename="logs_date_validate.log", filemode="a",
                    format= FORMAT, encoding="utf-8")
def parcer():
    """
    Парсер аргументов (день, месяц, год) в отсутствие одного из параметров устанавливается значение текущего дня,месяца
    или года соответственно.
    :return:
    """
    parcer = argparse.ArgumentParser()
    parcer.add_argument("-d", "--date", default=datetime.datetime.now().day)
    parcer.add_argument("-m", "--month", default=datetime.datetime.now().month)
    parcer.add_argument("-y", "--year", default=datetime.datetime.now().year)
    args = parcer.parse_args()
    args_list = [int(args.date), int(args.month),int(args.year)]

    return args_list

def is_leap(year: int) -> bool:
    """
    Фуекция проверки года на високосность
    :param year:
    :return:
    """
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)
def is_valid_date(date,month,year) -> bool:
    """
    Функция проверки даты на валидность. Доступен год от 1 до 9999
    :param date:
    :param month:
    :param year:
    :return:
    """


    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return logging.warning("Невалидная дата")
    if month in (4, 6, 9, 11) and date > 30:
        return logging.warning("Невалидный день, в апреле, июне, сентябре и ноябре не может быть более 30 дней")
    if month == 2 and is_leap(year) and date > 29:
        return logging.warning("Невалидный день, в  феврале високосного года не может быть более 29 дней ")
    if month == 2 and not is_leap(year) and date > 28:
        return logging.warning("Невалидный день, в  феврале не високосного не может быть более 28 дней ")
    return logging.info("Дата валидная")
  
try:
    logging.info(f"Принята дата {'.'.join(map(str, parcer()))}")
    is_valid_date(*parcer())


except ValueError:
    logging.error("Невалидные данные")
