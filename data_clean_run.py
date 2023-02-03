from scripts.data.dataFrame_clean import clean_authors_works_dataFrame
from scripts.util.dir_path import DATA_CSV
from scripts.util.read_csv_ui import show_csv


def clean_dataFrame():
    print('\nПребробка набору даних для аналізу...')
    clean_authors_works_dataFrame()
    print('Готово')

def main():
    clean_dataFrame()
    show_csv(f'{DATA_CSV}/preprocessed_data.csv')

if __name__ == "__main__":
    main()