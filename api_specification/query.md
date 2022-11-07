1. table [resources], store two types of resources, identified by resource_id
   	1. resource_id ending with 'kw' --> first chart, gives system load
   	1. resource_id ending with 'kwh' --> second chart, gives energy capacity

### chart1

1. actual

   ```sqlite
   SELECT resource_id from resources;
   ```

   

   ```sqlite
   SELECT sum(meters.real_power), orders.market_id 
                       FROM meters 
                       JOIN orders ON device_id 
                       WHERE orders.resource_id = (?)
                       GROUP by market_id
                       ORDER by market_id;
   
   get largest_market_id
   
   SELECT sum(dispatches.quantity), orders.market_id
                            FROM dispatches JOIN orders ON order_id
                            WHERE orders.resource_id = (?) AND orders.market_id > largest_market_id
                            GROUP BY market_id
                            ORDER by market_id;
   ```

   

2. cleared

   ```sqlite
   # what reported in the auction table
   SELECT quantity, market_time FROM auctions 
            WHERE market_time > now -24h
            ORDER BY market_time;
   ```

   

### chart2

   ```sqlite
   SELECT resource_id from resources;
   ```

   

   ```sqlite
   SELECT sum(meters.real_power), orders.market_id 
                       FROM meters 
                       JOIN orders ON device_id 
                       WHERE orders.resource_id = (?)
                       GROUP by market_id
                       ORDER by market_id;
   
   get largest_market_id
   
   SELECT sum(dispatches.quantity), orders.market_id
                            FROM dispatches JOIN orders ON order_id
                            WHERE orders.resource_id = (?) AND orders.market_id > largest_market_id
                            GROUP BY market_id
                            ORDER by market_id;
   ```

   

2. cleared

   ```sqlite
   ???
   # what reported in the auction table
   SELECT quantity, market_time FROM auctions 
            WHERE market_time > now -24h
            ORDER BY market_time;
   ```

### chart3

### chart4

### chart5

### chart6