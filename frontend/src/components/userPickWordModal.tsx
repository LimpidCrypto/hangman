export interface UserPickWordModalProps {
    userToPickWord: string | null;
    onPickWord: (word: string) => void;
}

export function UserPickWordModal({ userToPickWord, onPickWord }: UserPickWordModalProps) {
    return (
        <dialog id="userPickWordModal" className="modal">
            <div className="modal-box">
                <h3>Please pick a word, {userToPickWord}!</h3>
                <input type="password" id="word" />
                <div className="modal-action">
                    <form onSubmit={(e) => {
                        e.preventDefault();
                        const word = (document.getElementById("word") as HTMLInputElement).value;
                        onPickWord(word);
                    }}
                    >
                        <button type="submit">Submit</button>
                    </form>
                </div>
            </div>
        </dialog>
    );
}