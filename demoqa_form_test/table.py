from selene.core.entity import Element


class Table:
    def __init__(self, element: Element):
        self.element = element

    def get_row(self, row_num):
        return self.element.all('tr')[row_num - 1]

    def get_cell(self, row_num, cell_num):
        return self.get_row(row_num).all('td')[cell_num - 1]
