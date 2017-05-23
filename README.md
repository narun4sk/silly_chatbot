## ChatBot example using Bottle, ChatterBot and Slack RTMBot

Clone the repo: `git clone https://github.com/narunask/silly_chatbot.git`

Prerequisites: [docker-ce](https://docs.docker.com/engine/installation/), [docker-compose](https://docs.docker.com/compose/install/)

To start all the components together please type the following commands:

```
$ cd silly_chatbot
$ docker-compose up --build
```

Give it a minute to initialise and download its corpus files, then to see local `webui` navigate your browser to:

```
http://127.0.0.1:8000
````

#### Note

Please edit `silly_chatbot/rtmbot/app/rtmbot.conf` and modify `SLACK_TOKEN` parameter by adding valid hash, otherwise `rtmbot` will fail to start by throwing an error similar to the following:

```
rtmbot_1  | AttributeError: 'NoneType' object has no attribute 'recv'
```

---

If instead you prefer to play with each of the component separately, then please `cd` into the appropriate directory and run `build.sh` or `run.sh` respectively. For instance to build and run the local `webui` do the following:

```
$ cd silly_chatbot/webui
$ ./build.sh
$ ./run.sh
```
---

Please use `@tellme` prefix with all the input.

To see available Bot commads please type:

```
@tellme help
```

To see Bot list:

```
@tellme list
```

---

To run `unit-tests` please init virtual environment and install global requirements, then `cd` into the `app` directory and run `pytest -q`. Example:

```
$ cd silly_chatbot
$ virtualenv -p python3 env
$ pip install -r requirements.txt
$ cd rtmbot/app
$ pytest -q
......
6 passed in 0.25 seconds
```
