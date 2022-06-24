import styles from "../../../../styles/upload/header.module.css";


//Check user internet connection status
function InternetOffline(){
        return(
            <>
                <div className={styles.InterntOffline}>
                    <p>Your are Offline... Please check your connection</p>
                </div>
            </>
        );
};

export {InternetOffline}
