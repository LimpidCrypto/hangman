import { useState } from "react";
import { routes } from "../config/routes";

export interface LetterInputProps {
    gameId: string;
    userToGuess: string;
    guessedLetters: string[];
    setGame: (game: any) => void;
}

export function LetterInput({ gameId, userToGuess, guessedLetters, setGame }: LetterInputProps) {
    if (!userToGuess) {
        return null;
    }

    const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split('');
    return (
        <div className="flex flex-col gap-4">
            <h3 className="text-xl">It's <b>{userToGuess}</b> turn to guess</h3>
            <div className="letter-input grid grid-flow-row grid-cols-4 gap-6">
                {alphabet.map((letter) => (
                    <button key={letter} className="letter-button btn" onClick={() =>
                        fetch(routes.backend.guessLetter(gameId), {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({ guessed_by: userToGuess, letter: letter })
                        })
                            .then(res => res.json())
                            .then((game) => {
                                setGame(game);
                            })
                    }
                        disabled={guessedLetters.includes(letter)}
                    >
                        {letter}
                    </button>
                ))}
            </div>
        </div>
    )
}