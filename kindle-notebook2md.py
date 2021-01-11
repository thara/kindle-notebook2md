import sys
from bs4 import BeautifulSoup


def main():
    filepath = sys.argv[1]

    with open(filepath) as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        book_title = soup.find('div', class_='bookTitle').text.strip()
        print(f"## {book_title}")

        book_authors = soup.find('div', class_='authors').text.strip()
        print(f"Authors: {book_authors}")

        sections = [s.text for s in soup.find('body').find_all('h2')]

        all_texts = soup.find('body').find_all(text=True)
        lines = list(filter(len, map(str.strip, all_texts)))
        notebook = lines[lines.index(book_authors)+1:]

        section_idx = [notebook.index(s) for s in sections]

        for a, b in zip(section_idx, section_idx[1:]):
            section = notebook[a]
            print(f"\n### {section}")

            for i in range(a+1, b, 4):
                head = ''.join(notebook[i:i+3])
                print(f"#### {head}")
                note = notebook[i+3]
                print(note)


if __name__ == '__main__':
    main()
