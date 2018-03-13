CREATE TABLE change_value(
       id SERIAL PRIMARY KEY,
       ts timestamp,
       value_cambia_valute real,
       value_xe real,
       value_diff real,
       value_diff_perc real);
