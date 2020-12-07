DROP TABLE nsi_purch_phase_transition_association CASCADE;
DROP TABLE nsi_purchase_phase_transition CASCADE;
DROP TABLE nsi_purch_phase_protocol_association CASCADE;
DROP TABLE nsi_purch_method_phase_association CASCADE;
DROP TABLE nsi_purchase_phase CASCADE;
DROP TABLE nsi_purch_method_template_association CASCADE;
DROP TABLE nsi_purch_method_protocol_association CASCADE;
DROP TABLE nsi_purchase_protocol CASCADE;
DROP TABLE nsi_purchase_method CASCADE;

DROP TABLE nsi_template_field_notice CASCADE;
DROP TABLE nsi_template_notice CASCADE;

DELETE FROM nsi_template_base WHERE type='notice';
DELETE FROM nsi_template_field_base WHERE type='notice';