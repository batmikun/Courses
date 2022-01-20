import Head from "next/head";
import Link from "next/link";
import styles from "../styles/Home.module.css";

export default function Home() {
  return (
      <>    
        <Head>
            <title>List | HomePage</title>
            <meta name="keywords" /> 
        </Head>
        <div>
            <h1 className={ styles.title }>HomePage</h1>
            <p className={ styles.text }>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam iusto labore ratione deserunt nihil repellat tempora quis iure nobis velit.</p>
            <p className={ styles.text }>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam iusto labore ratione deserunt nihil repellat tempora quis iure nobis velit.</p>
            <Link href="/Listing">
                <a  className={ styles.btn }>See Listing</a>
            </Link>
        </div>
    </>
  )
}
