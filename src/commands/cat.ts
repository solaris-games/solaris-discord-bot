import axios from "axios";

export default async (msg) => {
    try {
        const response = await axios.get('https://api.thecatapi.com/v1/images/search');

        const catLink = response.data[0].url;

        msg.channel.send(catLink);
    } catch (error) {
        console.error(error);
    }
}
