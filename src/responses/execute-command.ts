import { extractCommandKey } from "../utils"
import commands from "../commands";

export const tryExecuteCommand = async (msg) => {
    const key = extractCommandKey(msg) // Check if the message is a command

    if (!key) {
        return
    }

    const command = commands[key] // Check if the command exists

    if (!command) {
        return
    }

    await command(msg)
}
