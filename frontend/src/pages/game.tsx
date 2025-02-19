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
        return <DefaultLayout><Scoreboard game={game} /></DefaultLayout>
    }
    const gameId = game.id;
    const userToPick = game.user_to_pick;
    const userToGuess = game.user_to_guess;
    const guessedLettersOfAllUsers = game.user_words.map((word) => {
        if (word.letters_guessed_by && Object.keys(word.letters_guessed_by).length > 0) {
            return Object.values(word.letters_guessed_by).flat();
        }
        return [];
    }).flat();
    let falselyGuessedLetters = 0;
    guessedLettersOfAllUsers.forEach((letter) => {
        const currentWord = game.user_words[game.user_words.length - 1] && game.user_words[game.user_words.length - 1].word;
        if (!currentWord.includes(letter)) {
            falselyGuessedLetters++;
        }
    })
    console.log(falselyGuessedLetters);


    return (
        <DefaultLayout>
            {game && <Scoreboard game={game} />}
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
                userToGuess && <div>
                    <img src={routes.hangman(falselyGuessedLetters)} alt="Hangman" />
                    <Word word={game.user_words[game.user_words.length - 1]} />
                    <LetterInput gameId={gameId} userToGuess={userToGuess} guessedLetters={guessedLettersOfAllUsers} setGame={setGame} />
                </div>
            }
        </DefaultLayout >
    );
}
