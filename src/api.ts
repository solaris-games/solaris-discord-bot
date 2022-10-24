import axios from 'axios'

const get = async (url: string) => {
    const response = await axios.get(url)

    if (response.status !== 200) {
        console.error(response.data)

        throw new Error(`GET ${url} failed with status ${response.status}.`)
    }

    return response.data
}

export const getBans = () => get(`${process.env.SOLARIS_API_BASE_URL}/api/game/specialists/bans`)
export const getFlux = () => get(`${process.env.SOLARIS_API_BASE_URL}/api/game/flux`)
export const getGameInfo = (gameId: string) => get(`${process.env.SOLARIS_API_BASE_URL}/api/game/${gameId}/info`)
export const getGlobalLeaderboard = () => get(`${process.env.SOLARIS_API_BASE_URL}/api/user/leaderboard?limit=10&sortingKey=rank`)
// TODO: Need an API endpoint to search by username
export const getUserAchievements = (userId: string) => get(`${process.env.SOLARIS_API_BASE_URL}/api/user/achievements/${userId}`)
