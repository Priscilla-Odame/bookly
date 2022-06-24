import { useForm, SubmitHandler } from "react-hook-form";
import Validation from "./Validations";
import Link from "next/link";
import styles from "../../styles/PasswordReset/passwordreset.module.css";
import { IoMdEye } from "react-icons/io";
import axios from "axios";
import { useRouter } from "next/router";
import { useState } from "react";
import { useToken } from "./useToken";
import "react-toastify/dist/ReactToastify.css";
import { toast } from "react-toastify";

//Tostify config
toast.configure();

interface IFormInput {
  email: string;
  password: string;
  fname: string;
  onames: string;
}

const SignUpForm = () => {
  const router = useRouter();
  const [token, setToken] = useToken();
  const [showPassword, setShowPassword] = useState<boolean>(false);
  const {
    register,
    formState: { errors },
    handleSubmit,
  }: any = useForm<IFormInput>();

  //function to submit login form data
  const onSubmit: SubmitHandler<IFormInput> = (data) => {
    //Endpoint -- url for making signup calls
    const url = `${process.env.API_URL}/api/user/signup`;

    axios
      .post(url, {
        email: data.email,
        password: data.password,
        first_name: data.fname,
        other_names: data.onames,
      })
      .then((resp) => {
        //If user credentials are correct and signup successful
        if (resp.status == 201) {
          toast.success("Signup Successful");
          router.push("/auth/login");
        }
      })
      .catch(() => {
        toast.error("Sorry, an Error Occurred");
      });
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className={styles.form}>
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
          <label htmlFor="first-name"></label>
          <input
            {...register("fname", { required: true })}
            type="name"
            placeholder="First name"
            className={styles.input}
            id="signup-first-name"
          />
        </div>
        {errors?.fname && (
          <Validation variant="danger">
            {errors.fname?.type === "required" && "First Name is required"}
          </Validation>
        )}
      </div>
      <div>
        <div className={styles.input_group}>
          <label htmlFor="other-names"></label>
          <input
            {...register("onames")}
            type="name"
            placeholder="Last name"
            className={styles.input}
            id="signup-other-names"
          />
        </div>
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

      <div className={styles.tsp}>
        By creating an account, you agree to our {""}
        <Link href="/auth/forgot_password">
          <a className={styles.ts_link}>Terms and Services</a>
        </Link>
      </div>

      <div>
        <button className={styles.btn} type="submit">
          Register
        </button>
      </div>
    </form>
  );
};

export default SignUpForm;
