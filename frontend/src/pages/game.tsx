import { useEffect, useState } from "react";
import DefaultLayout from "../layouts/default";
import { GameModel } from "../types";
import { routes } from "../config/routes";

export function GamePage() {
    const [game, setGame] = useState<GameModel | null>(null);
    const [userToPickWord, setUserToPickWord] = useState<string | null>(null);

    useEffect(() => {
        const gameId = window.location.pathname.split('/').pop();
        fetch(routes.backend.game(gameId ?? ""))
            .then(res => res.json())
            .then(setGame)
    }, []);

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
        </DefaultLayout >
    );
}
