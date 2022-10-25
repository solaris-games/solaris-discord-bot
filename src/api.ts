import axios from 'axios'

const get = async (url: string) => {
    const response = await axios.get(`${process.env.SOLARIS_API_BASE_URL}/${url}`)

    if (response.status !== 200) {
        console.error(response.data)

        throw new Error(`GET ${url} failed with status ${response.status}.`)
    }

    return response.data
}

export const getBans = () => get(`game/specialists/bans`)
export const getFlux = () => get(`game/flux`)
export const getGameInfo = (gameId: string) => get(`game/${gameId}/info`)
export const getGlobalLeaderboard = () => get(`user/leaderboard?limit=10&sortingKey=rank`)
export const getEloLeaderboard = () => get(`user/leaderboard?limit=10&sortingKey=elo-rating`)
export const getGuildLeaderboard = () => get(`guild/leaderboard?limit=10&sortingKey=totalRank`)
