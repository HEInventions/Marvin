# Marvin
The slackbot that makes sure your team isn't slacking.

Marvin is a tool that collates all open and non-wip merge requests so you can put them in your channel.

Currently the usage is mega basic

```
@marvin MR
```

And you'll get a big list of titles and web urls in your slack channel

## Installation

Marvin is dockerised and just expects some environment variables to run, which are:
```
GITLAB_URL
GITLAB_TOKEN
SLACK_BOT_TOKEN
BOT_ID
```

You can get ```BOT_ID``` by running ```print_bot_id.py``` 

When you have all of your environment variables sorted in a key=value file (or you have readied your choice of putting ENVs in docker) run:

```docker
docker run --env-file=/srv/marvin/marvin.env --name marvin registry.gitlab.com/heinventions/marvin:latest
```