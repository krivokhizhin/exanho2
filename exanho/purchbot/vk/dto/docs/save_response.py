from .doc_dto import DocDto
from .. import JSONObject, MethodResponseBase

class SaveDocsResponse(MethodResponseBase):

    def __init__(self) -> None:
        super().__init__()
        self.docs = list()
    
    def fill(self, json_obj: JSONObject):
        if hasattr(json_obj, 'error'):
            self.fill_error(json_obj)
        elif hasattr(json_obj, 'response'):
            if isinstance(json_obj.response, list):
                for dto in json_obj.response:
                    if dto.type == 'doc':
                        doc_dto = DocDto()
                        doc_dto.fill(dto.doc)
                        self.docs.append(doc_dto)
            else:
                if json_obj.response.type == 'doc':
                    doc_dto = DocDto()
                    doc_dto.fill(json_obj.response.doc)
                    self.docs.append(doc_dto)
        else:
            pass