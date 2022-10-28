# Database API

## `GET /db/load?<args...>`

Get a list of all resources.

### Arguments

| Name        | Type | Required | Description                                                  |
| ----------- | ---- | -------- | ------------------------------------------------------------ |
| device_type | text | No       | battery, ev, heater, hvac, pv, thermal. null means all devices |
| status      | int  | No       | 0:available;1:dispatched;-1:unavailable, null means all      |

### Returns

| Code | Body                                | Description                 |
| ---- | ----------------------------------- | --------------------------- |
| 200  | `{"data" : ["<resource_id>", ...]}` | Resource list data found ok |
| 403  | `{"error" : "not authorized"}`      | Access is denied            |

### Access

| Authority |  Agent  | Loader  | Participants | Controllers | Settlement | Operators | Experimenters | Analysts | Developers |
| --------- | :-----: | :-----: | :----------: | :---------: | :--------: | :-------: | :-----------: | :------: | :--------: |
| Access    | &check; | &check; |      X       |   &check;   |  &check;   |  &check;  |    &check;    | &check;  |  &check;   |

----

## `GET /db/energy?<args...>`

Get a list of all resources.

### Arguments

| Name        | Type | Required | Description                                                  |
| ----------- | ---- | -------- | ------------------------------------------------------------ |
| device_type | text | No       | battery, ev, heater, hvac, pv, thermal. null means all devices |
| status      | int  | No       | 0:available;-1:unavailable, null means all                   |

### Returns

| Code | Body                                | Description                 |
| ---- | ----------------------------------- | --------------------------- |
| 200  | `{"data" : ["<resource_id>", ...]}` | Resource list data found ok |
| 403  | `{"error" : "not authorized"}`      | Access is denied            |

### Access

| Authority |  Agent  | Loader  | Participants | Controllers | Settlement | Operators | Experimenters | Analysts | Developers |
| --------- | :-----: | :-----: | :----------: | :---------: | :--------: | :-------: | :-----------: | :------: | :--------: |
| Access    | &check; | &check; |      X       |   &check;   |  &check;   |  &check;  |    &check;    | &check;  |  &check;   |

----

## 

# Return Data

## Load_data

### schema

id

*[String](#string)*

feeder_id

*[String](#string)*

load

*[BigDecimal](#BigDecimal)*

*example: 100*

status

*[Integer](#integer)* 0:available;1:dispatched;-1:unavailable

*example: 0*

device_type

*[String](#string)*

*example: Battery*

unit

*[String](#string)*

*example: MWh*

timestamp

*[Date](#DateTime)* format: date-time

### example

```
[ {
  "unit" : "MWh",
  "load" : 100,
  "feeder_id" : "feeder_id",
  "device_type" : "Battery",
  "id" : "id",
  "status" : 0,
  "timestamp" : "2000-01-23T04:56:07.000+00:00"
}, {
  "unit" : "MWh",
  "load" : 100,
  "feeder_id" : "feeder_id",
  "device_type" : "Battery",
  "id" : "id",
  "status" : 0,
  "timestamp" : "2000-01-23T04:56:07.000+00:00"
} ]
```

## energy_data

### schema

id

*[String](#string)*

feeder_id

*[String](#string)*

energy

*[BigDecimal](#BigDecimal)*

*example: 100*

status

*[Integer](#integer)* 0:available;-1:unavailable

*example: 0*

device_type

*[String](#string)*

*example: Battery*

unit

*[String](#string)*

*example: MWh*

timestamp

*[Date](#DateTime)* format: date-time

### example

```
[ {
  "unit" : "MWh",
  "feeder_id" : "feeder_id",
  "device_type" : "Battery",
  "id" : "id",
  "energy" : 100,
  "status" : 0,
  "timestamp" : "2000-01-23T04:56:07.000+00:00"
}, {
  "unit" : "MWh",
  "feeder_id" : "feeder_id",
  "device_type" : "Battery",
  "id" : "id",
  "energy" : 100,
  "status" : 0,
  "timestamp" : "2000-01-23T04:56:07.000+00:00"
} ]
```

