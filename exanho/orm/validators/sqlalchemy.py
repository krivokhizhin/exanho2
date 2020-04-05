class Validator():
    
    def __init__(self, metadata, inspector):
        self._md = metadata
        self._insp = inspector
        self.is_valid = False
        self.error_messages = []
        self.warning_messages = []
        
    def validate(self, full=False):
        if (self._insp.default_schema_name != 'public'):
            self.error_messages.append("For the specified user, the default schema is '{}', but the expected 'public'.".format(self._insp.default_schema_name))
            self.is_valid = False
            return
        
        md_table_names = set(self._md.tables.keys())
        db_table_names = set(self._insp.get_table_names())
        
        for md_miss_table_name in md_table_names.difference(db_table_names):
            self.error_messages.append("There is no '{}' table in the database.".format(md_miss_table_name))

        if full:  
            for db_miss_table_name in db_table_names.difference(md_table_names):
                if db_miss_table_name in Validator.excluding_tables:
                    continue
                self.error_messages.append("There is no '{}' table in the domain.".format(db_miss_table_name))
        
        if (len(self.error_messages) > 0):
            self.is_valid = False
        else:
            self.is_valid = True