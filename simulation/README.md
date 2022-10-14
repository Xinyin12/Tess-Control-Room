[![validate](https://github.com/postroad-energy/simulation/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/postroad-energy/simulation/actions/workflows/validate.yml)

TESS Connected Communities Simulation

This repository contains the realtime simulation for TESS2. To run this
simulation do the following:

# Prerequisites

To run the realtime simulation you must install HiPAS GridLAB-D Version 4.3 or
later. See https://github.com/slacgismo/gridlabd for details.

On some systems you may need to install the SQLite development library, e.g.,

~~~
$ yum install sqlite-devel -y
~~~

or

~~~
$ apt-get install libsqlite3-dev
$ pip install pysqlite
~~~

# Starting the simulation

~~~
$ cd gridlabd
$ gridlabd config.glm realtime.glm
~~~

The simulation will run continously until interrupted with a `SIGINT`
(Ctrl-C).

## Configuration

The simulation is configured using the `config.glm` file.  The following
options may be set:

  - `PYTHON_OPTIONS`: Sets the options used by the python code. Valid options
    include:
    - `newdb`: enables destroying the existing database when starting the
      simulator (default True).
    - `progress`: enables showing progress time reports (default True).
    - `warning`: disables warning messages (default False).
    - `verbose`: enables verbose messages (default False).
    - `debug`: enables debug messages (default False).

  - `DATABASE`: Sets the name of the database given to the Tess2Database
    class (default 'gridlabd.db').

  - `UTILITY_NAME`: Sets the name of the simulated utility
    (default `Sim_Utility`).

  - `FEEDER_NAMES`: Sets the names of the feeders to create in the simulation
    (default is `Feeder_[1234]`).

  - `AGENT_COUNT`: Sets the number of agents to include in each feeder
    created (default is 25).

# Realtime Status

To observe the status of the system, run

~~~
$ cd gridlabd
$ python3 status.py
~~~

The status display runs until interrupted with a `SIGINT` (Ctrl-C).

# Data

The data is stored in SQLite3 database named by default `gridlabd.db`. The
database schema is stored in `schema.sql`. The database API is implemented in
`database.py` using the `Tess2Database` class.

You can dump the database using the command
~~~
$ python3 dump.py gridlabd.db
~~~

This creates a CSV file for each table in the database.

# Validation

The simulation can be tested by running the the command

~~~
$ cd gridlabd
$ gridlabd -D TEST config.glm realtime.glm
~~~

This will run the simulation from the wayback time to the present time and
then stop.

# Docker

The simulation can be run on docker if you have the source on your system. Run the following commands in a shell:

~~~
$ git clone https://github.com/postroad-energy/simulation
$ cd simulation/gridlabd
$ docker pull slacgismo/gridlabd:develop
$ docker run -it -v $PWD:/tmp --name testsim1 slacgismo/gridlabd:develop gridlabd config.glm realtime.glm
~~~

You can monitor the status of the simulation by opening a second shell and running the following command:

~~~
$ docker exec -it testsim1 python3 status.py
~~~
