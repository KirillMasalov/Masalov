from DataSet_class import DataSet
from Report_class import Report
from Table_statistics import TableStatistics


if __name__ == "__main__":
    userQuery = input("Введите команду: (Вакансии / Статистика)")
    if userQuery == "Вакансии":
        TableStatistics.start_table_programm()
    elif userQuery == "Статистика":
        folder_name = input("Введите название папки: ")
        file_name = input("Введите название файла: ")
        current_vacancy_name = input("Введите название профессии: ")

        data_set = DataSet(current_vacancy_name)
        file_names = data_set.csv_split_generator(file_name, folder_name)
        data_set.generate_currency()
    else:
        print("Неизвестная команда. Введите 'Вакансии' или 'Статистика'")
