# StockProject
create or replace view s2_fxs_stcode as
select lpad(to_char("1"),6,'0') as stcode,
to_char("2") as stname,
to_date(to_char("4"),'yyyy-mm-dd') as crdt,
to_date(to_char("5"),'yyyy-mm-dd') as crdt2,
to_char("6") as 分析结果,
to_number(to_char("7")) as his_price,
to_number(to_char("8")) as cur_price,
to_char("9") 阶段涨跌幅,
to_char("FXSCODE") as FXSCODE
 from fxs_stcode;
