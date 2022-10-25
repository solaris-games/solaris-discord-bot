require('dotenv').config()

import startBot from './bot'

process.on('SIGINT', async () => {
    console.log('Shutting down...');

    process.exit();
})

startBot()
