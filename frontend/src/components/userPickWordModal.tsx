export interface UserPickWordModalProps {
    userToPickWord: string | null;
    onPickWord: (word: string) => void;
}

export function UserPickWord({ userToPickWord, onPickWord }: UserPickWordModalProps) {
    return (
        <div className="card">
            <div className="card-body">
                <h3 className="text-xl">Please pick a word <b>{userToPickWord}</b>!</h3>
                <form onSubmit={(e) => {
                    e.preventDefault();
                    const word = (document.getElementById("word") as HTMLInputElement).value;
                    onPickWord(word);
                }}
                    className="flex flex-row gap-6"
                >
                    <input type="password" placeholder="Enter a word" id="word" className="input input-bordered" />
                    <button type="submit" className="btn btn-success">Submit</button>
                </form>
            </div>
        </div>
    );
}