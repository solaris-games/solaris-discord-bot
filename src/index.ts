import commands from "./commands";
import { extractCommandKey } from "./utils";

require('dotenv').config()

const Discord = require('discord.js')
const client = new Discord.Client()

process.on('SIGINT', async () => {
    console.log('Shutting down...');

    process.exit();
})

client.once('ready', async () => {
    console.log('Discord connection established.')
})

client.on('message', async (msg) => {
    if (msg.author.bot) { // Do not respond to bots.
        return
    }

    const key = extractCommandKey(msg)

    if (!key) {
        return
    }

    const command = commands[key]

    if (!command) {
        return
    }

    await command(msg)
})

console.log('Connecting to Discord...')
client.login(process.env.DISCORD_BOT_TOKEN)
