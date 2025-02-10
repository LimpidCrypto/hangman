import { appConfig } from "./app";

export const routes = {
    backend: {
        games: `${appConfig.backendUrl}/games`,
        game: (id: string) => `${appConfig.backendUrl}/game/${id}`,
    }
}
