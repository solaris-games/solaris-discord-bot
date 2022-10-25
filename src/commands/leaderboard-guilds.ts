import { getGuildLeaderboard } from "../api"
import { getBaseEmbedResponse } from "../utils"

export default async (msg) => {
    const leaderboard = await getGuildLeaderboard()

    const nameList = leaderboard.leaderboard.map(g => `${g.name} [${g.tag}]\n`)
    const positionList = leaderboard.leaderboard.map(g => g.position + `\n`)
    const rankList = leaderboard.leaderboard.map(g => g.totalRank + `\n`)

    const response = getBaseEmbedResponse()

    response
        .setTitle(`Top 10 Guilds`)
        .setURL(`https://solaris.games/#/leaderboard`)
        .addFields(
            { name: "Position", value: positionList, inline: true },
            { name: "Guild", value: nameList, inline: true },
            { name: "Rank", value: rankList, inline: true }
        )

    return msg.channel.send(response)
}
