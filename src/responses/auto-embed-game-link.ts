import { getGameInfo } from "../api";
import { extractGameLinkId, getBaseEmbedResponse } from "../utils";

export const tryAutoEmbedGameLink = async (msg) => {
    const gameLinkId = extractGameLinkId(msg)

    if (!gameLinkId) {
        return
    }

    const game = await getGameInfo(gameLinkId)

    const response = getBaseEmbedResponse()

    response
        .setTitle(game.settings.general.name)
        .setDescription(game.settings.general.description)
        .setURL(`https://solaris.games/#/game/detail?id=${gameLinkId}`)
        .addFields(
            {
                name: 'Mode',
                value: getGameModeFriendlyText(game),
                inline: true
            },
            {
                name: 'Type',
                value: getGameTypeFriendlyText(game),
                inline: true
            },
            {
                name: 'Players',
                value: `${game.state.players}/${game.settings.general.playerLimit}`,
                inline: true
            },
        )

    msg.channel.send(response)
}

const getGameTypeFriendlyText = (game) => {
    return {
      'tutorial': 'Tutorial',
      'new_player_rt': 'New Players',
      'standard_rt': 'Standard',
      'standard_tb': 'Standard - TB',
      '1v1_rt': '1 vs. 1',
      '1v1_tb': '1 vs. 1 - TB',
      '32_player_rt': '32 Players',
      'custom': 'Custom',
      'special_dark': 'Dark Galaxy',
      'special_ultraDark': 'Ultra Dark Galaxy',
      'special_orbital': 'Orbital',
      'special_battleRoyale': 'Battle Royale',
      'special_homeStar': 'Capital Stars',
      'special_homeStarElimination': 'Elimination',
      'special_anonymous': 'Anonymous',
      'special_kingOfTheHill': 'King Of The Hill',
      'special_tinyGalaxy': 'Tiny Galaxy',
      'special_freeForAll': 'Free For All',
      'special_arcade': 'Arcade'
    }[game.settings.general.type]
}

const getGameModeFriendlyText = (game) => {
    return {
        'conquest': 'Conquest',
        'battleRoyale': 'Battle Royale',
        'kingOfTheHill': 'King of the Hill'
    }[game.settings.general.mode]
}
