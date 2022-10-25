export default async (msg) => {
    const response = `Hey <@${msg.author.id}>,

Here's a list of things I can do:

\`$flux\` - Displays this month's Flux.
\`$bans\` - Displays this month's Specialist bans.
\`$leaderboard\` - Displays the top 10 players by rank.
\`$elo\` - Displays the top 10 players by ELO rating.
\`$guilds\` - Displays the top 10 guilds by total rank.
\`$dog\` - Dog.
\`$help\` - Displays this message again.

If you have any questions please contact a developer.`

    msg.channel.send(response);
}
