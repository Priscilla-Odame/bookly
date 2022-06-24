import { useForm, SubmitHandler } from "react-hook-form";
import Validation from "./Validations";
import Link from "next/link";
import axios from "axios";
import styles from "../../styles/PasswordReset/passwordreset.module.css";
import { MdKeyboardArrowLeft } from "react-icons/md";
import "react-toastify/dist/ReactToastify.css";
import { toast } from "react-toastify";

toast.configure();

interface IFormInput {
  email: string;
}

const ForgotPasswordForm = ({ setCheckMail }) => {
  const {
    register,
    formState: { errors },
    handleSubmit,
  }: any = useForm<IFormInput>();

  //function to submit password to reset
  const onSubmit: SubmitHandler<IFormInput> = (data) => {
    //Endpoint -- url for making signup calls
    const url = `${process.env.API_URL}/api/request_password_reset`;

    axios
      .post(url, {
        email: data.email,
      })
      .then((resp) => {
        //If user credentials are correct and login successful
        if (resp.status == 200) {
          setCheckMail(true);
        }
      })
      .catch(() => {
        toast.error("Sorry, an Error Occurred");
      });
  };

  return (
    <div className={styles.main}>
      <div className={styles.content_top}>
        <Link href="/auth/login">
          <a className={styles.back_button}>
            <MdKeyboardArrowLeft
              style={{ fontSize: "36px", color: "#000000" }}
            />{" "}
            back
          </a>
        </Link>
      </div>
      <div className={styles.content}>
        <h3>Scalework</h3>
        <h4>Reset your password</h4>
        <p>
          We'll send you instructions to reset your password and get you back on
          track
        </p>

        <form onSubmit={handleSubmit(onSubmit)}>
          <div>
            <div className={styles.input_group}>
              <label htmlFor="email"></label>
              <input
                {...register("email", {
                  required: true,
                  pattern: /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/,
                })}
                name="email"
                placeholder="Email"
                className={styles.input}
                id="forgot-password-email"
              />
            </div>
            {errors?.email && (
              <Validation variant="danger">
                {errors.email?.type === "required" && "Email is required"}
                {errors.email?.type === "pattern" && "Email is not valid"}
              </Validation>
            )}
          </div>

          <div className="">
            <button className={styles.btn} type="submit">
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default ForgotPasswordForm;
