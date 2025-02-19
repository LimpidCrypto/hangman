import { UserWordsModel } from "../types";

export interface WordProps {
    word: UserWordsModel;
}

export function Word({ word }: WordProps) {
    let allLettersGuessed: string[] = [];
    if (word.letters_guessed_by && Object.keys(word.letters_guessed_by).length > 0) {
        allLettersGuessed = Object.values(word.letters_guessed_by).flat();
    }
    const wordLetters = word.word.split('');
    const wordLettersWithGuessed = wordLetters.map((letter) => {
        if (allLettersGuessed.includes(letter)) {
            return letter;
        } else {
            return '_ ';
        }
    });

    return (
        <div className="card">
            <h3 className="text-3xl">Word: {wordLettersWithGuessed}</h3>
        </div>
    );
}