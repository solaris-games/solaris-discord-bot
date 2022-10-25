import startBot from './bot'

require('dotenv').config()

process.on('SIGINT', async () => {
    console.log('Shutting down...');

    process.exit();
})

startBot()
