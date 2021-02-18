SELECT p.* FROM agg_contract AS c
JOIN agg_contract_participant AS cp ON c.id = cp.contract_id
JOIN agg_participant AS p ON cp.participant_id = p.id
WHERE c.state='EXECUTION'
LIMIT 10;