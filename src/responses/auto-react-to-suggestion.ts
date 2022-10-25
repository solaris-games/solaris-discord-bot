const SUGGESTION_CHANNEL_IDS = process.env.CHAT_IDS_SUGGESTIONS?.split(',') || []

export const tryReactToSuggestion = (msg) => {
    if (!SUGGESTION_CHANNEL_IDS.includes(msg.channel.id)) {
        return
    }

    msg.react('👍')
    msg.react('👎')
}