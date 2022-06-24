import styles from "../../styles/dashboard/AdminPanel/Modal/prompt.module.css";
import { TiDelete } from "react-icons/ti";

export default function Prompt({ children, id, title }) {
  const { modalboxinfo, closeModalButton } = styles;

  return (
    <div id={id} className="modal" role="dialog">
      <div className="modal-dialog" role="document">
        <div className={`${modalboxinfo} modal-content`}>
          <div>
            <TiDelete
              className={closeModalButton}
              data-dismiss="modal"
              aria-label="Close"
            />
          </div>
          <div className="modal-body">{children}</div>
        </div>
      </div>
    </div>
  );
}
