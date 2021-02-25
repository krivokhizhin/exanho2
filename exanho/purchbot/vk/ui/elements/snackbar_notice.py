from ..element_content import SnackbarType, SnackbarContent

class SnackbarNotice:

    def __init__(self) -> None:
        self.content = SnackbarContent(
            type_ = SnackbarType.show_snackbar
        )

    def set_text(self, text:str):
        self.content.text = text