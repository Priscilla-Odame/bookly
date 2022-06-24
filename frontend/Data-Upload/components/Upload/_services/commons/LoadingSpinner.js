import "react-circular-progressbar/dist/styles.css";
import CircularProgress from "@material-ui/core/CircularProgress";


//File upload circular progress
function UploadSpinner() {
  return (
    <>
      <CircularProgress color="secondary" variant="indeterminate" />
      <p>Your file is Uploading...</p>
    </>
  );
}

export default UploadSpinner;