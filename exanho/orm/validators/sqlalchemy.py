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
        
        self.validate_tables(full)
        
        if (len(self.error_messages) > 0):
            self.is_valid = False
        else:
            self.is_valid = True

    def validate_tables(self, full=False):
        md_table_names = set(self._md.tables.keys())
        db_table_names = set(self._insp.get_table_names())
        
        for md_miss_table_name in md_table_names.difference(db_table_names):
            self.error_messages.append("There is no '{}' table in the database.".format(md_miss_table_name))

        if full:  
            for db_miss_table_name in db_table_names.difference(md_table_names):
                self.error_messages.append("There is no '{}' table in the domain.".format(db_miss_table_name))

        for table_name in md_table_names.intersection(db_table_names):
            self.validate_table(table_name)

    def validate_table(self, table_name):
        md_table = self._md.tables[table_name]

        db_columns = {db_column['name']: db_column for db_column in self._insp.get_columns(table_name)}
        for md_column in md_table.columns:
            db_column = db_columns.get(md_column.key, None)
            if db_column is None:
                self.error_messages.append(f'There is no "{md_column.key}" column in "{table_name}" table from database.')
                continue

            # This function is currently not implemented for SQLAlchemy types, and for all built in types will return None.
            # A future release of SQLAlchemy will potentially implement this method for builtin types as well.
            # The function should return True if this type is equivalent to the given type.
            # https://docs.sqlalchemy.org/en/13/core/type_api.html#sqlalchemy.types.TypeEngine.compare_against_backend

            # if not db_column['type'].compare_against_backend('psycopg2', md_column.type):
            #     pass

            db_type = str(db_column['type'])
            md_type = str(md_column.type)
            if (md_type != db_type) and (type_matching.get(md_type, '') != db_type):
                self.error_messages.append(f'Type mismatch for {md_column.key} column of the {table_name} table: {md_column.type} != {db_type}.')

            del db_columns[md_column.key]

        if db_columns:
            self.error_messages.extend([f'There is no "{name}" column in "{table_name}" table from domain.' for name in db_columns.keys()])

type_matching = {
    'DATETIME': 'TIMESTAMP WITHOUT TIME ZONE'
}