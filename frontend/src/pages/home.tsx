import { useState } from "react";
import UserList from "../components/userList";
import DefaultLayout from "../layouts/default";
import { routes } from "../config/routes";
import { None, Option } from "ts-results";
import { appConfig } from "../config/app";

const handleUserFormSubmit = async (event: React.FormEvent<HTMLFormElement>): Promise<Option<string>> => {
    event.preventDefault();
    const usernameInputs: NodeListOf<HTMLInputElement> = document.querySelectorAll('input[name="username"]');

    const response = await fetch(routes.backend.users, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ usernames: Array.from(usernameInputs).map((input: HTMLInputElement) => input.value) }),
    });
    console.log('Form submitted');
    return None;
}

export default function Home() {
    const [userCount, setUserCount] = useState(2);

    return (
        <DefaultLayout>
            <div className="flex gap-4">
                <button
                    className="btn btn-success" onClick={() => { setUserCount(userCount + 1) }}>Add User</button>
                <button className="btn btn-error" onClick={() => {
                    if (userCount > 2) {
                        setUserCount(userCount - 1)
                    }
                }}>Remove User</button>
            </div>
            <form method="POST" onSubmit={handleUserFormSubmit} className="flex flex-col gap-4" >
                <UserList userCount={userCount} />
                <button className="btn" disabled={userCount < 2}>Start Game</button>
                <span hidden={userCount > 1}>You need at least 2 players to start</span>
            </form>
        </DefaultLayout >
    );
}
