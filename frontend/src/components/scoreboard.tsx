import { GameModel } from "../types";

export interface ScoreboardProps {
    game: GameModel;
}

export function Scoreboard({ game }: ScoreboardProps) {
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
                    {game.users.map((user) => (
                        <tr key={user}>
                            <td className="text-center">{user}</td>
                            <td className="text-center">{game.user_scores[user]}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}