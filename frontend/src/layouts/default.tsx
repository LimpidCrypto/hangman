import Header from "../components/common/header";

export default function DefaultLayout({ children }: { children: React.ReactNode }) {
    return (
        <body className="flex flex-col min-h-screen gap-4">
            <Header />
            <main className="flex flex-col justify-center lg:w-1/2 w-full mx-auto">
                {children}
            </main>
        </body>
    );
}