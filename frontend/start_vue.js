import { createServer } from 'vite'

async function startServer() {
  const server = await createServer({
    configFile: './vite.config.js'
  })
  await server.listen()
  server.printUrls()
}

startServer()
