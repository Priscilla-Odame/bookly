import InfoPrompt from "../../../../../Layout/InfoPrompt";

export default function ViewContactDetail({ contactDetail }) {
  return (
    <InfoPrompt id="view-contact-detail">
      <div>
        {contactDetail.image ? (
          <img src={contactDetail.image} />
        ) : (
         <></>
        )}
        <h2>{contactDetail.name}</h2>
      </div>
      <div className="user-detail-item">
        <span>
          <svg
            width="32"
            height="32"
            viewBox="0 0 32 32"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M26.6666 5.33337H5.33329C3.86663 5.33337 2.67996 6.53337 2.67996 8.00004L2.66663 24C2.66663 25.4667 3.86663 26.6667 5.33329 26.6667H26.6666C28.1333 26.6667 29.3333 25.4667 29.3333 24V8.00004C29.3333 6.53337 28.1333 5.33337 26.6666 5.33337ZM26.6666 10.6667L16 17.3334L5.33329 10.6667V8.00004L16 14.6667L26.6666 8.00004V10.6667Z"
              fill="black"
            />
          </svg>
        </span>
        <span>
            {contactDetail.email}
        </span>
      </div>
      <div className="user-detail-item">
        <span>
          <svg
            width="32"
            height="32"
            viewBox="0 0 32 32"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M26.6666 5.33337H5.33329C3.86663 5.33337 2.67996 6.53337 2.67996 8.00004L2.66663 24C2.66663 25.4667 3.86663 26.6667 5.33329 26.6667H26.6666C28.1333 26.6667 29.3333 25.4667 29.3333 24V8.00004C29.3333 6.53337 28.1333 5.33337 26.6666 5.33337ZM26.6666 10.6667L16 17.3334L5.33329 10.6667V8.00004L16 14.6667L26.6666 8.00004V10.6667Z"
              fill="black"
            />
          </svg>
        </span>
        <span>
            {contactDetail.phone_number}
        </span>
      </div>
      <div className="user-detail-item">
        <span>
          <svg
            width="32"
            height="32"
            viewBox="0 0 32 32"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M26.6666 5.33337H5.33329C3.86663 5.33337 2.67996 6.53337 2.67996 8.00004L2.66663 24C2.66663 25.4667 3.86663 26.6667 5.33329 26.6667H26.6666C28.1333 26.6667 29.3333 25.4667 29.3333 24V8.00004C29.3333 6.53337 28.1333 5.33337 26.6666 5.33337ZM26.6666 10.6667L16 17.3334L5.33329 10.6667V8.00004L16 14.6667L26.6666 8.00004V10.6667Z"
              fill="black"
            />
          </svg>
        </span>
        <span>
            {contactDetail.role}
        </span>
      </div>
    </InfoPrompt>
  );
}
