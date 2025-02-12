export type GameType = "player_vs_player" | "player_vs_cpu";

export interface UserWordsModel {
    user: string;
    word: string;
    letters_guessed: string[];
}

export interface GameModel {
    id: string;
    type: GameType;
    users: string[];
    user_words: UserWordsModel[];
    user_scores: Record<string, number>;
    difficulty?: number;
    user_to_pick?: string;
    user_to_guess?: string;
}