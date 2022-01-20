import Link from "next/link";
import Image from "next/image";

const NavBar = () => {
    return ( 
        <nav>
            <div className="logo">
                <Image src="/logo.png" alt="Logo" width = {200} height = {77} />
            </div>
            <Link href="/">
                <a>Home</a>
            </Link>
            <Link href="/about">
                <a>About</a>
            </Link>
            <Link href="/user">
                <a>Users</a>
            </Link>
        </nav>
     );
}
 
export default NavBar;