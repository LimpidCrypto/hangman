import { useEffect, useState } from "react";
import DefaultLayout from "../layouts/default";
import { GameModel } from "../types";
import { routes } from "../config/routes";
import { UserPickWordModal } from "../components/userPickWordModal";

async function handleGetUserToPickWord(gameId: string) {
    const res = await fetch(routes.backend.userToPick(gameId));
    const user = await res.json();

    return user.user_to_pick;
}

export function GamePage() {
    const [game, setGame] = useState<GameModel | null>(null);
    const [userToPickWord, setUserToPickWord] = useState<string | null>(null);
    const [word, setWord] = useState<string | null>(null);

    useEffect(() => {
        const gameId = window.location.pathname.split('/').pop();
        fetch(routes.backend.game(gameId ?? ""))
            .then(res => res.json())
            .then(setGame)
    }, [userToPickWord]);
    useEffect(() => {
        if (!game) {
            return;
        }
        fetch(routes.backend.userToPick(game?.id ?? ""))
            .then(res => res.json())
            .then((user) => {
                if (user == null) {
                    // todo: game over
                    return;
                } else if (user.user_to_pick == null) {
                    // todo: ongoing game
                } else {
                    // new user to pick
                    console.log(user);

                    setUserToPickWord(user.user_to_pick.toString());
                    (document.getElementById("userPickWordModal") as any).showModal();
                }
            })
    }, [game]);


    return (
        <DefaultLayout>
            <UserPickWordModal userToPickWord={userToPickWord} onPickWord={(word) => {
                setWord(word);
                fetch(routes.backend.pickWord(game?.id ?? ""), {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ word: word, picked_by: userToPickWord })
                })
                    .then(() => {
                        (document.getElementById("userPickWordModal") as any).close();
                    });
            }} />
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
