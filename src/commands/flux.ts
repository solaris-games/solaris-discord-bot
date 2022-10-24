import { getFlux } from "../api";

export default async (msg) => {
    const authorId = msg.author.id

    const flux = await getFlux()

    let response = `Hey <@${authorId}>,\n\nThis month's flux is:\n\n*${flux.description}*\n\nFlux changes on the 1st of every month, for information see the wiki.`

    return msg.channel.send(response)
}
