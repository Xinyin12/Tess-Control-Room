1. table [resources], store two types of resources, identified by resource_id
   	1. resource_id ending with 'kw' --> first chart, gives system load
   	1. resource_id ending with 'kwh' --> second chart, gives energy capacity

### chart1

1. actual

   ```sqlite
   SELECT resource_id from resource;
   ```

   

   ```sqlite
   SELECT sum(meters.real_power), orders.market_id 
   FROM meters 
   JOIN orders ON device_id 
   Where orders.resouece_id = "xxxx"
   group by market_id
   [Order by market_id]
   
   get largest_market_id
   
   SELECT sum(dispatches.quantity), orders.market_id
   FROM dispatches JOIN orders ON order_id
   WHERE orders.resouece_id = "xxxx" AND orders.market_id > largest market_id
   GROUP BY market_id
   [Order by market_id]
   ```

   

2. cleared

   ```sqlite
   # what reported in the auction table
   select quantity, market_time from auctions where market_time > now -24h order by market_time
   ```

   

### chart2

1. actual

   ```sqlite
   SELECT resource_id from resource;
   ```

   

   ```sqlite
   SELECT sum(meters.real_power), orders.market_id 
   FROM meters 
   JOIN orders ON device_id 
   Where orders.resouece_id = "xxxx"
   group by market_id
   [Order by market_id]
   
   get largest_market_id
   
   SELECT sum(dispatches.quantity), orders.market_id
   FROM dispatches JOIN orders ON order_id
   WHERE orders.resouece_id = "xxxx" AND orders.market_id > largest market_id
   GROUP BY market_id
   [Order by market_id]
   ```

   

2. cleared

   ???

   ```sqlite
   # what reported in the auction table
   select quantity, market_time from auctions where market_time > now -24h order by market_time
   ```

### chart3

### chart4

### chart5

### chart6