import { appConfig } from "./app";

export const routes = {
    backend: {
        games: `${appConfig.backendUrl}/games`,
        game: (id: string) => `${appConfig.backendUrl}/game/${id}`,
        pickWord: (gameId: string) => `${appConfig.backendUrl}/game/${gameId}/pick-word`,
        guessLetter: (gameId: string) => `${appConfig.backendUrl}/game/${gameId}/guess-letter`,
    },
    hangman: (step: number) => `/assets/${step}.png`
}
