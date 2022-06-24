import ForgotPasswordForm from "../../components/Auth/ForgotPasswordForm";
import Link from "next/link";
import MainLayout from "../../components/Layout/MainLayout";
import { MdKeyboardArrowLeft } from "react-icons/md";
//import reportWebVitals from './reportWebVitals';
import styles from "../../styles/PasswordReset/passwordreset.module.css";
import CheckMail from "../../components/PasswordReset/checkMail";
import { useState } from "react";

export default function Login() {
  const [checkmail, setCheckMail] = useState<Boolean>(false);

  return (
    <MainLayout title="Forgot Password">
      <div className={styles.container}>
        <div className={styles.content_left}>
          <img src="/assets/images/logo.png"></img>
        </div>
        <div className={styles.content_right}>
          {checkmail ? (
            <CheckMail />
          ) : (
            <ForgotPasswordForm setCheckMail={setCheckMail} />
          )}
        </div>
      </div>

      {/* <div className="row" >
        <div className="col-6" 
             style={{  background: "#F7F7FC", backgroundImage: "url(" + " /assets/images/bg-image.jpg" + ")",
             margin: "0", height: "100vh", backgroundSize: "cover", backgroundPosition: "center" }}>
         
          <img src= "/assets/images/logo.png" 
            style={{ height: "62px", width: "#62px", zIndex: 1, margin: "50px 0 0 50px"  }}></img>
          
        </div>        
        <div className="col-6">
          <div style={{ margin: "40px 0 0 10px"}}>
            <Link href="/auth/login">
              <a style={{ fontSize: "22px", textDecoration: "none", color: "#AAAAAA", display: "flex", }}>
              <MdKeyboardArrowLeft style={{ fontSize: "36px", color: "#000000"}}/>back
              </a>
            </Link> 
          </div>
          <div className="row justify-content-center">
            <section className="col-9 text-center p-5">
              <h1
                className="pb-3"
                style={{ fontWeight: "bolder", fontSize: "48px" }}
              >
                Scalework
              </h1>

              <h4 className="pb-5" style={{ fontWeight: 500 }}>
                Reset your password
              </h4>

              <h5 className="pb-5" style={{ fontWeight: 500 }}>
                We'll send you instrucions to reset <br />
                your password and get you back on track
              </h5>

              <ForgotPasswordForm />
            </section>
          </div>
        </div>
      </div> */}
    </MainLayout>
  );
}
