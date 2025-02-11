import { appConfig } from "./app";

export const routes = {
    backend: {
        games: `${appConfig.backendUrl}/games`,
        game: (id: string) => `${appConfig.backendUrl}/game/${id}`,
        userToPick: (gameId: string) => `${appConfig.backendUrl}/game/${gameId}/user-to-pick`,
        pickWord: (gameId: string) => `${appConfig.backendUrl}/game/${gameId}/pick-word`,
    }
}
