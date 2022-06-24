import { TiDelete } from "react-icons/ti";
import styles from "../../styles/dashboard/AdminPanel/Modal/bootstrapmodal.module.css";

export default function Modal({ children, id, title }) {
  const { modalbox, header, closeModalButton } = styles;

  return (
    <div id={id} className="modal" tabIndex="-1" role="dialog">
      <div className="modal-dialog" role="document">
        <div className={`${modalbox} modal-content`}>
          <div className="">
            <h5 className={header}>{title}</h5>
            <TiDelete className={closeModalButton}
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
