const Discord = require('discord.js')

export const extractCommandKey = (msg) => {
    const match = msg.content.match(/^\$(\w+)/i)

    if (match && match.length) {
        return match[1] || null
    }

    return null
}

export const extractGameLinkId = (msg) => {
    const match = msg.content.match(/https:\/\/solaris\.games\/#\/game(?:\/detail)?\?id=(\w+)/i)

    if (match && match.length) {
        return match[1] || null
    }

    return null
}

export const getBaseEmbedResponse = () => new Discord.MessageEmbed()
    .setURL(`https://solaris.games`)
    .setAuthor(`Solaris`)
