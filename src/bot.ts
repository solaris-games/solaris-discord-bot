import commands from "./commands";
import { extractCommandKey } from "./utils";

const Discord = require('discord.js')
const client = new Discord.Client()

client.once('ready', async () => {
    console.log('Discord connection established.')
})

client.on('message', async (msg) => {
    if (msg.author.bot) { // Do not respond to bots.
        return
    }

    const key = extractCommandKey(msg) // Check if the message is a command

    if (!key) {
        return
    }

    const command = commands[key] // Check if the command exists

    if (!command) {
        return
    }

    await command(msg)
})

export default () => {
    console.log('Connecting to Discord...')
    client.login(process.env.DISCORD_BOT_TOKEN)
}
