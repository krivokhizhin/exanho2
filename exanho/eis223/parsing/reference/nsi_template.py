from ...ds.reference import baseTemplateType, baseTemplateFieldType, templateTableType, templateTableColumnType
from ...model.nsi_template import *


def get_template(session, polymorphic, discriminator:str, id:int) -> NsiTemplateBase:
    return session.query(NsiTemplateBase).\
        with_polymorphic(polymorphic).\
            filter(NsiTemplateBase.discriminator == discriminator, NsiTemplateBase.long_id == id).\
                one_or_none()

def fill_template(session, template:NsiTemplateBase, template_obj:baseTemplateType):
    template.long_id = template_obj.id
    template.parent_long_id = template_obj.parent
    template.status = template_obj.status
    template.version = template_obj.version

def fill_field_template(session, field_template:NsiFieldTemplateBase, field_template_obj:baseTemplateFieldType):
    field_template.long_id = field_template_obj.id
    field_template.name = field_template_obj.name
    field_template.extend_type = field_template_obj.type_
    field_template.length = field_template_obj.length
    field_template.mandatory = field_template_obj.mandatory
    
    field_template.tab_ordinal = field_template_obj.position.tabOrdinal
    field_template.tab_name = field_template_obj.position.tabName
    field_template.section_ordinal = field_template_obj.position.sectionOrdinal
    field_template.section_name = field_template_obj.position.sectionName
    
    field_template.info = field_template_obj.typeInfo
    field_template.integr_code = field_template_obj.integrCode
    field_template.index_number = field_template_obj.indexNumber
    field_template.code = field_template_obj.code

    field_template.table_type = get_table_type(session, field_template_obj.tableType)

def get_table_type(session, template_table_obj:templateTableType):
    if template_table_obj is None:
        return None

    long_id = template_table_obj.id
    table = session.query(NsiTableTemplate).filter(NsiTableTemplate.long_id == long_id).one_or_none()

    if table is None:
        table = NsiTableTemplate(
            long_id = long_id,
            name = template_table_obj.name
        )
        
        session.add(table)

        if template_table_obj.fixedColumnsData:
            for fixed_column_data_obj in template_table_obj.fixedColumnsData.colValue:
                fixed_column_data = get_table_fixed_column_data(session, fixed_column_data_obj)
                if fixed_column_data:
                    table.fixed_columns_data.append(fixed_column_data)

        if template_table_obj.columns:
            for column_obj in template_table_obj.columns.column:
                column = get_table_column(session, column_obj)
                if column:
                    table.columns.append(column)

    return table

def get_table_fixed_column_data(session, fixed_column_data_obj:str):
    if fixed_column_data_obj is None:
        return None
        
    fixed_column_data = NsiTableTemplateFixedColumnData(
        value = fixed_column_data_obj
    )

    return fixed_column_data

def get_table_column(session, column_obj:templateTableColumnType):
    if column_obj is None:
        return None

    column = NsiTableColumnTemplate(
        index = column_obj.colIndex,
        name = column_obj.colName,
        extend_type = column_obj.colType,
        length = column_obj.colLength,
        mandatory = column_obj.colMandatory,
        integr_code = column_obj.integrCode,
        info = column_obj.typeInfo
    )

    return column