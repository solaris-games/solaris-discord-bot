# Solaris Discord Bot

## Installation

Before you begin, run through the [discord.js](https://discordjs.guide/preparations/setting-up-a-bot-application.html#creating-your-bot) getting started guide to register a new Discord bot application and add it to your server.

Once you have created a bot, added it to your server and retrieved a bot token, you can proceed:

1. Install the prerequisites.
    - [Node.js](https://nodejs.org/en/) v14
2. Clone the repository.
3. Checkout `master`.
4. `npm install`
5. Create a `.env` file in the root directory (See `.env.example`).
    - Add your Discord bot token to the `DISCORD_BOT_TOKEN` environment variable.
6. `npm start` to start the bot.

## Adding new commands

1. Create a new command in `src/commands`.
2. Register it in `src/index.ts`.
    - Note that users can execute the command with the `$<command_name>` format, for example `$help`.

## Contributing
See [here](CONTRIBUTING.md).

## License
See [here](LICENSE).
