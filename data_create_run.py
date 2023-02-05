from scripts.data.dataFrame_create import create_authors_works_files, create_authors_works_dataFrame
from scripts.util.dir_path import DATA_CSV
from scripts.util.read_csv_ui import show_csv


def create_dataFrame():
    print('Створення файлу даних...')
    create_authors_works_files()
    print('\nСтворення набору даних для аналізу...')
    create_authors_works_dataFrame(3000)
    print('Готово')

def main():
    create_dataFrame()
    show_csv(f'{DATA_CSV}/author_data.csv')

if __name__ == "__main__":
    main()