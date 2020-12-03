INSERT INTO ftp_load_task (status, location, schedule, scheduled_date, excluded_folders, delimiter)
VALUES('NEW', '/out/nsi/*', '*', date '2020-11-13' + time '08:00:00', 'agencyRelations|archive|customerRegistry|nsiAgency|nsiClauseType|nsiOrganization|nsiProtocol|nsiPurchaseMethod', '|');

INSERT INTO ftp_load_task (status, location, schedule, scheduled_date)
VALUES('NEW', '/out/nsi/nsiOrganization/*', '*', date '2020-11-13' + time '08:00:00');

INSERT INTO ftp_load_task (status, location, schedule, scheduled_date)
VALUES('NEW', '/out/nsi/nsiPurchaseMethod/*', '*', date '2020-11-13' + time '08:00:00');

INSERT INTO ftp_load_task (status, location, schedule, scheduled_date)
VALUES('NEW', '/out/nsi/nsiProtocol/*', '*', date '2020-11-13' + time '08:00:00');