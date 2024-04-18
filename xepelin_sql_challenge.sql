-- DDLS
create schema if not exists xepelin_test;

create table if not exists xepelin_test.currency_price(
id int,
currency_name text,
usd_price numeric
)
;

create table if not exists xepelin_test.wallet_snapshot(
snapshot_date date, 
wallet_id int,
user_id int,
currency_id int,
balance numeric
)
;


-- INSERT TEST DATA
insert into xepelin_test.currency_price values
(1,'BTC',50000),
(2,'USDT',1),
(3,'ARS',0.5)
;

insert into xepelin_test.wallet_snapshot values
('2020-01-03',21412,36528,2,10),
('2020-01-03',21413,36520,3,10),
('2020-01-03',21414,36522,1,1),
('2020-01-02',21413,36520,3,5)
;


-- QUERY
with date_resume as (
	select 
	ws.snapshot_date as date, 
	ws.user_id as bb_user_id, 
	sum(balance * usd_price) over (partition by ws.snapshot_date, ws.user_id) as bb_balance_usd, 
	rank() over (partition by ws.snapshot_date order by balance * usd_price desc) as daily_user_rank,
	sum(balance * usd_price) over (partition by ws.snapshot_date) as total_balances_usd
	
	from xepelin_test.wallet_snapshot ws
	left join xepelin_test.currency_price cp on cp.id = ws.currency_id
)

select
date,
bb_user_id,
bb_balance_usd,
total_balances_usd,
round(((bb_balance_usd / total_balances_usd) * 100), 2)as bb_percentage

from date_resume
where daily_user_rank = 1
;
