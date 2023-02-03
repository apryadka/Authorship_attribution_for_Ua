import glob
import docx


def read_file(path):
    with open(path, encoding="utf-8") as fp:
        return fp.readlines()


def read_data_docx(path='Data'):
    text = []
    for path in glob.glob(f'{path}/*.docx'):
        doc = docx.Document(path)
        for p in doc.paragraphs:
            text.append(p.text)
    return text


def save_data_txt(data, path):
    with open(path, 'w', encoding="utf-8") as fp:
        for item in data:
            if(len(item.split(' ')) > 2):
                fp.write("%s\n" %item)
        print(f'Data saved to file {path}')
