import { useEffect, useState } from "react";
import DefaultLayout from "../layouts/default";
import { GameModel } from "../types";
import { routes } from "../config/routes";
import { UserPickWord } from "../components/userPickWordModal";
import { LetterInput } from "../components/letterInput";
import { Word } from "../components/word";
import { Scoreboard } from "../components/scoreboard";

function fetchGame(gameId: string) {
    return fetch(routes.backend.game(gameId))
        .then(res => res.json())
}

export function GamePage() {
    const [game, setGame] = useState<GameModel | null>(null);

    useEffect(() => {
        const gameId = window.location.pathname.split('/').pop();
        fetchGame(gameId ?? "")
            .then(setGame)
    }, []);
    console.log(game);


    if (!game) {
        return <DefaultLayout>Loading...</DefaultLayout>
    }
    if (game.user_to_pick == null && game.user_to_guess == null) {
        return <DefaultLayout>
            <a href="/"><button className="btn btn-warning" type="button">New Game</button></a>

            <Scoreboard game={game} />
        </DefaultLayout>
    }
    const gameId = game.id;
    const userToPick = game.user_to_pick;
    const userToGuess = game.user_to_guess;
    const currentWord = game.user_words[game.user_words.length - 1] ? game.user_words[game.user_words.length - 1] : null;
    const guessedLettersOfAllUsers = currentWord?.letters_guessed_by && Object.keys(currentWord?.letters_guessed_by).length > 0 ? Object.values(currentWord?.letters_guessed_by).flat() : []
    let falselyGuessedLetters = 0;
    guessedLettersOfAllUsers.forEach((letter) => {
        console.log("currentWord", currentWord);

        if (!currentWord?.word.includes(letter)) {
            falselyGuessedLetters++;
        }
    })

    return (
        <DefaultLayout>
            {game && <div>
                <a href="/"><button className="btn btn-warning mb-4" type="button">Reset Game</button></a>
                <Scoreboard game={game} />
            </div>}
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

            {
                userToGuess && <div className="flex flex-col gap-2 items-center">
                    <Word word={game.user_words[game.user_words.length - 1]} />
                    <div className="flex flex-row gap-2 items-center">
                        {falselyGuessedLetters > 0 && <div className="overflow-hidden max-w-[400px]">
                            <img src={routes.hangman(falselyGuessedLetters)} alt="Hangman" className="invert" />
                        </div>}
                        <LetterInput gameId={gameId} userToGuess={userToGuess} guessedLetters={guessedLettersOfAllUsers} setGame={setGame} />
                    </div>
                </div>
            }
        </DefaultLayout >
    );
}
