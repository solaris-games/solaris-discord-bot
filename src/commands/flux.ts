import { getFlux } from "../api"

export default async (msg) => {
    const authorId = msg.author.id

    const flux = await getFlux()

    let response = `Hey <@${authorId}>,

This month's flux is:

**${flux.description}**

*Flux changes on the 1st of every month, for information see the wiki.*`

    msg.channel.send(response)
}
