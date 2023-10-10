import pandas
class ExcelSheetOperator:

    def __init__(self, file_name, sheet_name):
        self._file_name = file_name
        self._sheet_name = sheet_name

        self._df = pandas.read_excel(self._file_name, sheet_name=self._sheet_name, dtype=str)

    def to_dict(self):
        return self._df.to_dict()
    
    def to_dict_list(self):
        origin_dict = self.to_dict()
        dict_list = []
        for i in range(0, self.row_count()):
            dictionary = {}
            for key in origin_dict:
               dictionary[key] = origin_dict[key][i]
            dict_list.append(dictionary)
        return dict_list
    
    def row_count(self):
        return len(self._df.index)

