CREATE TABLE order_analysis_mengniu (id  string COMMENT  "id", name  string COMMENT  "name", phone_number  string COMMENT  "phone_number", store  string COMMENT  "store", channel  string COMMENT  "channel", department  string COMMENT  "department", center  string COMMENT  "center", group  string COMMENT  "group", brand  string COMMENT  "brand", province  string COMMENT  "province", city  string COMMENT   "city", address  string COMMENT   "address", create_date  string COMMENT   "create_date", operate_date  string COMMENT   "operate_date", product  string COMMENT   "product", order_price  float COMMENT   "order_price", discount  float COMMENT  "discount", actual_payment  float COMMENT  "actual payment") comment  "order_analysis_mengniu"  PARTITIONED BY (`dt` string) ;