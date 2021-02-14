import enum

class IContext:
    pass

class ButtonType(enum.Enum):
    text = 1
    open_link = 2
    location = 3
    vkpay = 4
    open_app = 5
    callback = 6

class ButtonColor(enum.Enum):
    primary = 1
    secondary = 2
    negative = 3
    positive = 4

class TemplateType(enum.Enum):
    carousel = 1

class ElementActionType(enum.Enum):
    open_link = 1
    open_photo = 2

class ButtonActionContent(IContext):

    def __init__(self, **kwargs) -> None:
        self.type_ = kwargs.get('type_', None)
        self.label = kwargs.get('label', None)
        self.payload = kwargs.get('payload', None)
        self.link = kwargs.get('link', None)
        self.hash = kwargs.get('hash', None)
        self.app_id = kwargs.get('app_id', None)
        self.owner_id = kwargs.get('owner_id', None)

class ButtonContent(IContext):

    def __init__(self, **kwargs) -> None:
        self.action = kwargs.get('action', None)
        self.color = kwargs.get('color', None)

class KeyboardContent(IContext):

    def __init__(self, **kwargs) -> None:
        self.one_time = kwargs.get('one_time', None)
        self.buttons = kwargs.get('buttons', list())
        self.inline = kwargs.get('inline', None)

class ElementActionContent(IContext):

    def __init__(self, **kwargs) -> None:
        self.type_ = kwargs.get('type_', None)
        self.link = kwargs.get('link', None)

class TemplateElementContent(IContext):

    def __init__(self, **kwargs) -> None:
        self.title = kwargs.get('title', None)
        self.description = kwargs.get('description', None)
        self.photo_id = kwargs.get('photo_id', None)
        self.buttons = kwargs.get('buttons', list())
        self.action = kwargs.get('action', None)

class TemplateContent(IContext):

    def __init__(self, **kwargs) -> None:
        self.type_ = kwargs.get('type_', None)
        self.elements = kwargs.get('elements', list())