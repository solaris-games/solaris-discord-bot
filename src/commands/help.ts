export default async (msg) => {
    const response = `Hey <@${msg.author.id}>,\nPlease visit https://github.com/solaris-games/solaris/blob/master/server/bots/discord/README.md for help on how to interact with me.`

    return msg.channel.send(response);
}
