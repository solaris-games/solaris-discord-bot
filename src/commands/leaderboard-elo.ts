import { getEloLeaderboard } from "../api"
import { getBaseEmbedResponse } from "../utils"

export default async (msg) => {
    const leaderboard = await getEloLeaderboard()

    const usernameList = leaderboard.leaderboard.map(u => u.username + `\n`)
    const positionList = leaderboard.leaderboard.map(u => u.position + `\n`)
    const eloList = leaderboard.leaderboard.map(u => u.achievements.eloRating + `\n`)

    const response = getBaseEmbedResponse()

    response
        .setTitle(`Top 10 Players - ELO`)
        .setURL(`https://solaris.games/#/leaderboard`)
        .addFields(
            { name: "Position", value: positionList, inline: true },
            { name: "Name", value: usernameList, inline: true },
            { name: "ELO", value: eloList, inline: true }
        )

    return msg.channel.send(response)
}
