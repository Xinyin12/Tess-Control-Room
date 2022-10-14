create table settings
(
    class text not null,
    name text not null,
    value_at int not null,
    value text
);
create unique index u_group_name_valueat on settings (class,name,value_at);

create table markets
(
    resource_id text not null,
    units text not null,
    interval int not null
);

create table auctions 
(
    auction_id text primary_key,
    market_id int not null,
    resource_id text not null,
    market_time real not null,
    price real not null,
    quantity real not null,
    marginal_type text not null,
    marginal_order text not null,
    marginal_quantity real not null,
    marginal_rank int not null
);
create unique index u_auctions_constraintid_marketid_markettime on auctions (resource_id, market_id, market_time);

create table agents
(
    agent_id text primary key,
    resource_id text not null
);

create table devices
(
    device_id text primary key,
    agent_id text not null,
    device_type text not null
);
create index i_devices_deviceid_agentid on devices (device_id, agent_id);

create table orders
(
    order_id primary key,
    record_time datetime not null,
    device_id text not null,
    resource_id text not null,
    market_id int not null,
    quantity real not null,
    price real not null,
    flexible int not null default 0,
    state real not null
);
create unique index u_orders_marketid_deviceid on orders (market_id, device_id);
create index i_orders_resourceid_deviceid_marketid on orders (resource_id,device_id,market_id);

create table dispatches
(
    order_id text primary key,
    record_time datetime not null,
    quantity real not null
);
create index i_dispatches_recordtime_orderid on dispatches (record_time, order_id);

create table settlements
(
    order_id text primary key,
    record_time datetime not null,
    cost real not null
);
create index i_settlements_recordtime_orderid on settlements (record_time, order_id);
