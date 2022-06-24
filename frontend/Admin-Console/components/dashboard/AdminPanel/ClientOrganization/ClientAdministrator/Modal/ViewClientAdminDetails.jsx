import InfoPrompt from "../../../../../Layout/InfoPrompt";
import styles from "../../../../../../styles/dashboard/AdminPanel/Modal/viewdetails.module.css";

export default function ViewClientAdminDetail({ clientDetail }) {
  const { textBox, header, subinfo } = styles;

  return (
    <InfoPrompt id="view-client-admin" title={clientDetail.name}>
      <div id="cliad-det-prof-img" className={header}>
        <img
          src={clientDetail.image ? clientDetail.image : "/profile-view.svg"}
        />

        <h2>{clientDetail.name}</h2>
      </div>
      <div className={textBox} id="cla-det-txt">
        <div className="user-detail-item" id="em-sec-vcad">
          <span id="em-ico-vcad">
            <img src="/email-icon.svg" />
          </span>
          <span id="emtxt-vcad" className={subinfo}>{clientDetail.email}</span>
        </div>
        <div className="user-detail-item" id="phn-sec-vcad">
          <span id="phn-ico-vcad">
          <img src="/phone-icon.svg" />
          </span>
          <span id="phntxt-vcad" className={subinfo}>{clientDetail.phone_number}</span>
        </div>
        <div className="user-detail-item" id="crol-sec-vcad">
          <span id="crol-ico-vcad">
          <img src="/client-icon.svg" />
          </span>
          <span id="crol-vcad" className={subinfo}>{clientDetail.role}</span>
        </div>
      </div>
    </InfoPrompt>
  );
}
