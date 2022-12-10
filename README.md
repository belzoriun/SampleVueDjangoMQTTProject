# Setting things up
## Install dependencies
Run the command ```npm i``` to install all projects dependencies
### Common issues
- can't fins npm: please make sur you have nodejs installed on your device. Check if it is by taping the command ```node -v``` in a terminal or console. It it is not, ilstall it here : https://nodejs.org/dist/v18.12.1/node-v18.12.1-x64.msi
## Babel configuration
Babel should be configured directly when the project is open.
### Common issues
- Can't find a babel configuration file: Go to ```file>preferences>settings```, type in ```eslint``` int eh search bar and click the ```edit in settings.json``` link. Then paste the followinf code on the json root 
```
    "eslint.options": {
        "configFile": "ABOLUTE\PATH\TO\PROJECT\ROOT\ui\babel.config.js"
    }
```
## Initialise the database
Got to the ```backend``` folder, then type in ```python playmigrations.py``` in a terminal or console, when completed, a db.sqlite3 file should appear. If this file was present, run the command too, as it ensure you have the latest version of the database.

### Common issues
- python does not exist: please ensure you have ```python 3.0``` or later installed on your device.
- error while running migrations: please create an issue on github explaining the reproduction steps and giving the error's stacktrace, and rollback to an older version of the tool. I'll fix it asap. 

### A wise man once said ...
Make a backup of your database before you run a new version of the tool's migrations. I am not responsible of you loosing your data. If it happens, please create a github issue.

If I'm not too lazy, i'll make a backup system. (But that's a <b>TODO</b>)

# Run the project
## Developement mode
### Setting env
*This part is still WIP, there's nothin to look at.*
### The ui
Go to ```app\ui```, and run ```npm run serve```.

You should have a Node server running holding the ui.
### The backend
Go to ```app\backend``` and run ```python manage.py runserver```. 

You should have a running backend.

## Production mode
*This part is still WIP, there's nothin to look at.*