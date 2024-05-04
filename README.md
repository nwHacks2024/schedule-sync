# ScheduleSync

Welcome to ScheduleSync, the ultimate scheduling companion for UBC students! This application is designed to streamline the course scheduling process by allowing users to create accounts, manage their courses, add friends, and view their friends' schedules.

#### Created with love by [Daven Froberg](http://www.github.com/davenfroberg), [Carlos Perez](https://github.com/carlosperez67), [Erica Buchanan](https://github.com/ericabuchanan), and [Brett Caswell](https://github.com/caswellbrett) ####
## Technology Stack

- **Frontend:**
  - Vue.js 3.4.15
  - Quasar 2.14.2

- **Backend:**
  - Python 3
  - Flask 3.0.1
  - MySQL
  - BeautifulSoup 4.12.3

## Getting Started

To run ScheduleSync locally, follow these steps:

1. Clone the repository:
```bash
$ git clone https://github.com/davenfroberg/schedule-sync.git
```
2. Create a virtual environment in root project directory and activate it:
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

3. Install dependencies and initialize the application:

```bash
# Install frontend dependencies
$ cd front
$ sudo npm i -g @quasar/cli
$ sudo npm install

# Install backend dependencies
$ cd back
$ pip install -r requirements.txt
```
4. Configure the database
   - Set up a MySQL database and put the credentials in a new file `config.py`:
```
  host = <host_name>
  port = <host_port>
  user = <db_username>
  password = <db_password>
  database = <db_name>
```

5. Run the application:
```bash
# Start frontend
$ cd front
$ quasar dev

# Start backend
$ cd back
$ python apis.py
```

## License ##
ScheduleSync is licensed under the MIT License. Feel free to use, modify, and distribute this software according to the terms of the license.
