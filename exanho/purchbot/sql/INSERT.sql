DECLARE p_id product.id%TYPE;

INSERT INTO product (kind, code, "name") VALUES('QUERY', 'QUE_PAR_ACT', 'Текущая активность участника') RETURNING id INTO p_id;
INSERT INTO tariff (product_id, value) VALUES(p_id, 1);

INSERT INTO product (kind, code, "name") VALUES('QUERY', 'QUE_HIS_ACT', 'Опыт участник') RETURNING id INTO p_id;
INSERT INTO tariff (product_id, value) VALUES(p_id, 1);

INSERT INTO product (kind, code, "name") VALUES('SUBSCRIPTION', 'SUB_PAR', 'События по участнику') RETURNING id INTO p_id;
INSERT INTO tariff (product_id, value) VALUES(p_id, 5);

INSERT INTO product (kind, code, "name") VALUES('REPORT', 'REP_CON_PAR', 'Опыт исполнения контрактов по всем участникам') RETURNING id INTO p_id;
INSERT INTO tariff (product_id, value) VALUES(p_id, 100);