DROP TABLE nsi_protocol_template_association CASCADE;
DROP TABLE nsi_protocol_purch_method CASCADE;
DROP TABLE nsi_protocol CASCADE;

DROP TABLE nsi_template_field_protocol CASCADE;
DROP TABLE nsi_template_protocol CASCADE;

DELETE FROM nsi_template_base WHERE type='protocol';
DELETE FROM nsi_template_field_base WHERE type='protocol';