const AsciiTable = require('ascii-table')
import { getEloLeaderboard } from "../api"

export default async (msg) => {
    const leaderboard = await getEloLeaderboard()

    const table = new AsciiTable('Top 10 Players')
        .setHeading('', 'Name', 'ELO')
        .setHeadingAlignLeft()

    for (const user of leaderboard.leaderboard) {
        table.addRow(
            user.position,
            user.username,
            user.achievements.eloRating)
    }

    const response = `\`\`\`\n${table.toString()}\`\`\``

    msg.channel.send(response)
}
