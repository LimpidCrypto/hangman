import { GameModel } from "../types";

export interface ScoreboardProps {
    game: GameModel;
}

export function Scoreboard({ game }: ScoreboardProps) {
    const sortedScores = Object.entries(game.user_scores).sort((a, b) => b[1] - a[1]);
    return (
        <div className="flex flex-col gap-2 border border-gray-700 rounded-lg p-4">
            <h4 className="font-bold">Scoreboard</h4>
            <table className="table table-zebra">
                <thead>
                    <tr>
                        <th>Player</th>
                        <th>Score</th>
                    </tr>
                </thead>
                <tbody>
                    {sortedScores.map(([username, score]) => (
                        <tr key={username}>
                            <td>{username}</td>
                            <td>{score}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}