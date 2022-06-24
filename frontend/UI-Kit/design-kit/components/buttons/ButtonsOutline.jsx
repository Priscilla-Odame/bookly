import React from "react";
import styles from "../../styles/buttons/button-outline.module.css";
import classNames from 'classnames';

const ButtonOutline = () => {
  const {
    // btnDefaults_Heading,
    // btnRounded_Heading,
    btnPrimary,
    btnSecondary,
    btnTertiary,
    btnSuccess,
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
          <div className={btnDefault}>
            <div className={button}>
              <button className={classNames({[btn_default_large]:true, [btnPrimary]: true})} style={{borderRadius: "16px"}} id="button-primary-h">
                Primary
              </button>

              <button className={classNames({[btn_default_large]:true, [btnSecondary]: true})} style={{borderRadius: "16px"}} id="button-secondary">
                Secondary
              </button>

              <button className={classNames({[btn_default_large]:true, [btnTertiary]: true})} style={{borderRadius: "16px"}} id="button-tertiary">
                Tertiary
              </button>
              <button className={classNames({[btn_default_large]:true, [btnSuccess]: true})} style={{borderRadius: "16px"}} id="button-success">
                Success
              </button>
            </div>

            <div className={button}>
              <button className={classNames({[btn_default_medium]:true, [btnPrimary]:true})} style={{borderRadius: "16px"}} id="button-primary">
                Primary
              </button>

              <button className={classNames({[btn_default_medium]:true, [btnSecondary]:true})} style={{borderRadius: "16px"}} id="button-secondary">
                Secondary
              </button>

              <button className={classNames({[btn_default_medium]:true, [btnTertiary]:true})} style={{borderRadius: "16px"}} id="button-tertiary">
                Tertiary
              </button>
              <button className={classNames({[btn_default_medium]:true, [btnSuccess]:true})} style={{borderRadius: "16px"}} id="button-success">
                Success
              </button>
            </div>

            <div className={button}>
              <button className={classNames({[btn_default_small]:true, [btnPrimary]:true})} style={{borderRadius: "16px"}} id="button-primary">
                Primary
              </button>

              <button className={classNames({[btn_default_small]:true, [btnSecondary]:true})} style={{borderRadius: "16px"}} id="button-secondary">
                Secondary
              </button>

              <button className={classNames({[btn_default_small]:true, [btnTertiary]:true})} style={{borderRadius: "16px"}} id="button-tertiary">
                Tertiary
              </button>
              <button className={classNames({[btn_default_small]:true, [btnSuccess]:true})} style={{borderRadius: "16px"}} id="button-success">
                Success
              </button>
            </div>
          </div>

          <div className={btn_Rounded}>
            <div className={button}>
              <button className={classNames({[btn_rounded_large]:true, [btnPrimary]:true})} style={{borderRadius: "50px"}} id="button-primary">
                Primary
              </button>

              <button className={classNames({[btn_rounded_large]:true, [btnSecondary]:true})} style={{borderRadius: "50px"}} id="button-secondary">
                Secondary
              </button>

              <button className={classNames({[btn_rounded_large]:true, [btnTertiary]:true})} style={{borderRadius: "50px"}} id="button-tertiary">
                Tertiary
              </button>
              <button className={classNames({[btn_rounded_large]:true, [btnSuccess]:true})} style={{borderRadius: "50px"}} id="button-success">
                Success
              </button>
            </div>

            <div className={button}>
              <button className={classNames({[btn_rounded_medium]:true, [btnPrimary]:true})} style={{borderRadius: "50px"}} id="button-primary">
                Primary
              </button>

              <button className={classNames({[btn_rounded_medium]:true, [btnSecondary]:true})} style={{borderRadius: "50px"}} id="button-secondary">
                Secondary
              </button>

              <button className={classNames({[btn_rounded_medium]:true, [btnTertiary]:true})} style={{borderRadius: "50px"}} id="button-tertiary">
                Tertiary
              </button>
              <button className={classNames({[btn_rounded_medium]:true, [btnSuccess]:true})} style={{borderRadius: "50px"}} id="button-success">
                Success
              </button>
            </div>

            <div className={button}>
              <button className={classNames({[btn_rounded_small]:true, [btnPrimary]:true})} style={{borderRadius: "50px"}} id="button-primary">
                Primary
              </button>

              <button className={classNames({[btn_rounded_small]:true, [btnSecondary]:true})} style={{borderRadius: "50px"}} id="button-secondary">
                Secondary
              </button>

              <button className={classNames({[btn_rounded_small]:true, [btnTertiary]:true})} style={{borderRadius: "50px"}} id="button-tertiary">
                Tertiary
              </button>
              <button className={classNames({[btn_rounded_small]:true, [btnSuccess]:true})} style={{borderRadius: "50px"}} id="button-success">
                Success
              </button>
            </div>
          </div>
        </div>

    </div>
  );
};

export default ButtonOutline;
