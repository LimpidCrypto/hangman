import UserInput from "./userInput";

export default function UserList({ userCount }: { userCount: number }) {
    const userInputListItems = [];
    for (let i = 0; i < userCount; i++) {
        userInputListItems.push(<UserInput key={i} className={"border-b-4"} />);
    }

    return (
        <ul className="flex flex-col justify-center w-full">
            {userInputListItems}
        </ul>
    );
}