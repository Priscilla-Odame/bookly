import { useRouter } from "next/router";
import { FiCheckCircle } from "react-icons/fi";
import styles from "../../styles/PasswordReset/passwordreset.module.css";

const PasswordChanged = () => {
  const router = useRouter();

  return (
    <div className={styles.main_content}>
      <FiCheckCircle
        style={{ fontSize: "100px", color: "#12D09D", marginBottom: "50px" }}
      />
      <h3>Password changed!</h3>
      <p>Your Password has been changed successfully</p>

      <button
        type="button"
        onClick={() => router.push("/auth/login")}
        className={styles.btn}
      >
        Continue
      </button>
    </div>
  );
};
export default PasswordChanged;
