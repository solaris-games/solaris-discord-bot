import { getBans } from "../api";

export default async (msg) => {
    const authorId = msg.author.id

    const bans = await getBans()

    const starBans = bans.star.map(s => `- ${s.name}\n`).join('')
    const carrBans = bans.carrier.map(s => `- ${s.name}\n`).join('')
    const specStarBans = bans.specialStar.map(s => `- ${s.name}\n`).join('')

    let response = `Hey <@${authorId}>,\n\nThis month's bans are as follows.\n\nStar specialists:\n${starBans}\n\nCarrier specialists:\n${carrBans}\n\Special stars:\n${specStarBans}\n\nThe ban list affects official games only and changes on the 1st of every month, for information see the wiki.`

    return msg.channel.send(response)
}
