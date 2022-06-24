import styles from "../../styles/PasswordReset/passwordreset.module.css"
import Link from "next/link"
import { MdKeyboardArrowLeft, MdMail } from "react-icons/md"

const CheckMail = () => {

    return (
        <div className={styles.main}>
            
            <div className={styles.content_top}>
                <Link href="/auth/login">
                    <a className={styles.back_button}>
                        <MdKeyboardArrowLeft style={{ fontSize: "36px", color: "#000000"}}/> back
                    </a>
                </Link>
                
            </div>
            <div className={styles.content}>
                <div style={{ width: "140px", background: "#dfdddd", textAlign: "center", borderRadius: "16px", marginBottom: "50px" }}>
                    <MdMail style={{ fontSize: "100px", color: "#DF265E" }}/>
                </div>
                <h3>Check your mail</h3>
                <p>We have sent password instructions to your mail</p>
            </div>

        </div>
    )
}
export default CheckMail
