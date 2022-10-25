const AsciiTable = require('ascii-table')
import { getGuildLeaderboard } from "../api"

export default async (msg) => {
    const leaderboard = await getGuildLeaderboard()

    const table = new AsciiTable('Top 10 Guilds')
        .setHeading('', 'Name', 'Rank')
        .setHeadingAlignLeft()

    for (const guild of leaderboard.leaderboard) {
        table.addRow(
            guild.position,
            `${guild.name} [${guild.tag}]`,
            guild.totalRank)
    }

    const response = `\`\`\`\n${table.toString()}\`\`\``

    msg.channel.send(response)
}
