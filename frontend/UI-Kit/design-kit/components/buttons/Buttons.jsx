import React from "react";
import styles from "../../styles/buttons/buttons.module.css";

const Buttons = () => {
  const {
    btnDefaults_Heading,
    btnRounded_Heading,
    btnDefault,
    btn_default_large,
    btn_default_medium,
    btn_default_small,
    btn_Rounded,
    btn_rounded_large,
    btn_rounded_medium,
    btn_rounded_small,
    button
  } = styles;
  return (
    <div>

        <div>
          {/* <div className={btnDefaults_Heading}>
            <h3>Default Buttons</h3>
          </div>
          <div className={btnRounded_Heading}>
            <h3>Rounded Buttons</h3>
          </div> */}
          <div className={btnDefault}>
            <div className={button}>
              <button className={btn_default_large} style={{background: "#DF265E", borderRadius: "16px"}} id="button-primary">
                Primary
              </button>

              <button className={btn_default_large} style={{background: "#2F80ED", borderRadius: "16px"}} id="button-secondary">
                Secondary
              </button>

              <button className={btn_default_large} style={{background: "#0FCDF7", borderRadius: "16px"}} id="button-tertiary">
                Tertiary
              </button>
              <button className={btn_default_large} style={{background: "#12D09D", borderRadius: "16px"}} id="button-success">
                Success
              </button>
            </div>

            <div className={button}>
              <button className={btn_default_medium} style={{background: "#DF265E", borderRadius: "16px"}} id="button-primary">
                Primary
              </button>

              <button className={btn_default_medium} style={{background: "#2F80ED", borderRadius: "16px"}} id="button-secondary">
                Secondary
              </button>

              <button className={btn_default_medium} style={{background: "#0FCDF7", borderRadius: "16px"}} id="button-tertiary">
                Tertiary
              </button>
              <button className={btn_default_medium} style={{background: "#12D09D", borderRadius: "16px"}} id="button-success">
                Success
              </button>
            </div>

            <div className={button}>
              <button className={btn_default_small} style={{background: "#DF265E", borderRadius: "16px"}} id="button-primary">
                Primary
              </button>

              <button className={btn_default_small} style={{background: "#2F80ED", borderRadius: "16px"}} id="button-secondary">
                Secondary
              </button>

              <button className={btn_default_small} style={{background: "#0FCDF7", borderRadius: "16px"}} id="button-tertiary">
                Tertiary
              </button>
              <button className={btn_default_small} style={{background: "#12D09D", borderRadius: "16px"}} id="button-success">
                Success
              </button>
            </div>
          </div>

          <div className={btn_Rounded}>
            <div className={button}>
              <button className={btn_rounded_large} style={{background: "#DF265E", borderRadius: "50px"}} id="button-primary">
                Primary
              </button>

              <button className={btn_rounded_large} style={{background: "#2F80ED", borderRadius: "50px"}} id="button-secondary">
                Secondary
              </button>

              <button className={btn_rounded_large} style={{background: "#0FCDF7", borderRadius: "50px"}} id="button-tertiary">
                Tertiary
              </button>
              <button className={btn_rounded_large} style={{background: "#12D09D", borderRadius: "50px"}} id="button-success">
                Success
              </button>
            </div>

            <div className={button}>
              <button className={btn_rounded_medium} style={{background: "#DF265E", borderRadius: "50px"}} id="button-primary">
                Primary
              </button>

              <button className={btn_rounded_medium} style={{background: "#2F80ED", borderRadius: "50px"}} id="button-secondary">
                Secondary
              </button>

              <button className={btn_rounded_medium} style={{background: "#0FCDF7", borderRadius: "50px"}} id="button-tertiary">
                Tertiary
              </button>
              <button className={btn_rounded_medium} style={{background: "#12D09D", borderRadius: "50px"}} id="button-success">
                Success
              </button>
            </div>

            <div className={button}>
              <button className={btn_rounded_small} style={{background: "#DF265E", borderRadius: "50px"}} id="button-primary">
                Primary
              </button>

              <button className={btn_rounded_small} style={{background: "#2F80ED", borderRadius: "50px"}} id="button-secondary">
                Secondary
              </button>

              <button className={btn_rounded_small} style={{background: "#0FCDF7", borderRadius: "50px"}} id="button-tertiary">
                Tertiary
              </button>
              <button className={btn_rounded_small} style={{background: "#12D09D", borderRadius: "50px"}} id="button-success">
                Success
              </button>
            </div>
          </div>
        </div>
      
    </div>
  );
};

export default Buttons;
