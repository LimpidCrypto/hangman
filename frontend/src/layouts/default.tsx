import Header from "../components/common/header";

export default function DefaultLayout({ children }: { children: React.ReactNode }) {
    return (
        <body className="flex flex-col min-h-screen gap-6">
            <Header />
            <main className="flex flex-col gap-6 justify-center lg:w-1/2 w-full mx-auto">
                {children}
            </main>
        </body>
    );
}