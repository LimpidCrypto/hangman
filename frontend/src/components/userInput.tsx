import clsx from "clsx";

export default function UserInput({ className }: { className: string }) {
    return (
        <input required type="text" max={15} min={1} placeholder="Enter a username" className={clsx("input input-bordered w-full", className)} name="username" />
    )
}
