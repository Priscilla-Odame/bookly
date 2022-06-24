import styles from "../../styles/dashboard/AdminPanel/Modal/prompt.module.css";
import { TiDelete } from "react-icons/ti";

export default function Prompt({ children, id, title }) {
  const { modalbox, header, closeModalButton } = styles;

  return (
    <div id={id} className="modal" role="dialog">
      <div className="modal-dialog" role="document">
        <div className={`${modalbox} modal-content`}>
          <h5 className={`${header} ml-5`}>{title}</h5>
          <TiDelete className={closeModalButton}
                data-dismiss="modal"
                aria-label="Close"
              />
          <div className="modal-body">{children}</div>
        </div>
      </div>
    </div>
  );
}
