import { useState } from "react";
import UserList from "../components/userList";
import DefaultLayout from "../layouts/default";
import { routes } from "../config/routes";
import { None, Option, Some } from "ts-results";
import { GameType } from "../types";

const handleUserFormSubmit = async (event: React.FormEvent<HTMLFormElement>): Promise<Option<string>> => {
    event.preventDefault();
    const form: HTMLFormElement = event.currentTarget;
    const usernameInputs: NodeListOf<HTMLInputElement> = form.querySelectorAll('input[name="username"]');
    const gameTypeInput: HTMLInputElement | null = form.querySelector('input[name="game-type"]:checked');
    if (gameTypeInput === null) {
        return Some('Please select a game type');
    }

    const usernames = Array.from(usernameInputs).map((input: HTMLInputElement) => input.value);

    // Validate unique usernames
    if (new Set(usernames).size !== usernames.length) {
        return Some('Usernames must be unique');
    }

    const response = await fetch(routes.backend.games, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ usernames: usernames, game_type: gameTypeInput.value as GameType }),
    });
    console.log('Form submitted');
    return None;
}

export default function Home() {
    const [userCount, setUserCount] = useState(2);
    const [error, setError] = useState<Option<string>>(None);

    return (
        <DefaultLayout>
            <form method="POST" onSubmit={async (e) => setError(await handleUserFormSubmit(e))} className="flex flex-col gap-4" >
                <div className="card">
                    <div className="card-body gap-6">
                        <h2 className="card-title">Enter your Usernames</h2>
                        <div className="flex gap-6">
                            <button
                                type="button" className="btn btn-success" onClick={() => { userCount <= 4 && setUserCount(userCount + 1) }}>Add User</button>
                            <button type="button" className="btn btn-error" onClick={() => {
                                if (userCount > 2) {
                                    setUserCount(userCount - 1)
                                }
                            }}>Remove User</button>
                        </div>
                        <div className="card-actions">
                            <UserList userCount={userCount} />
                        </div>
                    </div>
                </div>
                <div className="card">
                    <div className="card-body">
                        <h2 className="card-title">Select the Game Mode</h2>
                        <div className="card-actions">
                            <label className="radio-label" htmlFor="radio-player-vs-player">Player vs. Player</label>
                            <input type="radio" name="game-type" id="radio-player-vs-player" className="radio" checked value={"player_vs_player" as GameType} />
                            <label className="radio-label" htmlFor="radio-player-vs-cpu">Players vs. Computer</label>
                            <input type="radio" name="game-type" id="radio-player-vs-cpu" className="radio" value={"player_vs_cpu" as GameType} />
                        </div>
                    </div>
                </div>
                <button className="btn" disabled={userCount < 2}>Start Game</button>
                <span hidden={userCount > 1}>You need at least 2 players to start</span>
            </form>
            {error !== None && <div className="alert alert-error">{error.unwrap()}</div>}
        </DefaultLayout >
    );
}
