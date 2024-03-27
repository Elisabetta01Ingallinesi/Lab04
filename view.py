import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        # Row 1
        self.__tDd1 = ft.Text()
        self.ddLanguage = ft.Dropdown(label="Lingua", width= 500, on_change=self.dropdown_changed1)
        self._fillDdLanguage()
        row1 = ft.Row([self.ddLanguage, self.__tDd1])

        # Row 2
        self.__tDd2 = ft.Text()
        self.ddOpzioni = ft.Dropdown(label = "Opzione di ricerca", width = 200, on_change=self.dropdown_changed2)
        self._fillDdOpzioni()
        self.txtTesto = ft.TextField(label = "Testo", width= 600)
        self._btn = ft.ElevatedButton(text = "SpellCheck", on_click=self.__controller.handleSpellCheck)
        row2= ft.Row([self.ddOpzioni, self.__tDd2, self.txtTesto, self._btn])

        self.lvOut = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        self.page.add(row1, row2, self.lvOut)

        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()

    def _fillDdLanguage(self):
        self.ddLanguage.options.append(ft.dropdown.Option("italian"))
        self.ddLanguage.options.append(ft.dropdown.Option("english"))
        self.ddLanguage.options.append(ft.dropdown.Option("spanish"))

    def dropdown_changed1(self, e):
        self.__tDd1.value = f"Dropdown cambiato correttamente {self.ddLanguage.value} "
        self.page.update()

    def _fillDdOpzioni(self):
        self.ddOpzioni.options.append(ft.dropdown.Option("Default"))
        self.ddOpzioni.options.append(ft.dropdown.Option("Linear"))
        self.ddOpzioni.options.append(ft.dropdown.Option("Dichotomic"))

    def dropdown_changed2(self, e):
        self.__tDd2.value = f"Dropdown cambiato correttamente {self.ddOpzioni.value} "
        self.page.update()


