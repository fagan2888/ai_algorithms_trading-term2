import os
from pathlib import Path
from IPython.display import display, Markdown, HTML


def auto_notebook_links(p, t):
    path = Path(p)
    ulo = '<ul>'
    ul_li = ''
    ulc = '</ul>'
    style = 'background-color:#fefdf6;padding:10px;border:1px solid #b1b0a8;border-radius:5px;'

    dir_contents = os.listdir(path)
    all_notebooks = [file for file in dir_contents if file.endswith('.ipynb')]
    notebooks = [
        file for file in dir_contents
        if file.endswith('.ipynb') and not file.endswith('_solution.ipynb')
    ]
    notebooks.sort()

    display(Markdown(f'### {t}\n___'))

    for idx, file in enumerate(notebooks):
        file_name = file.split(".")[0]
        file_path = path / file
        title = file_name.replace('_', " ").title()

        solution_file = f'{file_name}_solution.ipynb'

        if solution_file in all_notebooks:
            li = f'<li><a href="{file_path}" target="_blank">{title}</a> : <a href="{path / solution_file}">Solution</a></li>'
            ul_li += li
        else:
            li = f'<li><a href="{file_path}" target="_blank">{title}</a></li>'
            ul_li += li
    display(HTML(f'<div style="{style}">{ulo}{ul_li}{ulc}</div>'))