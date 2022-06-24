import React from "react";
import styles from "../../../../styles/Homepage/MainContent/reports/recents.module.css";

export default function RecentProjects() {
    
  //Define styles
  const {
    recents_tab,
    horizon_division,
    recent1,
    recent2,
    recent3,
    recent4,
    recent5,
    recent6,
    btn_recent1,
    btn_recent2,
    btn_recent3,
    btn_recent4,
    btn_recent5,
    btn_recent6,
    card,
    card_title,
    card_content,
    card_footer
  } = styles;

  return (
    <div>
      <div className={recents_tab}>
        <div className={card}>
          <div className={card_title}>
            <b>CP</b>
            <b>Community</b>
            <span>Just Now</span>
          </div>

          <div className={card_content}>
            When you have multiple toasts, we default to vertically
          </div>
          <div className={card_footer}>
            pending invites
            <span style={{ background: "#3B71FA", padding: "4px 7px" }}>1</span>
          </div>
        </div>

        <div className={card}>
          <div className={card_title}>
            <b style={{ background: "#FDC132", color: "#ffffff" }}>RO</b>
            <b style={{ color: "#FDC132" }}>ROGG</b>
            <span>Just Now</span>
          </div>

          <div className={card_content}>
            When you have multiple toasts, we default to vertically
          </div>
          <div className={card_footer}>
            pending invites
            <span style={{ background: "#3B71FA", padding: "4px 7px" }}>1</span>
          </div>
        </div>
      </div>
    </div>
  );
}
