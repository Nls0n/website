import webbrowser
file_path = 'index.html'
html_string = """
<!DOCTYPE html>
<html>
 <head>
  <meta charset="utf-8">
  <title>Импульс</title>
  <style>
    p {
     margin-top: 0.1em; 
     margin-bottom: 0.1em; 
    }
   </style>
 </head>
 <body>
  <form method="post" action="program">
  <p><font color="grey"> <h2>Список сотрудников</h2></p>
    <p><h2>компании "Импульс"</h2></p>
  <p><b><i>Отдел разработки:</b></p></i> 
  <ul>
      <li>Главный разработчик - Фёдоров Руслан</li>
      <li>Младший разработчик - Иванова Ирина</li>
      <li>Тестировщик - Романов Пётр</li>
  </ul>
   <p><i><b>Бухгалтерия:</b></i></p>  
   <ul>
       <li>Старший бухгалтер - Петров Иван</li>
       <li>Бухгалтер - Антонова Ольга</li>
   </ul>   
  </form>
 </body>
</html>
"""
with open(file_path, 'w', encoding='utf-8') as html_file:
    html_file.write(html_string)
webbrowser.open_new_tab(file_path)