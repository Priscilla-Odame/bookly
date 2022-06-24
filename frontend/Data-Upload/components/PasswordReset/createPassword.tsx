import Link from "next/link";
import { IoMdEye } from "react-icons/io";
import axios from "axios";
import { useForm, SubmitHandler } from "react-hook-form";
import { MdKeyboardArrowLeft } from "react-icons/md";
import styles from "../../styles/PasswordReset/passwordreset.module.css";
import { useState } from "react";
import Validation from "../Auth/Validations";
import { useRouter } from "next/router";
import "react-toastify/dist/ReactToastify.css";
import { toast } from "react-toastify";

toast.configure();

interface IFormInput {
  password: string;
}

const CreatePassword = ({ setPasswordChanged }) => {
  const { query } = useRouter();
  const {
    register,
    formState: errors,
    handleSubmit,
  }: any = useForm<IFormInput>();
  const [showPassword, setShowPassword] = useState<boolean>(false);

  const onSubmit: SubmitHandler<IFormInput> = (data) => {
    //Endpoint -- url for making signup calls
    const url = `${process.env.API_URL}/api/password_reset_complete`;

    axios
      .patch(url, {
        password: data.password,
        token: query.token,
        uidb64: query.uidb64,
      })
      .then((resp) => {
        //If user credentials are correct and login successful
        if (resp.status == 200) {
          setPasswordChanged(true);
        }
      })
      .catch((err) => {
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
        <h3>Create New Password</h3>
        <p>Your new password must be different from your old password</p>

        <form className={styles.form} onSubmit={handleSubmit(onSubmit)}>
          <div className={styles.input_group}>
            <input
              {...register("password", { required: true, minLength: 6 })}
              name="password"
              type={showPassword ? "text" : "password"}
              id="Resetpassword"
              placeholder="New Password"
              className={styles.input}
            />
            <IoMdEye
              className={styles.password_icon}
              onClick={() => {
                setShowPassword(!showPassword);
              }}
            />{" "}
            <br />
            {errors?.password && (
              <Validation variant="danger">
                {errors.password?.type === "required" && "Password is required"}
                {errors.password?.type === "minLength" &&
                  "Password length should be greater than 6"}
              </Validation>
            )}
          </div>

          <div className={styles.input_group}>
            <input
              {...register("Cpassword", { required: true, minLength: 6 })}
              name="Cpassword"
              type={showPassword ? "text" : "password"}
              id="Cpassword"
              placeholder="Confirm Password"
              className={styles.input}
            />
            <IoMdEye
              className={styles.password_icon}
              onClick={() => {
                setShowPassword(!showPassword);
              }}
            />{" "}
            <br />
            {errors?.password && (
              <Validation variant="danger">
                {errors.password?.type === "required" && "Password is required"}
                {errors.password?.type === "minLength" &&
                  "Password length should be greater than 6"}
              </Validation>
            )}
          </div>

          <button type="submit" className={styles.btn}>
            Reset
          </button>
        </form>
      </div>
    </div>
  );
};
export default CreatePassword;
