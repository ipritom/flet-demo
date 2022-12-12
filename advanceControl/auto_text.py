"""
https://towardsdatascience.com/fuzzy-string-matching-in-python-68f240d910fe
pip install fuzzywuzzy
pip install python-Levenshtein # to remove the slow warning (warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning'))
"""
import flet as ft
from fuzzywuzzy import fuzz

theme = ft.Theme()
def main(page: ft.Page):
    text_list = ["banana", "apple", "tiger", "avocado", "toxic", "ten"]

    def option_selected(e):
        print(e.data)
        text_box.value = e.data
        suggest_list.clean()
        page.update()


    def text_box_on_change(e):
        suggest_list.clean()
        match_dict = {}
        for token in text_list:
            match = fuzz.ratio(e.data,token)
            match_dict[token] = match
            if match > 50:
                suggest_list.controls.append(ft.TextButton(token, data=token, on_click=option_selected))
        
        print(match_dict)
        page.update()


    text_box = ft.TextField(on_change=text_box_on_change)
    suggest_list = ft.ListView(expand=1)

    suggest_list.controls.append(ft.TextButton("PASS"))
    page.add(ft.Column(
        [text_box,
        suggest_list]
    ))



    page.theme_mode = "light"
    page.update()


ft.app(target=main)