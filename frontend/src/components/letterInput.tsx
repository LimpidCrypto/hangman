import { routes } from "../config/routes";

export interface LetterInputProps {
    gameId: string;
    userToGuess: string;
    setGame: (game: any) => void;
}

export function LetterInput({ gameId, userToGuess, setGame }: LetterInputProps) {
    const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split('');
    return (
        <>
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
                    }>
                        {letter}
                    </button>
                ))}
            </div>
        </>
    )
}