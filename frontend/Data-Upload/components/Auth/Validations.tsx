import styles from "./validation.module.css";

export default function Validation({ children }: any) {
  return <div className={styles.alert}>{children}</div>;
}
