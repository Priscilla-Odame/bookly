import ForgotPasswordForm from "../../components/Auth/ForgotPasswordForm";
import Link from "next/link";
import MainLayout from "../../components/Layout/MainLayout";
//import reportWebVitals from './reportWebVitals';

export default function Login() {
  return (
    <MainLayout title="Login">
      <div className="row" style={{ height: "1vh" }}>
        <img src="/assets/images/bg.svg" className="col-6"></img>
        <div className="col-6">
          <Link href="/auth/login">
            <a>{"<"} back</a>
          </Link>
          <div className="row justify-content-center">
            <section className="col-9 text-center p-5">
              <h1
                className="pb-5"
                style={{ fontWeight: "bolder", fontSize: "48px" }}
              >
                Scalework
              </h1>

              <h4 className="pb-5" style={{ fontWeight: "bold" }}>
                Reset your password
              </h4>

              <h5 className="pb-5" style={{ fontWeight: "bold" }}>
                We'll send you instrucions to reset <br />
                your password and get you back on track
              </h5>

              <ForgotPasswordForm />
            </section>
          </div>
        </div>
      </div>
    </MainLayout>
  );
}
