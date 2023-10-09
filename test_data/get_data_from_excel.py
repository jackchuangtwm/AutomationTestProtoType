import pandas
class ExcelSheetOperator:

    def __init__(self, file_name, sheet_name):
        self._file_name = file_name
        self._sheet_name = sheet_name

        self._df = pandas.read_excel(self._file_name, sheet_name=self._sheet_name, dtype=str)
        self._df = self._df.fillna('')
        if 'Title' in self._df:
            for row_index in self._df['Title'].keys():
                if 'chars' not in self._df['Title'][row_index] and len(str(self._df['Title'][row_index]))!=0:
                    self._df['Title'][row_index] = str('Rupert_' + str(self._df['Title'][row_index]).strip('\n'))
        
        if 'sizes' in self._df:
            for row_index in self._df['sizes'].keys():
                self._df['sizes'][row_index] = (
                    self._df['sizes'][row_index].split(',') 
                    if self._df['sizes'][row_index] != ''
                    else None
                    )

        if 'color_ids' in self._df:
            for row_index in self._df['color_ids'].keys():
                self._df['color_ids'][row_index] = (
                    self._df['color_ids'][row_index].split(',') 
                    if self._df['color_ids'][row_index] != ''
                    else None
                    )
                
        if 'other_images' in self._df:
            for row_index in self._df['other_images'].keys():
                self._df['other_images'][row_index] = (
                    self._df['other_images'][row_index].split(',') 
                    if self._df['other_images'][row_index] != ''
                    else ['', '']
                    )


        self._df = self._df.applymap(
            lambda x: 'K' * int(x.split()[0]) if isinstance(x, str) and 'chars' in x else x
            )

    def position(self, row, column):
        return self._df.loc[row, column]
    
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

