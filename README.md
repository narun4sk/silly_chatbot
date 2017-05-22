## ChatBot example using Bottle, ChatterBot and Slack RTMBot

Clone the repo: `git clone https://github.com/narunask/silly_chatbot.git`

Prerequisites: [docker-ce](https://docs.docker.com/engine/installation/), [docker-compose](https://docs.docker.com/compose/install/)

To start all the components together please type the following commands:

```
cd silly_chatbot
docker-compose up
```

If instead you prefer to play with each of the component separately, then please `cd` into the appropriate directory and run `build.sh` or `run.sh` respectively. For instance to build and run the local `webui` do the following:

```
cd silly_chatbot/webui
./build.sh
./run.sh
```

Please use `@tellme` prefix with all the input.

To see available Bot commads type:

```
@tellme help
```

To see available Bots type:

```
@tellme list
```
