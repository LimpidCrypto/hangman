export interface UserPickWordModalProps {
    userToPickWord: string | null;
    onPickWord: (word: string) => void;
}

export function UserPickWord({ userToPickWord, onPickWord }: UserPickWordModalProps) {
    return (
        <div className="card">
            <h3>Please pick a word, {userToPickWord}!</h3>
            <div className="modal-action">
                <form onSubmit={(e) => {
                    e.preventDefault();
                    const word = (document.getElementById("word") as HTMLInputElement).value;
                    onPickWord(word);
                }}
                >
                    <input type="password" placeholder="Enter a word" id="word" className="input input-bordered" />
                    <button type="submit">Submit</button>
                </form>
            </div>
        </div>
    );
}