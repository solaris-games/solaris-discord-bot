import { getGlobalLeaderboard } from "../api"
import { getBaseEmbedResponse } from "../utils"

export default async (msg) => {
    const leaderboard = await getGlobalLeaderboard()

    const usernameList = leaderboard.leaderboard.map(u => u.username + `\n`)
    const positionList = leaderboard.leaderboard.map(u => u.position + `\n`)
    const rankList = leaderboard.leaderboard.map(u => u.achievements.rank + `\n`)

    const response = getBaseEmbedResponse()

    response
        .setTitle(`Top 10 Players - Global`)
        .setURL(`https://solaris.games/#/leaderboard`)
        .addFields(
            { name: "Position", value: positionList, inline: true },
            { name: "Name", value: usernameList, inline: true },
            { name: "Rank", value: rankList, inline: true }
        )

    return msg.channel.send(response)
}
