import { useEffect, useState } from "react";
import DefaultLayout from "../layouts/default";
import { GameModel } from "../types";
import { routes } from "../config/routes";
import { UserPickWord } from "../components/userPickWordModal";
import { LetterInput } from "../components/letterInput";

export function GamePage() {
    const [game, setGame] = useState<GameModel | null>(null);

    useEffect(() => {
        const gameId = window.location.pathname.split('/').pop();
        fetch(routes.backend.game(gameId ?? ""))
            .then(res => res.json())
            .then(setGame)
    }, []);
    console.log(game);


    if (!game) {
        return <DefaultLayout>Loading...</DefaultLayout>
    }
    if (game.user_to_pick == null && game.user_to_guess == null) {
        return <DefaultLayout>End?</DefaultLayout>
    }
    const gameId = game.id;
    const userToPick = game.user_to_pick;
    const userToGuess = game.user_to_guess;

    return (
        <DefaultLayout>
            <h2>Game Page</h2 >
            {game && (
                <div>
                    <h2>Game ID: {game.id}</h2>
                    <h2>Game Type: {game.type}</h2>
                    <h2>Users: {game.users.join(', ')}</h2>
                </div>
            )}

            {userToPick && <UserPickWord userToPickWord={userToPick} onPickWord={(word) => {
                fetch(routes.backend.pickWord(game?.id ?? ""), {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ word: word, picked_by: userToPick })
                })
                    .then(res => res.json())
                    .then(setGame)
            }} />}
            {userToGuess && <LetterInput gameId={gameId} userToGuess={userToGuess} setGame={setGame} />}
        </DefaultLayout >
    );
}
