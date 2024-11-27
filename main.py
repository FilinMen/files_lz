table = doc_word.add_table(rows=1, cols=len(df_word.columns))

#Добавляем заголовки колонок
hdr_cells = table.rows[0].cells
for i, column_name in enumerate(df_word.columns):
    hdr_cells[i].text = column_name

# Добавляем данные из DataFrame
for index, row in df_word.iterrows():
    row_cells = table.add_row().cells
    for i, cell_value in enumerate(row):
         row_cells[i].text = str(cell_value)  
         #надосделать таблицу с тремя столбцами 