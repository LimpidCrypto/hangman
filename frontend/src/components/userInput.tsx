import clsx from "clsx";

export default function UserInput({ className }: { className: string }) {
    return (
        <input required type="text" placeholder="Enter a username" className={clsx("input w-full", className)} name="username" />
    )
}
