# ScheduleSync

Welcome to ScheduleSync, the ultimate scheduling companion for UBC students! This application is designed to streamline the course scheduling process by allowing users to create accounts, manage their courses, add friends, and view their friends' schedules.

#### Created with love by [Daven Froberg](http://www.github.com/dfroberg), [Carlos Perez](https://github.com/carlosperez67), [Erica Buchanan](https://github.com/ericabuchanan), and [Brett Caswell](https://github.com/caswellbrett) ####
## Technology Stack

- **Frontend:**
  - Vue.js v3.4.15
  - Quasar v2.14.2

- **Backend:**
  - Python 3
  - Flask v3.0.1
  - MySQL

## Getting Started

To run ScheduleSync locally, follow these steps:

1. Clone the repository:
```bash
   $ git clone https://github.com/davenfroberg/schedule-sync.git
```

2. Install dependencies:
   - TBD
     
3. Configure the database
   - Set up a MySQL database and put the credentials in a new file `config.py`:
```
  host = <host name>
  port = <host port>
  user = <db username>
  password = <db password>
  database = <db name>
```

4. Run the application:
```bash
# Start frontend
$ cd ../front
$ quasar dev

# Start backend
$ cd ../back
$ python apis.py
```

## License ##
ScheduleSync is licensed under the MIT License. Feel free to use, modify, and distribute this software according to the terms of the license.
