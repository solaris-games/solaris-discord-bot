export const extractCommandKey = (msg) => {
    const match = msg.content.match(/^\$(\w+)/i)

    if (match && match.length) {
        return match[1] || null
    }

    return null
}
