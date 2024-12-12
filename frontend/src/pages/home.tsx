import UserInput from "../components/userInput";

export default function Home() {
    return (
        <div className="flex flex-col justify-center">
            <h1 className="font-red">Hangman</h1>
            <UserInput />
        </div>
    );
}
