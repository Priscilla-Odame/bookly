import { useForm, SubmitHandler } from "react-hook-form";
import Validation from "./Validations";
import Link from "next/link";
import styles from "../../styles/PasswordReset/passwordreset.module.css";
import axios from "axios";
import { useRouter } from "next/router";
import { IoMdEye } from "react-icons/io";
import { useState } from "react";
import "react-toastify/dist/ReactToastify.css";
import { toast } from "react-toastify";

toast.configure();

interface IFormInput {
  email: string;
  password: string;
}

const LoginForm = () => {
  const router = useRouter();
  const [showPassword, setShowPassword] = useState<boolean>(false);
  const {
    register,
    formState: { errors },
    handleSubmit,
  }: any = useForm<IFormInput>();

  //function to submit login form data
  const onSubmit: SubmitHandler<IFormInput> = (data) => {
    //Endpoint -- url for making login calls "https://pushinsights-be.azurewebsites.net/api/user/login"
    const url = `${process.env.API_URL}/api/user/login`;

    axios
      .post(url, {
        email: data.email,
        password: data.password,
      })
      .then((resp) => {
        //If user credentials are correct and login successful
        if (resp.status == 200) {
          toast.success("Login successful");
          window.localStorage.setItem("user-data", JSON.stringify(resp.data));
          router.push("/upload");
        }
      })
      .catch(() => {
        toast.error("Sorry, an Error Occurred");
      });
  };

  return (
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
            id="signup-email"
          />
        </div>
        {errors?.email && (
          <Validation variant="danger">
            {errors.email?.type === "required" && "Email is required"}
            {errors.email?.type === "pattern" && "Email is not valid"}
          </Validation>
        )}
      </div>

      <div>
        <div className={styles.input_group}>
          <label htmlFor="password"></label>
          <input
            {...register("password", { required: true, minLength: 6 })}
            type={showPassword ? "text" : "password"}
            placeholder="Password"
            className={styles.input}
            id="signup-password"
          />
          <IoMdEye
            className={styles.password_icon}
            onClick={() => {
              setShowPassword(!showPassword);
            }}
          />
        </div>
        {errors?.password && (
          <Validation variant="danger">
            {errors.password?.type === "required" && "Password is required"}
            {errors.password?.type === "minLength" &&
              "Password length should be greater than 6"}
          </Validation>
        )}
      </div>

      <div>
        <Link href="/auth/forgot_password">
          <a className={styles.fp_link}>Forgot password?</a>
        </Link>
      </div>

      <div>
        <button className={styles.btn} type="submit">
          Login
        </button>
      </div>
    </form>
  );
};

export default LoginForm;
