import flet as ft
from UI.view import View
from model.biblioteca_DTO import Biblioteca
from model.libro_DTO import Libro
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view
        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dd_biblioteca(self):
        '''
        if biblioteca is None:
            self.alert.show_alert("Devi scegliere una bilioteca")
            return 
        '''
        biblioteche = self._model.get_biblioteche()

        self._view._dd_biblioteca.options.append(ft.DropdownOption(key = "nessuno", text = "Nessun filtro"))

        for biblioteca in biblioteche:
            self._view._dd_biblioteca.options.append(ft.DropdownOption(key = str(biblioteca.id), text= (biblioteca.nome)))

    def popola_dd_generi(self):
        generi = self._model.get_generi()

        self._view._dd_genere.options.append(ft.DropdownOption(key = "nessuno", text = "Nessun filtro"))

        for genere in generi:
            self._view._dd_genere.options.append(ft.DropdownOption(key = genere, text = genere))

    # CALLBACKS DROPDOWN
    # TODO
    def handler_dd_biblioteca(self, e):
        self.biblioteca_selezionata = self._view._dd_biblioteca.value

    def handler_dd_genere(self, e):
        self.genere_selezionato = self._view._dd_genere.value

    # AZIONE: MOSTRA LIBRI
    # TODO
    def handler_mostra_libri(self,  e):
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        self._view._list_view.controls.clear()

        if len(libri) == 0:
            self._view.update()
            self._view.show_alert("Nessun libro trovato")
            return

        for libro in libri:
            self._view._list_view.controls.append(ft.Text(f"{libro.titolo} - {libro.autore} - {libro.genere} - {libro.anno_pubblicazione}"))

        self._view.update()