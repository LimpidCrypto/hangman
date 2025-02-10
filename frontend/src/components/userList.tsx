import UserInput from "./userInput";

export default function UserList({ userCount }: { userCount: number }) {
    const userInputListItems = [];
    for (let i = 0; i < userCount; i++) {
        userInputListItems.push(<UserInput key={i} className={""} />);
    }

    return (
        <ul className="flex flex-col gap-6 justify-center w-full">
            {userInputListItems}
        </ul>
    );
}