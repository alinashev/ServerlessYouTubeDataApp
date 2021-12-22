CREATE EXTERNAL TABLE IF NOT EXISTS `atestdb`.`test` ( 
`col1` int, `col2` int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' WITH SERDEPROPERTIES ( 'serialization.format' = '1'
) LOCATION 's3://task-bucket-a/Parquet/test'
TBLPROPERTIES ('has_encrypted_data'='false')