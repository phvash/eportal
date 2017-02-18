from bs4 import BeautifulSoup
# f_obj = open('rawscore.html', 'r')
# html_doc = f_obj.read()
# f_obj.close()
#
# results = {}
#


class Parser:
    """Parser all html received from eportal"""
    def __init__(self):
        pass

    @staticmethod
    def parse_html(html_doc):
        results = {}
        soup = BeautifulSoup(html_doc, 'html.parser')

        for row in soup.find_all('tr')[1:]:
            row_details = []
            for column in row.contents:
                if column.string != '\n':
                    row_details.append(column.string)
            results[row_details[0]] = row_details[1:]

        for course in results:
            print course
            details = ['Title', 'No of Units', 'Test Score', 'Exam Score', 'Total']
            for i in range(len(results[course])):
                print "{} : {}".format(details[i], results[course][i])
