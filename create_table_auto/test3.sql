CREATE TABLE dim_campign_tracking (campign_id string  , campign_name string  , campign_type string  , campign_brand string  , campign_id_name string) comment  "dim_campign_tracking"  PARTITIONED BY (`dt` string) ;