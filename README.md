# Solaris Discord Bot

## Installation

Before you begin, run through the [discord.js](https://discordjs.guide/preparations/setting-up-a-bot-application.html#creating-your-bot) getting started guide to register a new Discord bot application and add it to your server.

Once you have created a bot, added it to your server and retrieved a bot token, you can proceed:

1. Install the prerequisites.
    - pip install -r requirements.txt
2. Clone the repository.
3. Checkout `master`.
4. Create a `.env` file in the root directory (See `.env.example`).
    - Add your Discord bot token to the `DISCORD_BOT_TOKEN` environment variable.
6. `python3 main.py` to start the bot.

Running via docker is also supported. Look at `docker-compose.yaml`.

## Adding new commands

1. Create a new command in `extensions`.


## Contributing
See [here](CONTRIBUTING.md).

## License
See [here](LICENSE).
