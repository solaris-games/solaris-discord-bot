import axios from "axios";

export default async (msg) => {
    const response = await axios.get('https://dog.ceo/api/breeds/image/random')

    msg.channel.send(response.data.message)
}
