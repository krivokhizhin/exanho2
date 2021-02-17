class VkMethodCall:

    def __init__(self, section:str, method:str, options:str) -> None:
        self.section = section
        self.method = method
        self.options = options

    def __str__(self) -> str:
        return 'vk_api: section={0.section!s}, method={0.method!s}, options={0.options!s}'.format(self)

    def __repr__(self) -> str:
        return 'VkMethodCall({0.section!r}, {0.method!r}, {0.options!s})'.format(self)

    def form_vk_api_method_name(self):
        return '{}_{}'.format(self.section, self.method)