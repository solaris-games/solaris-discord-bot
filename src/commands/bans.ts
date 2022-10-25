import { getBans } from "../api"

export default async (msg) => {
    const authorId = msg.author.id

    const bans = await getBans()

    const starBans = bans.star.map(s => `- ${s.name}`).join('\n')
    const carrBans = bans.carrier.map(s => `- ${s.name}`).join('\n')
    const specStarBans = bans.specialStar.map(s => `- ${s.name}`).join('\n')

    let response = `Hey <@${authorId}>,
    
This month's bans are as follows:

__Star specialists__
${starBans}

__Carrier specialists__
${carrBans}

__Special stars__
${specStarBans}

*The ban list affects official games only and changes on the 1st of every month, for information see the wiki.*`

    return msg.channel.send(response)
}
