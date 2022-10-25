import { tryExecuteCommand } from "./responses/execute-command";
import { tryAutoEmbedGameLink } from "./responses/auto-embed-game-link";
import { tryReactToSuggestion } from "./responses/auto-react-to-suggestion";

const Discord = require('discord.js')
const client = new Discord.Client()

client.once('ready', async () => {
    console.log('Discord connection established.')
})

client.on('message', async (msg) => {
    if (msg.author.bot) { // Do not respond to bots.
        return
    }

    await tryExecuteCommand(msg)
    await tryReactToSuggestion(msg)
    await tryAutoEmbedGameLink(msg)
})

export default () => {
    console.log('Connecting to Discord...')
    client.login(process.env.DISCORD_BOT_TOKEN)
}
