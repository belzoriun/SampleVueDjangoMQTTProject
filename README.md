# The Sensall project
As said earlier, this project is ment to be use as a sensor dashboard, where you can see in real time, sensors connected via the WQTT protocol.

By the time I'm writing this, websockets are not yet supported. Don't hesitate to post a discussion or te react to an existing discussion about that on this github. If you really want it I'll think about it.
## The genesis
At first, this project was made to impress some recruiters for a job, but I said to myself "what about make a REAL project", then I made it.

Thats it, don't look any further.
## The ~~bugs~~ features
With this tool, you have acces to
- The sensors you registered and the one poeple shared with you (and only those)
- The informations these sensors are sending via MQTT (cf. `The Sensall project`)
- Some actions on sensors when possible (ie. a relay you can activate remotely)
- statistics on multiple sensors to compare their fiability or data

There is yet no data encryption and there likely to never will be. (We are using MQTT, who cares about security anyway ?)

About statistics on sensors
- Simple data evolution chart
- A chart with some hue shift depending on data
- Sensor location
- Pie chart of the amount of data some sensor sent
- Pie chart of the data of some sensors

All these are (in addition to being the only ones planed for now) in real time and complitely customizable.

If you have any idea of another stat I can add to the tool, I'll be glad to answer you I dan't have time for this.

Jokes appart, don't hesitate to, as always, create a discussion or react to an existing one here.

## Feel free ~~not~~ to ask anything
Don't hesitate, I promise I don't bite, but I'm not a chatbot, I'll answer when I'll have time.

If you have critical questions about the project, or just want to discuss around web apps or other computer science stuff, feel free to join me over on [discord](https://discord.gg/aBQD9g3VWJ).

Oh, and if, by chance, you're hireing, come over on discord as well, I'm sure I can help you in your search.

# Setting things up
Wellcome to this project.

This was all made by me, and is a tool I created to manage some sensors ans display some info about them.

You can use, copy and modify this code as much as you want.

Check below to get started.
## Requirements
- `python 3.8` or later
- `Node.js 18.12` or later
- some sensors connected to an MQTT broker
## Install dependencies
Go to the `ui` folder and run the command `npm i` to install all ui project's dependencies

Go to `app\backend` and run the command `pip install -r requirements.txt` to install all backend project's dependencies
### Common issues
- can't find pip: please ensure you have `python 3.0` or later installed on your device.
- can't fins npm: please make sur you have nodejs installed on your device. Check if it is by taping the command `node -v` in a terminal or console. It it is not, ilstall it here : https://nodejs.org/dist/v18.12.1/node-v18.12.1-x64.msi
## Babel configuration
Babel should be configured directly when the project is open.
### Common issues
- Can't find a babel configuration file: Go to `file>preferences>settings`, type in `eslint` int eh search bar and click the `edit in settings.json` link. Then paste the followinf code on the json root 
```json
    "eslint.options": {
        "configFile": "ABOLUTE\\PATH\\TO\\PROJECT\\ROOT\\ui\\babel.config.js"
    }
```
## Initialise the database
Got to `app\backend`, then type in `python playmigrations.py` in a terminal or console, when completed, a db.sqlite3 file should appear. If this file was present, run the command too, as it ensure you have the latest version of the database.

!!! DO NOT in any case alter the migration files, as it can lead to errors or, in the worst case scenario, data loss !!!

If you really have to change a migration file, it means you've done something wrong.

### Common issues
- python does not exist: please ensure you have `python 3.8` or later installed on your device.
- error while running migrations: please create an issue on github explaining the reproduction steps and giving the error's stacktrace, and rollback to an older version of the tool. I'll fix it asap. 

### A wise man once said ...
Make a backup of your database before you run a new version of the tool's migrations. I am not responsible of you loosing your data. If it happens, please create a github issue.

If I'm not too lazy, i'll make a backup system. (But that's a <b>TODO</b>)

# Run the project
## Developement mode
### Setting env
*This part is still WIP, there's nothin to look at.*
### The ui
Go to the `ui` folder, and run `npm run serve`.

You should have a Node server running holding the ui.
### The backend
Go to `app\backend` and run `python manage.py runserver`. 

You should have a running backend.

## Production mode
*This part is still WIP, there's nothin to look at.*