DROP TABLE nsi_order_clause_template_association CASCADE;
DROP TABLE nsi_order_clause CASCADE;

DROP TABLE nsi_template_field_order_clause CASCADE;
DROP TABLE nsi_template_order_clause CASCADE;

DELETE FROM nsi_template_base WHERE type='order_clause';
DELETE FROM nsi_template_field_base WHERE type='order_clause';