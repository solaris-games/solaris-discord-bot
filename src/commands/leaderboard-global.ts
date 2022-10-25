const AsciiTable = require('ascii-table')
import { getGlobalLeaderboard } from "../api"

export default async (msg) => {
    const leaderboard = await getGlobalLeaderboard()

    const table = new AsciiTable('Top 10 Players')
        .setHeading('', 'Name', 'Rank')
        .setHeadingAlignLeft()

    for (const user of leaderboard.leaderboard) {
        table.addRow(
            user.position,
            user.username,
            user.achievements.rank)
    }

    const response = `\`\`\`\n${table.toString()}\`\`\``

    msg.channel.send(response)
}
