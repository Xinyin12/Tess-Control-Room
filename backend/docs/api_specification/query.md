1. table [resources], store two types of resources, identified by resource_id
   	1. resource_id ending with 'kw' --> first chart, gives system load
   	1. resource_id ending with 'kwh' --> second chart, gives energy capacity

### chart1

1. actual

   ```sqlite
   SELECT meters.valid_at AS x, sum(meters.real_power) AS y
   FROM meters JOIN devices ON meters.device_id = devices.device_id
   JOIN agents ON devices.agent_id = agents.agent_id
   JOIN resources ON agents.resource_id = resources.resource_id
   WHERE resources.name = 'Feeder_1'
   group by round(meters.valid_at/300);
   ```
   
   
   
2. cleared

   ```sqlite
   SELECT dispatches.valid_at AS x, sum(dispatches.quantity) AS y
   FROM dispatches JOIN orders ON dispatches.order_id = orders.order_id
   JOIN resources ON orders.resource_id = resources.resource_id
   WHERE resources.name = 'Feeder_1'
   GROUP BY round(dispatches.valid_at/300);
   
   
   
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