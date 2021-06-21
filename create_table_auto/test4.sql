CREATE TABLE channel
(
    channel_id   string COMMENT ' channel_id',
    channel_name string COMMENT ' channel_name'
) comment  "channel"  PARTITIONED BY (`dt` string);